import requests
import random
from PIL import Image, ImageTk
from io import BytesIO
from datetime import datetime
import database_avalon

def buscar_livros_na_api(query):
    try:
        url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults=10"
        return requests.get(url).json().get('items', [])
    except:
        return []

def baixar_imagem(url):
    try:
        res = requests.get(url.replace("http://", "https://"))
        img = Image.open(BytesIO(res.content)).resize((120, 180), Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    except:
        return None

def calcular_valor_total(itens_selecionados):
    total = 0
    for i in itens_selecionados:
        if i["tipo"] == "Aluguel":
            total += (i["preco_base"] * 0.15) * i["dias_aluguel"].get()
        else:
            total += i["preco_base"]
    return total

def salvar_venda_completa(usuario_id, itens_para_pagar):
    for i in itens_para_pagar:
        v = i["preco_base"] if i["tipo"] == "Compra" else (i["preco_base"]*0.15)*i["dias_aluguel"].get()
        database_avalon.salvar_venda(usuario_id, i["titulo"], i["tipo"], v)

def formatar_nota_fiscal(usuario_nome, itens, total, metodo):
    res = f"{'='*42}\n{'BIBLIOTECA AVALON LTDA':^42}\n{'CNPJ: 12.345.678/0001-99':^42}\n"
    res += f"{'DATA: ' + datetime.now().strftime('%d/%m/%Y %H:%M'):^42}\n{'='*42}\n"
    res += f"CLIENTE: {usuario_nome}\n"
    res += f"METODO: {metodo.upper()}\n{'-'*42}\n"
    for i in itens:
        v = i["preco_base"] if i["tipo"] == "Compra" else (i["preco_base"]*0.15)*i["dias_aluguel"].get()
        res += f"{i['titulo'][:25]:.<25} R$ {v:>7.2f}\n ({i['tipo']})\n"
    res += f"{'-'*42}\n{'TOTAL FINAL:':<25} R$ {total:>7.2f}\n{'='*42}\n"
    res += f"{'Obrigado por sua compra!':^42}\n{'='*42}"
    return res
