import requests
import random
from PIL import Image, ImageTk
from io import BytesIO
from datetime import datetime
import database_avalon

# Função para ver se o que o usuário digitou no cadastro tá certo
def validar_dados_usuario(nome, gmail, senha):
    if len(nome) < 3:
        return False, "Nome muito curto!"
    
    # Verificação simples de email que a gente aprende no começo
    if "@" not in gmail:
        return False, "E-mail inválido! Falta o @"
    if "." not in gmail:
        return False, "E-mail inválido! Falta o ponto"
        
    if len(senha) < 4:
        return False, "A senha deve ter pelo menos 4 dígitos!"
    
    return True, ""

# Função que vai no Google buscar os livros
def buscar_livros_na_api(query):
    # Monta a URL para pesquisar
    url = "https://www.googleapis.com/books/v1/volumes?q=" + query + "&maxResults=10"
    
    try:
        resposta = requests.get(url)
        dados = resposta.json()
        # Pega a lista de livros que vem dentro de 'items'
        lista_livros = dados.get('items', [])
        return lista_livros
    except:
        print("Deu erro ao buscar livros na internet")
        return []

# Função para carregar a fotinho da capa do livro
def baixar_imagem(url):
    try:
        # Arruma a URL se vier sem o S do HTTPS
        url_segura = url.replace("http://", "https://")
        res = requests.get(url_segura)
        
        # Abre a imagem usando a biblioteca PIL
        img_aberta = Image.open(BytesIO(res.content))
        # Muda o tamanho para caber no quadradinho da tela
        img_redimensionada = img_aberta.resize((120, 180))
        
        # Converte para o formato que o Tkinter aceita
        foto_final = ImageTk.PhotoImage(img_redimensionada)
        return foto_final
    except:
        return None

# Função para somar o valor de tudo que tá no carrinho
def calcular_valor_total(itens_selecionados):
    total = 0
    for item in itens_selecionados:
        if item["tipo"] == "Aluguel":
            # Faz a conta: 15% do preço vezes a quantidade de dias
            preco_base = item["preco_base"]
            dias = item["dias_aluguel"].get()
            valor_item = (preco_base * 0.15) * dias
            total = total + valor_item
        else:
            # Se for compra é só somar o preço normal
            total = total + item["preco_base"]
    return total

# Salva cada item que foi pago no banco de dados
def salvar_venda_completa(usuario_id, itens_para_pagar):
    for i in itens_para_pagar:
        # Calcula o valor de novo para salvar certo no banco
        if i["tipo"] == "Compra":
            valor_venda = i["preco_base"]
        else:
            valor_venda = (i["preco_base"] * 0.15) * i["dias_aluguel"].get()
            
        # Chama a função que criamos no arquivo de banco
        database_avalon.salvar_venda(
            usuario_id, 
            i["titulo"], 
            i["tipo"], 
            valor_venda
        )

# Cria o texto que vai aparecer na nota fiscal
def formatar_nota_fiscal(usuario_nome, itens, total, metodo):
    data_hoje = datetime.now().strftime('%d/%m/%Y %H:%M')
    
    # Montando a nota linha por linha (estilo aluno)
    nota = "==========================================\n"
    nota += "          BIBLIOTECA AVALON LTDA          \n"
    nota += "==========================================\n"
    nota += "DATA: " + data_hoje + "\n"
    nota += "CLIENTE: " + usuario_nome + "\n"
    nota += "PAGAMENTO: " + metodo.upper() + "\n"
    nota += "------------------------------------------\n"
    
    for i in itens:
        nome_livro = i["titulo"][:25]
        if i["tipo"] == "Compra":
            v = i["preco_base"]
            tipo_txt = " (COMPRA)"
        else:
            v = (i["preco_base"] * 0.15) * i["dias_aluguel"].get()
            tipo_txt = " (" + str(i['dias_aluguel'].get()) + " DIAS ALUGUEL)"
            
        nota += nome_livro + " .... R$ " + str(round(v, 2)) + "\n"
        nota += tipo_txt + "\n"
        
    nota += "------------------------------------------\n"
    nota += "TOTAL A PAGAR: R$ " + str(round(total, 2)) + "\n"
    nota += "==========================================\n"
    nota += "              VOLTE SEMPRE!               \n"
    
    return nota
