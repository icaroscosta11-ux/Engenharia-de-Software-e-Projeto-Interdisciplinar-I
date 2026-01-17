import sqlite3
from datetime import datetime

def conectar():
    return sqlite3.connect("biblioteca_avalon.db")

def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()
    # Tabela de Usuários
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        gmail TEXT UNIQUE NOT NULL,
        senha TEXT NOT NULL,
        endereco TEXT
    )
    """)
    # Tabela de Histórico de Vendas
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
    conn.commit()
    conn.close()

def cadastrar_usuario(nome, gmail, senha, endereco):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nome, gmail, senha, endereco) VALUES (?, ?, ?, ?)", 
                       (nome, gmail, senha, endereco))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False

def verificar_login(gmail, senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE gmail = ? AND senha = ?", (gmail, senha))
    usuario = cursor.fetchone()
    conn.close()
    return usuario

def salvar_venda(usuario_id, titulo, tipo, valor):
    conn = conectar()
    cursor = conn.cursor()
    data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")
    cursor.execute("INSERT INTO historico_vendas (usuario_id, livro_titulo, tipo, valor, data_venda) VALUES (?, ?, ?, ?, ?)",
                   (usuario_id, titulo, tipo, valor, data_atual))
    conn.commit()
    conn.close()
