import tkinter as tk
from tkinter import ttk, messagebox


class PacienteView:
    def __init__(self, controller):
        self.controller = controller

        self.janela = tk.Toplevel()
        self.janela.title("Cadastro de Pacientes")
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

        tk.Label(frame, text="Celular").grid(row=1, column=0, padx=5, pady=5)
        self.entry_celular = tk.Entry(frame, width=30)
        self.entry_celular.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="CPF").grid(row=2, column=0, padx=5, pady=5)
        self.entry_cpf = tk.Entry(frame, width=30)
        self.entry_cpf.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame, text="Data Nascimento (DD/MM/AAAA)").grid(row=3, column=0, padx=5, pady=5)
        self.entry_data_nascimento = tk.Entry(frame, width=30)
        self.entry_data_nascimento.grid(row=3, column=1, padx=5, pady=5)

    def criarTabela(self):
        colunas = ("nome", "celular", "cpf", "data_nascimento")

        self.tabela = ttk.Treeview(self.janela, columns=colunas, show="headings")
        self.tabela.heading("nome", text="Nome")
        self.tabela.heading("celular", text="Celular")
        self.tabela.heading("cpf", text="CPF")
        self.tabela.heading("data_nascimento", text="Data Nascimento")

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
            self.entry_celular.get(),
            self.entry_cpf.get(),
            self.entry_data_nascimento.get()
        )

    def lerIndiceSelecionado(self):
        selecionado = self.tabela.selection()

        if not selecionado:
            raise ValueError("Selecione um paciente na tabela.")

        return int(selecionado[0])

    def mostrarLista(self, pacientes):
        for item in self.tabela.get_children():
            self.tabela.delete(item)

        for i, paciente in enumerate(pacientes):
            self.tabela.insert(
                "",
                "end",
                iid=str(i),
                values=(
                    paciente.nome,
                    paciente.celular,
                    paciente.cpf,
                    paciente.dataNascimento.strftime("%d/%m/%Y")
                )
            )

    def preencherCampos(self, event):
        selecionado = self.tabela.selection()

        if not selecionado:
            return

        valores = self.tabela.item(selecionado[0], "values")

        self.limparCampos()
        self.entry_nome.insert(0, valores[0])
        self.entry_celular.insert(0, valores[1])
        self.entry_cpf.insert(0, valores[2])
        self.entry_data_nascimento.insert(0, valores[3])

    def limparCampos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_celular.delete(0, tk.END)
        self.entry_cpf.delete(0, tk.END)
        self.entry_data_nascimento.delete(0, tk.END)

    def mostrarMensagem(self, mensagem):
        messagebox.showinfo("Mensagem", mensagem)

    def mostrarErro(self, mensagem):
        messagebox.showerror("Erro", mensagem)