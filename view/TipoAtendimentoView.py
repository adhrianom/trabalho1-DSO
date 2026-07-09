import tkinter as tk
from tkinter import ttk, messagebox


class TipoAtendimentoView:
    def __init__(self, controller):
        self.controller = controller

        self.janela = tk.Toplevel()
        self.janela.title("Cadastro de Tipos de Atendimento")
        self.janela.geometry("600x400")

        self.criarFormulario()
        self.criarTabela()
        self.criarBotoes()

    def criarFormulario(self):
        frame = tk.Frame(self.janela)
        frame.pack(pady=10)

        tk.Label(frame, text="Descrição").grid(row=0, column=0, padx=5, pady=5)
        self.entry_descricao = tk.Entry(frame, width=40)
        self.entry_descricao.grid(row=0, column=1, padx=5, pady=5)

    def criarTabela(self):
        colunas = ("descricao",)

        self.tabela = ttk.Treeview(self.janela, columns=colunas, show="headings")
        self.tabela.heading("descricao", text="Descrição")

        self.tabela.pack(pady=10, fill="both", expand=True)
        self.tabela.bind("<<TreeviewSelect>>", self.preencherCampos)

    def criarBotoes(self):
        frame = tk.Frame(self.janela)
        frame.pack(pady=10)

        tk.Button(frame, text="Incluir", width=12, command=self.controller.incluir).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Alterar", width=12, command=self.controller.alterar).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Excluir", width=12, command=self.controller.excluir).grid(row=0, column=2, padx=5)
        tk.Button(frame, text="Limpar", width=12, command=self.limparCampos).grid(row=0, column=3, padx=5)

    def lerDados(self):
        return self.entry_descricao.get()

    def lerIndiceSelecionado(self):
        selecionado = self.tabela.selection()

        if not selecionado:
            raise ValueError("Selecione um tipo de atendimento na tabela.")

        return int(selecionado[0])

    def mostrarLista(self, tipos):
        for item in self.tabela.get_children():
            self.tabela.delete(item)

        for i, tipo in enumerate(tipos):
            self.tabela.insert(
                "",
                "end",
                iid=str(i),
                values=(tipo.descricao,)
            )

    def preencherCampos(self, event):
        selecionado = self.tabela.selection()

        if not selecionado:
            return

        valores = self.tabela.item(selecionado[0], "values")

        self.limparCampos()
        self.entry_descricao.insert(0, valores[0])

    def limparCampos(self):
        self.entry_descricao.delete(0, tk.END)

    def mostrarMensagem(self, mensagem):
        messagebox.showinfo("Mensagem", mensagem)

    def mostrarErro(self, mensagem):
        messagebox.showerror("Erro", mensagem)