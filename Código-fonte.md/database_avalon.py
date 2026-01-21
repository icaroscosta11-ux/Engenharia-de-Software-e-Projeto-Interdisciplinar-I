import sqlite3
from datetime import datetime

# Função para criar o banco e as tabelas (o aluno geralmente coloca tudo junto)
def criar_tabelas():
    # Abre a conexão com o arquivo do banco
    con = sqlite3.connect("biblioteca_avalon.db")
    cursor = con.cursor()
    
    # Criando a tabela de quem vai usar o sistema
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        gmail TEXT UNIQUE NOT NULL,
        senha TEXT NOT NULL,
        endereco TEXT
    )
    """)
    
    # Criando a tabela para salvar o que foi comprado ou alugado
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS historico_vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER,
        livro_titulo TEXT,
        tipo TEXT,
        valor REAL,
        data_venda TEXT,
        FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
    )
    """)
    
    con.commit()
    con.close()

# Função para salvar um novo usuário no sistema
def cadastrar_usuario(nome, gmail, senha, endereco):
    try:
        con = sqlite3.connect("biblioteca_avalon.db")
        cursor = con.cursor()
        # Comando para inserir os dados que o usuário digitou
        cursor.execute("INSERT INTO usuarios (nome, gmail, senha, endereco) VALUES (?, ?, ?, ?)", 
                       (nome, gmail, senha, endereco))
        con.commit()
        con.close()
        return True
    except:
        # Se der erro (tipo gmail repetido), ele retorna falso
        return False

# Função para conferir se o login está certo
def verificar_login(gmail, senha):
    con = sqlite3.connect("biblioteca_avalon.db")
    cursor = con.cursor()
    # Procura no banco um usuario que tenha esse email e essa senha
    cursor.execute("SELECT * FROM usuarios WHERE gmail = ? AND senha = ?", (gmail, senha))
    usuario = cursor.fetchone() # Pega o resultado
    con.close()
    return usuario

# Função para buscar os dados de um usuario pelo ID dele
def buscar_usuario_por_id(id_user):
    con = sqlite3.connect("biblioteca_avalon.db")
    cursor = con.cursor()
    cursor.execute("SELECT id, nome, gmail, endereco FROM usuarios WHERE id = ?", (id_user,))
    resultado = cursor.fetchone()
    con.close()
    return resultado

# Função para mudar os dados do cadastro
def atualizar_usuario(id_user, nome, gmail, endereco):
    con = sqlite3.connect("biblioteca_avalon.db")
    cursor = con.cursor()
    cursor.execute("UPDATE usuarios SET nome = ?, gmail = ?, endereco = ? WHERE id = ?", 
                   (nome, gmail, endereco, id_user))
    con.commit()
    con.close()

# Função para deletar uma conta
def deletar_usuario(id_user):
    con = sqlite3.connect("biblioteca_avalon.db")
    cursor = con.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_user,))
    con.commit()
    con.close()

# Função que salva a compra ou aluguel no histórico
def salvar_venda(id_user, titulo, tipo, valor):
    con = sqlite3.connect("biblioteca_avalon.db")
    cursor = con.cursor()
    # Pega a data e hora do momento da compra
    agora = datetime.now()
    data_formatada = agora.strftime("%d/%m/%Y %H:%M")
    
    cursor.execute("INSERT INTO historico_vendas (usuario_id, livro_titulo, tipo, valor, data_venda) VALUES (?, ?, ?, ?, ?)", 
                   (id_user, titulo, tipo, valor, data_formatada))
    con.commit()
    con.close()

# Função para mostrar o histórico na tela do usuário
def obter_historico(id_user):
    con = sqlite3.connect("biblioteca_avalon.db")
    cursor = con.cursor()
    # Pega as vendas do mais novo para o mais antigo
    cursor.execute("SELECT livro_titulo, tipo, valor, data_venda FROM historico_vendas WHERE usuario_id = ? ORDER BY id DESC", (id_user,))
    lista_vendas = cursor.fetchall()
    con.close()
    return lista_vendas
