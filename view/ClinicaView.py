import tkinter as tk
from tkinter import ttk, messagebox


class ClinicaView:
    def __init__(self, controller):
        self.controller = controller

        self.janela = tk.Toplevel()
        self.janela.title("Cadastro de Clínicas")
        self.janela.geometry("750x500")

        self.criarFormulario()
        self.criarTabela()
        self.criarBotoes()

    def criarFormulario(self):
        frame = tk.Frame(self.janela)
        frame.pack(pady=10)

        tk.Label(frame, text="Nome").grid(row=0, column=0, padx=5, pady=5)
        self.entry_nome = tk.Entry(frame, width=30)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Cidade").grid(row=1, column=0, padx=5, pady=5)
        self.entry_cidade = tk.Entry(frame, width=30)
        self.entry_cidade.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Descrição").grid(row=2, column=0, padx=5, pady=5)
        self.entry_descricao = tk.Entry(frame, width=30)
        self.entry_descricao.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame, text="Abertura (HH:MM)").grid(row=3, column=0, padx=5, pady=5)
        self.entry_abertura = tk.Entry(frame, width=30)
        self.entry_abertura.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(frame, text="Fechamento (HH:MM)").grid(row=4, column=0, padx=5, pady=5)
        self.entry_fechamento = tk.Entry(frame, width=30)
        self.entry_fechamento.grid(row=4, column=1, padx=5, pady=5)

    def criarTabela(self):
        colunas = ("nome", "cidade", "descricao", "abertura", "fechamento")

        self.tabela = ttk.Treeview(self.janela, columns=colunas, show="headings")
        self.tabela.heading("nome", text="Nome")
        self.tabela.heading("cidade", text="Cidade")
        self.tabela.heading("descricao", text="Descrição")
        self.tabela.heading("abertura", text="Abertura")
        self.tabela.heading("fechamento", text="Fechamento")

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
        return (
            self.entry_nome.get(),
            self.entry_cidade.get(),
            self.entry_descricao.get(),
            self.entry_abertura.get(),
            self.entry_fechamento.get()
        )

    def lerIndiceSelecionado(self):
        selecionado = self.tabela.selection()

        if not selecionado:
            raise ValueError("Selecione uma clínica na tabela.")

        return int(selecionado[0])

    def mostrarLista(self, clinicas):
        for item in self.tabela.get_children():
            self.tabela.delete(item)

        for i, clinica in enumerate(clinicas):
            self.tabela.insert(
                "",
                "end",
                iid=str(i),
                values=(
                    clinica.nome,
                    clinica.cidade,
                    clinica.descricao,
                    clinica.horarioAbertura.strftime("%H:%M"),
                    clinica.horarioFechamento.strftime("%H:%M")
                )
            )

    def preencherCampos(self, event):
        selecionado = self.tabela.selection()

        if not selecionado:
            return

        valores = self.tabela.item(selecionado[0], "values")

        self.limparCampos()
        self.entry_nome.insert(0, valores[0])
        self.entry_cidade.insert(0, valores[1])
        self.entry_descricao.insert(0, valores[2])
        self.entry_abertura.insert(0, valores[3])
        self.entry_fechamento.insert(0, valores[4])

    def limparCampos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_cidade.delete(0, tk.END)
        self.entry_descricao.delete(0, tk.END)
        self.entry_abertura.delete(0, tk.END)
        self.entry_fechamento.delete(0, tk.END)

    def mostrarMensagem(self, mensagem):
        messagebox.showinfo("Mensagem", mensagem)

    def mostrarErro(self, mensagem):
        messagebox.showerror("Erro", mensagem)