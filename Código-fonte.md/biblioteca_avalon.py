import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import database_avalon
import funcoes_avalon  # Importando o novo arquivo de funções

class BibliotecaAvalon:
    def __init__(self, root):
        self.root = root
        self.root.title("Biblioteca Avalon")
        self.root.geometry("1100x850")
        
        database_avalon.criar_tabelas()
        
        self.itens_carrinho = [] 
        self.usuario_logado = None 
        
        self.cor_principal = "#4B0082" 
        self.cor_botao_compra = "#28a745"
        self.cor_botao_aluguel = "#17a2b8"

        self.container = tk.Frame(self.root)
        self.container.pack(expand=True, fill="both")

        self.tela_inicial()

    def limpar_tela(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def tela_inicial(self):
        self.limpar_tela()
        tk.Label(self.container, text="", pady=30).pack()
        tk.Label(self.container, text="BIBLIOTECA AVALON", font=("Georgia", 40, "bold"), fg=self.cor_principal).pack(pady=10)
        tk.Label(self.container, text="Onde o conhecimento encontra a magia.", font=("Arial", 14, "italic"), fg="#555").pack(pady=5)
        
        texto = ("Bem-vindo ao maior acervo digital de literatura.\n"
                 "Seu portal para compras e aluguéis de livros.")
        tk.Label(self.container, text=texto, font=("Arial", 12), justify="center", pady=30).pack()

        frame_btns = tk.Frame(self.container)
        frame_btns.pack(pady=20)
        tk.Button(frame_btns, text="CRIAR CONTA", bg=self.cor_principal, fg="white", font=("Arial", 12, "bold"), width=20, height=2, command=self.tela_cadastro).pack(side="left", padx=10)
        tk.Button(frame_btns, text="FAZER LOGIN", bg="white", fg=self.cor_principal, font=("Arial", 12, "bold"), width=20, height=2, command=self.tela_login).pack(side="left", padx=10)

    def executar_cadastro(self):
        nome, gmail, senha, end = self.ent_nome.get(), self.ent_gmail.get(), self.ent_senha.get(), self.ent_endereco.get()
        if not (nome and gmail and senha):
            messagebox.showwarning("Aviso", "Preencha os campos obrigatórios!")
            return
        if database_avalon.cadastrar_usuario(nome, gmail, senha, end):
            messagebox.showinfo("Sucesso", "Conta criada! Faça login.")
            self.tela_login()
        else:
            messagebox.showerror("Erro", "Gmail já cadastrado.")

    def executar_login(self):
        usuario = database_avalon.verificar_login(self.ent_login_gmail.get(), self.ent_login_senha.get())
        if usuario:
            self.usuario_logado = {"id": usuario[0], "nome": usuario[1], "gmail": usuario[2], "endereco": usuario[4]}
            self.ir_para_principal()
        else:
            messagebox.showerror("Erro", "Credenciais inválidas.")

    def tela_cadastro(self):
        self.limpar_tela()
        tk.Label(self.container, text="Cadastro Avalon", font=("Arial", 28, "bold"), fg=self.cor_principal).pack(pady=20)
        self.ent_nome = self.criar_campo_central("Nome Completo:")
        self.ent_gmail = self.criar_campo_central("Gmail:")
        self.ent_senha = self.criar_campo_central("Senha:", show="*")
        self.ent_endereco = self.criar_campo_central("Endereço:")
        tk.Button(self.container, text="CADASTRAR", bg=self.cor_principal, fg="white", font=("Arial", 12, "bold"), width=25, height=2, command=self.executar_cadastro).pack(pady=20)
        tk.Button(self.container, text="Voltar", command=self.tela_inicial, relief="flat").pack()

    def tela_login(self):
        self.limpar_tela()
        tk.Label(self.container, text="Login Avalon", font=("Arial", 28, "bold"), fg=self.cor_principal).pack(pady=40)
        self.ent_login_gmail = self.criar_campo_central("Gmail:")
        self.ent_login_senha = self.criar_campo_central("Senha:", show="*")
        tk.Button(self.container, text="ENTRAR", bg=self.cor_principal, fg="white", font=("Arial", 12, "bold"), width=25, height=2, command=self.executar_login).pack(pady=20)
        tk.Button(self.container, text="Criar conta", command=self.tela_cadastro, relief="flat").pack()

    def criar_campo_central(self, label_text, show=None):
        tk.Label(self.container, text=label_text, font=("Arial", 11)).pack(pady=(5, 0))
        entry = tk.Entry(self.container, show=show, font=("Arial", 12), justify="center")
        entry.pack(ipady=5, padx=60, fill="x")
        return entry

    def ir_para_principal(self):
        self.limpar_tela()
        header = tk.Frame(self.container, bg=self.cor_principal, height=80); header.pack(fill="x")
        tk.Label(header, text=f"Olá, {self.usuario_logado['nome'].split()[0]}", fg="white", bg=self.cor_principal).pack(side="left", padx=20)
        
        self.busca_input = tk.Entry(header, font=("Arial", 13))
        self.busca_input.pack(side="left", padx=10, ipady=5, expand=True, fill="x")
        tk.Button(header, text="🔍", command=self.buscar_livros).pack(side="left", padx=5)
        
        self.btn_carrinho = tk.Button(header, text=f"🛒 ({len(self.itens_carrinho)})", bg="#FFD700", command=self.tela_carrinho)
        self.btn_carrinho.pack(side="right", padx=20)

        self.canvas = tk.Canvas(self.container)
        self.scrollable_frame = tk.Frame(self.canvas)
        scrollbar = ttk.Scrollbar(self.container, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((550, 0), window=self.scrollable_frame, anchor="n")
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.buscar_livros("Lançamentos")

    def buscar_livros(self, query=None):
        if not query: query = self.busca_input.get()
        if not query: return
        for w in self.scrollable_frame.winfo_children(): w.destroy()
        
        itens = funcoes_avalon.buscar_livros_na_api(query)
        r, c = 0, 0
        self.imagens_cache = []
        
        for item in itens:
            info = item.get('volumeInfo', {})
            titulo = info.get('title', 'Sem título')[:40]
            autores = ", ".join(info.get('authors', ['Desconhecido']))
            capa_url = info.get('imageLinks', {}).get('thumbnail')
            preco = random.uniform(35, 95)
            
            card = tk.Frame(self.scrollable_frame, bd=1, relief="solid", width=450, height=420); card.grid(row=r, column=c, padx=15, pady=15); card.pack_propagate(False)
            
            if capa_url:
                foto = funcoes_avalon.baixar_imagem(capa_url)
                if foto:
                    lbl_img = tk.Label(card, image=foto); lbl_img.image = foto; lbl_img.pack()
                    self.imagens_cache.append(foto)
            
            tk.Label(card, text=titulo, font=("Arial", 11, "bold"), wraplength=400).pack(pady=5)
            tk.Label(card, text=f"Autor: {autores}", fg="#555").pack()
            tk.Label(card, text=f"Preço Base: R$ {preco:.2f}", fg="green", font=("Arial", 9, "bold")).pack(pady=5)
            
            f_btn = tk.Frame(card); f_btn.pack(side="bottom", pady=10)
            tk.Button(f_btn, text="COMPRAR", bg=self.cor_botao_compra, fg="white", command=lambda t=titulo, p=preco: self.add_ao_carrinho(t, p, "Compra")).pack(side="left", padx=5)
            tk.Button(f_btn, text="ALUGAR", bg=self.cor_botao_aluguel, fg="white", command=lambda t=titulo, p=preco: self.add_ao_carrinho(t, p, "Aluguel")).pack(side="left", padx=5)
            
            c += 1
            if c > 1: c = 0; r += 1

    def add_ao_carrinho(self, t, p, tipo):
        self.itens_carrinho.append({"titulo": t, "preco_base": p, "tipo": tipo, "selecionado": tk.BooleanVar(value=True), "dias_aluguel": tk.IntVar(value=1)})
        self.btn_carrinho.config(text=f"🛒 ({len(self.itens_carrinho)})")
        messagebox.showinfo("Avalon", f"{t} adicionado!")

    def tela_carrinho(self):
        self.limpar_tela()
        header = tk.Frame(self.container, bg=self.cor_principal, height=80); header.pack(fill="x")
        tk.Button(header, text="← Voltar", command=self.ir_para_principal).pack(side="left", padx=20)
        tk.Label(header, text="Meu Carrinho", font=("Arial", 20, "bold"), fg="white", bg=self.cor_principal).pack(side="left")
        
        self.frame_lista = tk.Frame(self.container, padx=50, pady=20); self.frame_lista.pack(fill="both", expand=True)
        self.atualizar_lista_carrinho()

    def atualizar_lista_carrinho(self):
        for w in self.frame_lista.winfo_children(): w.destroy()
        
        itens_selecionados = [i for i in self.itens_carrinho if i["selecionado"].get()]
        total = funcoes_avalon.calcular_valor_total(itens_selecionados)
        
        for idx, item in enumerate(self.itens_carrinho):
            linha = tk.Frame(self.frame_lista, pady=5, bd=1, relief="groove"); linha.pack(fill="x", pady=2)
            tk.Checkbutton(linha, variable=item["selecionado"], command=self.atualizar_lista_carrinho).pack(side="left", padx=10)
            tk.Label(linha, text=item["titulo"][:40], width=40, anchor="w").pack(side="left")
            
            if item["tipo"] == "Aluguel":
                tk.Spinbox(linha, from_=1, to=7, width=3, textvariable=item["dias_aluguel"], command=self.atualizar_lista_carrinho).pack(side="left")
                v = (item["preco_base"] * 0.15) * item["dias_aluguel"].get()
            else:
                tk.Label(linha, text="Compra", width=8).pack(side="left"); v = item["preco_base"]
            
            tk.Label(linha, text=f"R$ {v:.2f}", font=("Arial", 10, "bold"), width=12).pack(side="left")
            tk.Button(linha, text="X", bg="red", fg="white", command=lambda i=idx: [self.itens_carrinho.pop(i), self.tela_carrinho()]).pack(side="right", padx=10)
        
        tk.Label(self.frame_lista, text=f"TOTAL: R$ {total:.2f}", font=("Arial", 14, "bold"), fg=self.cor_principal).pack(pady=20)
        tk.Button(self.frame_lista, text="PROSSEGUIR PARA PAGAMENTO", bg=self.cor_botao_compra, fg="white", font=("Arial", 12, "bold"), command=self.tela_pagamento).pack()

    def tela_pagamento(self):
        self.itens_para_pagar = [i for i in self.itens_carrinho if i["selecionado"].get()]
        if not self.itens_para_pagar: return
        self.limpar_tela()
        header = tk.Frame(self.container, bg=self.cor_principal, height=80); header.pack(fill="x")
        tk.Button(header, text="← Carrinho", command=self.tela_carrinho).pack(side="left", padx=20)
        tk.Label(header, text="Pagamento", font=("Arial", 20, "bold"), fg="white", bg=self.cor_principal).pack(side="left")

        corpo = tk.Frame(self.container, padx=50, pady=20); corpo.pack(fill="both")
        
        resumo = tk.LabelFrame(corpo, text=" Resumo do Pedido ", padx=15, pady=15); resumo.pack(side="left", fill="both", expand=True)
        self.total_final = funcoes_avalon.calcular_valor_total(self.itens_para_pagar)
        
        for i in self.itens_para_pagar:
            v = i["preco_base"] if i["tipo"] == "Compra" else (i["preco_base"]*0.15)*i["dias_aluguel"].get()
            tk.Label(resumo, text=f"• {i['titulo'][:30]}...", anchor="w").pack(fill="x")
            tk.Label(resumo, text=f"  R$ {v:.2f}", fg="gray").pack(anchor="w")
        
        tk.Label(resumo, text=f"\nTOTAL A PAGAR: R$ {self.total_final:.2f}", font=("Arial", 12, "bold")).pack(anchor="w")

        opcoes = tk.LabelFrame(corpo, text=" Método de Pagamento ", padx=15, pady=15); opcoes.pack(side="right", fill="both", expand=True, padx=(20,0))
        self.metodo = tk.StringVar(value="pix")
        tk.Radiobutton(opcoes, text="Pix", variable=self.metodo, value="pix", command=self.atualizar_campos_pagamento).pack(anchor="w")
        tk.Radiobutton(opcoes, text="Boleto", variable=self.metodo, value="boleto", command=self.atualizar_campos_pagamento).pack(anchor="w")
        tk.Radiobutton(opcoes, text="Cartão de Crédito", variable=self.metodo, value="cartao", command=self.atualizar_campos_pagamento).pack(anchor="w")
        
        self.area_campos = tk.Frame(opcoes, pady=15); self.area_campos.pack(fill="both")
        self.atualizar_campos_pagamento()
        
        tk.Button(self.container, text="CONFIRMAR E GERAR NOTA FISCAL", bg=self.cor_botao_compra, fg="white", font=("Arial", 12, "bold"), height=2, command=self.finalizar_venda).pack(side="bottom", pady=30)

    def atualizar_campos_pagamento(self):
        for w in self.area_campos.winfo_children(): w.destroy()
        m = self.metodo.get()
        if m == "pix":
            tk.Label(self.area_campos, text="Chave Pix (E-mail):", font=("Arial", 9, "bold")).pack(anchor="w")
            tk.Entry(self.area_campos, font=("Arial", 10)).insert(0, "pagar@avalon.com")
            self.area_campos.winfo_children()[-1].pack(fill="x")
        elif m == "boleto":
            tk.Label(self.area_campos, text="Código de Barras:", font=("Arial", 9, "bold")).pack(anchor="w")
            tk.Label(self.area_campos, text="34191.09008 63561.760409 07750.190006 8 95610000", wraplength=200, fg="blue").pack()
        elif m == "cartao":
            tk.Label(self.area_campos, text="Número do Cartão:").pack(anchor="w")
            tk.Entry(self.area_campos).pack(fill="x", pady=2)
            tk.Label(self.area_campos, text="Nome no Cartão:").pack(anchor="w")
            tk.Entry(self.area_campos).pack(fill="x", pady=2)
            f2 = tk.Frame(self.area_campos); f2.pack(fill="x")
            tk.Label(f2, text="Validade:").grid(row=0, column=0)
            tk.Entry(f2, width=10).grid(row=0, column=1)
            tk.Label(f2, text=" CVV:").grid(row=0, column=2)
            tk.Entry(f2, width=5).grid(row=0, column=3)

    def finalizar_venda(self):
        funcoes_avalon.salvar_venda_completa(self.usuario_logado["id"], self.itens_para_pagar)
        self.exibir_comprovante_profissional()
        self.itens_carrinho = [i for i in self.itens_carrinho if not i["selecionado"].get()]

    def exibir_comprovante_profissional(self):
        nf = tk.Toplevel(self.root); nf.title("Nota Fiscal Avalon"); nf.geometry("500x650")
        txt = tk.Text(nf, font=("Courier", 10), padx=25, pady=25); txt.pack(fill="both", expand=True)
        
        conteudo = funcoes_avalon.formatar_nota_fiscal(
            self.usuario_logado['nome'], 
            self.itens_para_pagar, 
            self.total_final, 
            self.metodo.get()
        )
        
        txt.insert("1.0", conteudo); txt.config(state="disabled")
        tk.Button(nf, text="FECHAR E IR PARA O INÍCIO", bg=self.cor_botao_compra, fg="white", command=lambda: [nf.destroy(), self.ir_para_principal()]).pack(pady=15)

if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaAvalon(root)
    root.mainloop()
