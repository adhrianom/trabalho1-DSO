import tkinter as tk
from tkinter import ttk, messagebox


class PagamentoView:
    def __init__(self, controller):
        self.controller = controller

        self.janela = tk.Toplevel()
        self.janela.title("Registro de Pagamentos")
        self.janela.geometry("850x550")

        self.criarFormulario()
        self.criarTabela()
        self.criarBotoes()

    def criarFormulario(self):
        self.frame_formulario = tk.Frame(self.janela)
        self.frame_formulario.pack(pady=10)

        tk.Label(self.frame_formulario, text="Atendimento").grid(row=0, column=0, padx=5, pady=5)
        self.combo_atendimento = ttk.Combobox(self.frame_formulario, width=45, state="readonly")
        self.combo_atendimento.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_formulario, text="Data Pagamento (DD/MM/AAAA)").grid(row=1, column=0, padx=5, pady=5)
        self.entry_data = tk.Entry(self.frame_formulario, width=30)
        self.entry_data.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.frame_formulario, text="Valor Pago").grid(row=2, column=0, padx=5, pady=5)
        self.entry_valor = tk.Entry(self.frame_formulario, width=30)
        self.entry_valor.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.frame_formulario, text="Tipo").grid(row=3, column=0, padx=5, pady=5)
        self.combo_tipo = ttk.Combobox(
            self.frame_formulario,
            width=30,
            state="readonly",
            values=("Dinheiro", "PIX", "Cartão de Crédito")
        )
        self.combo_tipo.grid(row=3, column=1, padx=5, pady=5)
        self.combo_tipo.bind("<<ComboboxSelected>>", self.atualizarCamposTipo)

        self.label_cpf_pagador = tk.Label(self.frame_formulario, text="CPF Pagador (PIX)")
        self.entry_cpf_pagador = tk.Entry(self.frame_formulario, width=30)

        self.label_numero_cartao = tk.Label(self.frame_formulario, text="Número Cartão")
        self.entry_numero_cartao = tk.Entry(self.frame_formulario, width=30)

        self.label_bandeira = tk.Label(self.frame_formulario, text="Bandeira")
        self.entry_bandeira = tk.Entry(self.frame_formulario, width=30)

    def atualizarCamposTipo(self, event=None):
        self.label_cpf_pagador.grid_forget()
        self.entry_cpf_pagador.grid_forget()
        self.label_numero_cartao.grid_forget()
        self.entry_numero_cartao.grid_forget()
        self.label_bandeira.grid_forget()
        self.entry_bandeira.grid_forget()

        tipo = self.combo_tipo.get()

        if tipo == "PIX":
            self.label_cpf_pagador.grid(row=4, column=0, padx=5, pady=5)
            self.entry_cpf_pagador.grid(row=4, column=1, padx=5, pady=5)

        elif tipo == "Cartão de Crédito":
            self.label_numero_cartao.grid(row=4, column=0, padx=5, pady=5)
            self.entry_numero_cartao.grid(row=4, column=1, padx=5, pady=5)

            self.label_bandeira.grid(row=5, column=0, padx=5, pady=5)
            self.entry_bandeira.grid(row=5, column=1, padx=5, pady=5)

    def criarTabela(self):
        colunas = ("data", "valor", "tipo")

        self.tabela = ttk.Treeview(self.janela, columns=colunas, show="headings")
        self.tabela.heading("data", text="Data")
        self.tabela.heading("valor", text="Valor")
        self.tabela.heading("tipo", text="Tipo")

        self.tabela.pack(pady=10, fill="both", expand=True)
        self.tabela.bind("<<TreeviewSelect>>", self.preencherCampos)

    def criarBotoes(self):
        frame_botoes = tk.Frame(self.janela)
        frame_botoes.pack(pady=10)

        tk.Button(
            frame_botoes,
            text="Incluir",
            width=12,
            command=self.controller.incluir
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            frame_botoes,
            text="Alterar",
            width=12,
            command=self.controller.alterar
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            frame_botoes,
            text="Excluir",
            width=12,
            command=self.controller.excluir
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            frame_botoes,
            text="Limpar",
            width=12,
            command=self.limparCampos
        ).grid(row=0, column=3, padx=5)

    def atualizarCombos(self, atendimentos):
        valores = []

        for atendimento in atendimentos:
            valores.append(
                f"{atendimento.paciente.nome} - {atendimento.data.strftime('%d/%m/%Y')} - R$ {atendimento.valor}"
            )

        self.combo_atendimento["values"] = valores

    def lerDados(self):
        return (
            self.combo_atendimento.current(),
            self.entry_data.get(),
            self.entry_valor.get(),
            self.combo_tipo.get(),
            self.entry_cpf_pagador.get(),
            self.entry_numero_cartao.get(),
            self.entry_bandeira.get()
        )

    def lerIndiceSelecionado(self):
        selecionado = self.tabela.selection()

        if not selecionado:
            raise ValueError("Selecione um pagamento na tabela.")

        return int(selecionado[0])

    def mostrarLista(self, pagamentos):
        for item in self.tabela.get_children():
            self.tabela.delete(item)

        for i, pagamento in enumerate(pagamentos):
            self.tabela.insert(
                "",
                "end",
                iid=str(i),
                values=(
                    pagamento.data.strftime("%d/%m/%Y"),
                    pagamento.valorPago,
                    pagamento.__class__.__name__
                )
            )

    def preencherCampos(self, event):
        selecionado = self.tabela.selection()

        if not selecionado:
            return

        indice = int(selecionado[0])
        pagamento = self.controller.pagamentos[indice]

        self.limparCampos()

        self.entry_data.insert(0, pagamento.data.strftime("%d/%m/%Y"))
        self.entry_valor.insert(0, str(pagamento.valorPago))

        if pagamento.__class__.__name__ == "PagamentoDinheiro":
            self.combo_tipo.set("Dinheiro")

        elif pagamento.__class__.__name__ == "PagamentoPix":
            self.combo_tipo.set("PIX")
            self.atualizarCamposTipo()
            self.entry_cpf_pagador.insert(0, pagamento.cpfPagador)

        elif pagamento.__class__.__name__ == "PagamentoCartaoCredito":
            self.combo_tipo.set("Cartão de Crédito")
            self.atualizarCamposTipo()
            self.entry_numero_cartao.insert(0, pagamento.numeroCartao)
            self.entry_bandeira.insert(0, pagamento.bandeira)

        self.atualizarCamposTipo()

    def limparCampos(self):
        self.combo_atendimento.set("")
        self.entry_data.delete(0, tk.END)
        self.entry_valor.delete(0, tk.END)
        self.combo_tipo.set("")

        self.entry_cpf_pagador.delete(0, tk.END)
        self.entry_numero_cartao.delete(0, tk.END)
        self.entry_bandeira.delete(0, tk.END)

        self.atualizarCamposTipo()

    def mostrarMensagem(self, mensagem):
        messagebox.showinfo("Mensagem", mensagem)

    def mostrarErro(self, mensagem):
        messagebox.showerror("Erro", mensagem)