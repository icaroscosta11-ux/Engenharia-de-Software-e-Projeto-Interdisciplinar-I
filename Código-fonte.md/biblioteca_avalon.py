import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import random
import database_avalon
import funcoes_avalon

class BibliotecaAvalon:
    def __init__(self, root):
        self.root = root
        self.root.title("Biblioteca Avalon - Projeto Final")
        self.root.geometry("1100x850")
        
        # Inicia o banco de dados
        database_avalon.criar_tabelas()
        
        # Listas e variaveis de controle
        self.itens_carrinho = [] 
        self.usuario_logado = None 
        
        # Cores padronizadas do sistema
        self.cor_roxa = "#4B0082" 
        self.cor_verde = "#28a745"
        self.cor_azul = "#17a2b8"

        # Frame onde as telas vao carregar
        self.painel_principal = tk.Frame(self.root)
        self.painel_principal.pack(expand=True, fill="both")

        # Chama a tela de inicio
        self.abrir_tela_inicial()

    def limpar_janela(self):
        # Remove tudo que esta na tela atual
        for widget in self.painel_principal.winfo_children():
            widget.destroy()

    def abrir_tela_inicial(self):
        self.limpar_janela()
        tk.Label(self.painel_principal, text="", pady=30).pack()
        tk.Label(self.painel_principal, text="BIBLIOTECA AVALON", font=("Georgia", 40, "bold"), fg=self.cor_roxa).pack(pady=10)
        tk.Label(self.painel_principal, text="Onde o conhecimento encontra a magia.", font=("Arial", 14, "italic"), fg="#555").pack(pady=5)
        
        texto_boas_vindas = "Bem-vindo ao maior acervo digital de literatura.\nSeu portal para compras e aluguéis de livros."
        tk.Label(self.painel_principal, text=texto_boas_vindas, font=("Arial", 12), pady=30).pack()

        btns_frame = tk.Frame(self.painel_principal)
        btns_frame.pack(pady=20)
        tk.Button(btns_frame, text="CRIAR CONTA", bg=self.cor_roxa, fg="white", font=("Arial", 12, "bold"), width=20, height=2, command=self.ir_para_cadastro).pack(side="left", padx=10)
        tk.Button(btns_frame, text="FAZER LOGIN", bg="white", fg=self.cor_roxa, font=("Arial", 12, "bold"), width=20, height=2, command=self.ir_para_login).pack(side="left", padx=10)

    def ir_para_cadastro(self):
        self.limpar_janela()
        tk.Label(self.painel_principal, text="Cadastro Avalon", font=("Arial", 28, "bold"), fg=self.cor_roxa).pack(pady=20)
        
        tk.Label(self.painel_principal, text="Nome Completo:").pack()
        self.campo_nome = tk.Entry(self.painel_principal, font=("Arial", 12), justify="center")
        self.campo_nome.pack(ipady=5, fill="x", padx=100)
        
        tk.Label(self.painel_principal, text="Gmail:").pack(pady=(10,0))
        self.campo_gmail = tk.Entry(self.painel_principal, font=("Arial", 12), justify="center")
        self.campo_gmail.pack(ipady=5, fill="x", padx=100)
        
        tk.Label(self.painel_principal, text="Senha:").pack(pady=(10,0))
        self.campo_senha = tk.Entry(self.painel_principal, show="*", font=("Arial", 12), justify="center")
        self.campo_senha.pack(ipady=5, fill="x", padx=100)
        
        tk.Label(self.painel_principal, text="Endereço:").pack(pady=(10,0))
        self.campo_end = tk.Entry(self.painel_principal, font=("Arial", 12), justify="center")
        self.campo_end.pack(ipady=5, fill="x", padx=100)
        
        tk.Button(self.painel_principal, text="CADASTRAR", bg=self.cor_roxa, fg="white", font=("Arial", 12, "bold"), width=25, height=2, command=self.processar_cadastro).pack(pady=20)
        tk.Button(self.painel_principal, text="Voltar", command=self.abrir_tela_inicial, relief="flat").pack()

    def processar_cadastro(self):
        n, g, s, e = self.campo_nome.get(), self.campo_gmail.get(), self.campo_senha.get(), self.campo_end.get()
        valido, msg = funcoes_avalon.validar_dados_usuario(n, g, s)
        if not valido:
            messagebox.showwarning("Erro", msg)
            return
        if database_avalon.cadastrar_usuario(n, g, s, e):
            messagebox.showinfo("Sucesso", "Conta criada!")
            self.ir_para_login()
        else:
            messagebox.showerror("Erro", "Email já existe.")

    def ir_para_login(self):
        self.limpar_janela()
        tk.Label(self.painel_principal, text="Login Avalon", font=("Arial", 28, "bold"), fg=self.cor_roxa).pack(pady=40)
        tk.Label(self.painel_principal, text="Gmail:").pack()
        self.login_email = tk.Entry(self.painel_principal, font=("Arial", 12), justify="center")
        self.login_email.pack(ipady=5, fill="x", padx=100)
        tk.Label(self.painel_principal, text="Senha:").pack(pady=(10,0))
        self.login_senha = tk.Entry(self.painel_principal, show="*", font=("Arial", 12), justify="center")
        self.login_senha.pack(ipady=5, fill="x", padx=100)
        tk.Button(self.painel_principal, text="ENTRAR", bg=self.cor_roxa, fg="white", font=("Arial", 12, "bold"), width=25, height=2, command=self.processar_login).pack(pady=20)
        tk.Button(self.painel_principal, text="Criar conta", command=self.ir_para_cadastro, relief="flat").pack()

    def processar_login(self):
        u = database_avalon.verificar_login(self.login_email.get(), self.login_senha.get())
        if u:
            self.usuario_logado = {"id": u[0], "nome": u[1], "gmail": u[2], "endereco": u[4]}
            self.abrir_loja()
        else:
            messagebox.showerror("Erro", "Login incorreto!")

    def abrir_loja(self):
        self.limpar_janela()
        header = tk.Frame(self.painel_principal, bg=self.cor_roxa, height=80)
        header.pack(fill="x")
        
        tk.Button(header, text="📜 Pedidos", bg="#6a5acd", fg="white", command=self.ver_pedidos).pack(side="left", padx=10)
        tk.Label(header, text="Olá, " + self.usuario_logado['nome'].split()[0], fg="white", bg=self.cor_roxa).pack(side="left", padx=10)
        
        self.entrada_busca = tk.Entry(header, font=("Arial", 13))
        self.entrada_busca.pack(side="left", padx=10, ipady=5, expand=True, fill="x")
        tk.Button(header, text="🔍", command=lambda: self.carregar_livros()).pack(side="left", padx=5)
        
        self.btn_carro = tk.Button(header, text=f"🛒 ({len(self.itens_carrinho)})", bg="#FFD700", command=self.ir_para_carrinho)
        self.btn_carro.pack(side="right", padx=20)

        # Barra de scroll
        self.canvas = tk.Canvas(self.painel_principal)
        self.scroll_frame = tk.Frame(self.canvas)
        barra = ttk.Scrollbar(self.painel_principal, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=barra.set)
        barra.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((550, 0), window=self.scroll_frame, anchor="n")
        self.scroll_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        
        self.carregar_livros("Lançamentos")

    def carregar_livros(self, busca=None):
        if not busca: busca = self.entrada_busca.get()
        if not busca: return
        for w in self.scroll_frame.winfo_children(): w.destroy()
        
        itens = funcoes_avalon.buscar_livros_na_api(busca)
        r, c = 0, 0
        self.fotos = []
        for i in itens:
            info = i.get('volumeInfo', {})
            tit = info.get('title', 'Sem título')[:35]
            preco = random.uniform(40, 90)
            card = tk.Frame(self.scroll_frame, bd=1, relief="solid", width=400, height=400)
            card.grid(row=r, column=c, padx=15, pady=15)
            card.pack_propagate(False)
            
            capa = info.get('imageLinks', {}).get('thumbnail')
            if capa:
                img = funcoes_avalon.baixar_imagem(capa)
                if img:
                    l_img = tk.Label(card, image=img); l_img.image = img; l_img.pack()
                    self.fotos.append(img)
            
            tk.Label(card, text=tit, font=("Arial", 10, "bold")).pack(pady=5)
            tk.Label(card, text=f"R$ {round(preco, 2)}", fg="green").pack()
            
            f_b = tk.Frame(card); f_b.pack(side="bottom", pady=10)
            tk.Button(f_b, text="COMPRAR", bg=self.cor_verde, fg="white", command=lambda t=tit, p=preco: self.add_item(t, p, "Compra")).pack(side="left", padx=5)
            tk.Button(f_b, text="ALUGAR", bg=self.cor_azul, fg="white", command=lambda t=tit, p=preco: self.add_item(t, p, "Aluguel")).pack(side="left", padx=5)
            
            c += 1
            if c > 1: c = 0; r += 1

    def add_item(self, t, p, tipo):
        self.itens_carrinho.append({"titulo": t, "preco_base": p, "tipo": tipo, "selecionado": tk.BooleanVar(value=True), "dias_aluguel": tk.IntVar(value=1)})
        self.btn_carro.config(text=f"🛒 ({len(self.itens_carrinho)})")
        messagebox.showinfo("Avalon", f"{t} adicionado!")

    def ir_para_carrinho(self):
        self.limpar_janela()
        topo = tk.Frame(self.painel_principal, bg=self.cor_roxa, height=80)
        topo.pack(fill="x")
        tk.Button(topo, text="← Voltar", command=self.abrir_loja).pack(side="left", padx=20)
        
        self.area_lista = tk.Frame(self.painel_principal, padx=50, pady=20)
        self.area_lista.pack(fill="both", expand=True)
        self.desenhar_carrinho()

    def desenhar_carrinho(self):
        for w in self.area_lista.winfo_children(): w.destroy()
        
        marcados = [i for i in self.itens_carrinho if i["selecionado"].get()]
        total = funcoes_avalon.calcular_valor_total(marcados)
        
        for idx, item in enumerate(self.itens_carrinho):
            f = tk.Frame(self.area_lista, pady=5, bd=1, relief="groove")
            f.pack(fill="x", pady=2)
            tk.Checkbutton(f, variable=item["selecionado"], command=self.desenhar_carrinho).pack(side="left", padx=10)
            tk.Label(f, text=item["titulo"][:40], width=40, anchor="w").pack(side="left")
            
            if item["tipo"] == "Aluguel":
                tk.Spinbox(f, from_=1, to=10, width=3, textvariable=item["dias_aluguel"], command=self.desenhar_carrinho).pack(side="left")
                v = (item["preco_base"] * 0.15) * item["dias_aluguel"].get()
            else:
                tk.Label(f, text="Compra", width=8).pack(side="left")
                v = item["preco_base"]
            
            tk.Label(f, text=f"R$ {round(v, 2)}", font=("Arial", 10, "bold")).pack(side="left", padx=20)
            tk.Button(f, text="X", bg="red", fg="white", command=lambda i=idx: [self.itens_carrinho.pop(i), self.desenhar_carrinho()]).pack(side="right", padx=10)
            
        tk.Label(self.area_lista, text=f"TOTAL: R$ {round(total, 2)}", font=("Arial", 18, "bold"), fg=self.cor_roxa).pack(pady=20)
        tk.Button(self.area_lista, text="PAGAMENTO", bg=self.cor_verde, fg="white", font=("Arial", 12, "bold"), command=self.ir_pagamento).pack()

    def ir_pagamento(self):
        self.itens_pagar = [i for i in self.itens_carrinho if i["selecionado"].get()]
        if not self.itens_pagar: return
        self.limpar_janela()
        
        # Topo
        f_topo = tk.Frame(self.painel_principal, bg=self.cor_roxa, height=40).pack(fill="x")
        
        corpo = tk.Frame(self.painel_principal, padx=30, pady=20)
        corpo.pack(fill="both")
        
        # Lado Esquerdo
        esq = tk.LabelFrame(corpo, text=" Itens do Pedido ", padx=15, pady=15)
        esq.pack(side="left", fill="both", expand=True)
        for i in self.itens_pagar:
            tk.Label(esq, text=f"> {i['titulo'][:30]}...").pack(anchor="w")
        
        self.total_final = funcoes_avalon.calcular_valor_total(self.itens_pagar)
        tk.Label(esq, text=f"\nTOTAL FINAL: R$ {round(self.total_final, 2)}", font=("Arial", 12, "bold")).pack(anchor="w")
        
        # Lado Direito (Igual à sua imagem)
        self.dir = tk.LabelFrame(corpo, text=" Escolha como pagar ", padx=15, pady=15)
        self.dir.pack(side="right", fill="both", expand=True, padx=(20,0))
        
        self.metodo = tk.StringVar(value="pix")
        tk.Radiobutton(self.dir, text="Pagar com Pix", variable=self.metodo, value="pix", command=self.mudar_campos).pack(anchor="w")
        tk.Radiobutton(self.dir, text="Boleto Bancário", variable=self.metodo, value="boleto", command=self.mudar_campos).pack(anchor="w")
        tk.Radiobutton(self.dir, text="Cartão de Crédito", variable=self.metodo, value="cartao", command=self.mudar_campos).pack(anchor="w")
        
        self.f_detalhes = tk.Frame(self.dir, pady=10)
        self.f_detalhes.pack(fill="both")
        self.mudar_campos()
        
        tk.Button(self.painel_principal, text="FINALIZAR COMPRA", bg=self.cor_verde, fg="white", font=("Arial", 15, "bold"), height=2, command=self.finalizar).pack(pady=30)

    def mudar_campos(self):
        for w in self.f_detalhes.winfo_children(): w.destroy()
        m = self.metodo.get()
        if m == "pix":
            tk.Label(self.f_detalhes, text="Chave Pix:").pack(anchor="w")
            e = tk.Entry(self.f_detalhes); e.insert(0, "pagar@avalon.com"); e.pack(fill="x")
        elif m == "boleto":
            tk.Label(self.f_detalhes, text="Linha Digitável:").pack(anchor="w")
            tk.Label(self.f_detalhes, text="34191.09008 63561.760409...", fg="blue").pack()
        else:
            tk.Label(self.f_detalhes, text="Número do Cartão:").pack(anchor="w")
            tk.Entry(self.f_detalhes).pack(fill="x")

    def finalizar(self):
        funcoes_avalon.salvar_venda_completa(self.usuario_logado["id"], self.itens_pagar)
        
        # Nota Fiscal
        nf = tk.Toplevel(self.root)
        nf.geometry("450x600")
        t = tk.Text(nf, font=("Courier", 10), padx=20, pady=20)
        t.pack(fill="both", expand=True)
        conteudo = funcoes_avalon.formatar_nota_fiscal(self.usuario_logado['nome'], self.itens_pagar, self.total_final, self.metodo.get())
        t.insert("1.0", conteudo)
        t.config(state="disabled")
        
        self.itens_carrinho = [i for i in self.itens_carrinho if not i["selecionado"].get()]
        self.btn_carro.config(text=f"🛒 ({len(self.itens_carrinho)})")
        tk.Button(nf, text="FECHAR", command=lambda: [nf.destroy(), self.abrir_loja()]).pack(pady=10)

    def ver_pedidos(self):
        vendas = database_avalon.obter_historico(self.usuario_logado["id"])
        janela = tk.Toplevel(self.root)
        janela.geometry("600x400")
        if not vendas:
            tk.Label(janela, text="Sem pedidos.").pack(pady=50)
        else:
            tab = ttk.Treeview(janela, columns=("L", "T", "V", "D"), show="headings")
            tab.heading("L", text="Livro"); tab.heading("V", text="Valor")
            for v in vendas: tab.insert("", "end", values=(v[0], v[1], v[2], v[3]))
            tab.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = tk.Tk()
    BibliotecaAvalon(app)
    app.mainloop()
