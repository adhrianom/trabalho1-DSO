import tkinter as tk
from tkinter import ttk, messagebox


class AtendimentoView:
    def __init__(self, controller):
        self.controller = controller

        self.janela = tk.Toplevel()
        self.janela.title("Registro de Atendimentos")
        self.janela.geometry("950x550")

        self.criarFormulario()
        self.criarTabela()
        self.criarBotoes()

    def criarFormulario(self):
        frame = tk.Frame(self.janela)
        frame.pack(pady=10)

        tk.Label(frame, text="Clínica").grid(row=0, column=0, padx=5, pady=5)
        self.combo_clinica = ttk.Combobox(frame, width=30, state="readonly")
        self.combo_clinica.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Paciente").grid(row=1, column=0, padx=5, pady=5)
        self.combo_paciente = ttk.Combobox(frame, width=30, state="readonly")
        self.combo_paciente.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Profissional").grid(row=2, column=0, padx=5, pady=5)
        self.combo_profissional = ttk.Combobox(frame, width=30, state="readonly")
        self.combo_profissional.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame, text="Tipo Atendimento").grid(row=3, column=0, padx=5, pady=5)
        self.combo_tipo = ttk.Combobox(frame, width=30, state="readonly")
        self.combo_tipo.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(frame, text="Data (DD/MM/AAAA)").grid(row=0, column=2, padx=5, pady=5)
        self.entry_data = tk.Entry(frame, width=20)
        self.entry_data.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(frame, text="Hora Início (HH:MM)").grid(row=1, column=2, padx=5, pady=5)
        self.entry_hora_inicio = tk.Entry(frame, width=20)
        self.entry_hora_inicio.grid(row=1, column=3, padx=5, pady=5)

        tk.Label(frame, text="Hora Fim (HH:MM)").grid(row=2, column=2, padx=5, pady=5)
        self.entry_hora_fim = tk.Entry(frame, width=20)
        self.entry_hora_fim.grid(row=2, column=3, padx=5, pady=5)

        tk.Label(frame, text="Valor").grid(row=3, column=2, padx=5, pady=5)
        self.entry_valor = tk.Entry(frame, width=20)
        self.entry_valor.grid(row=3, column=3, padx=5, pady=5)

        tk.Label(frame, text="Procedimento").grid(row=4, column=0, padx=5, pady=5)
        self.entry_procedimento = tk.Entry(frame, width=30)
        self.entry_procedimento.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(frame, text="Custo Procedimento").grid(row=4, column=2, padx=5, pady=5)
        self.entry_custo = tk.Entry(frame, width=20)
        self.entry_custo.grid(row=4, column=3, padx=5, pady=5)

    def criarTabela(self):
        colunas = ("clinica", "paciente", "profissional", "tipo", "data", "inicio", "fim", "valor")

        self.tabela = ttk.Treeview(self.janela, columns=colunas, show="headings")
        self.tabela.heading("clinica", text="Clínica")
        self.tabela.heading("paciente", text="Paciente")
        self.tabela.heading("profissional", text="Profissional")
        self.tabela.heading("tipo", text="Tipo")
        self.tabela.heading("data", text="Data")
        self.tabela.heading("inicio", text="Início")
        self.tabela.heading("fim", text="Fim")
        self.tabela.heading("valor", text="Valor")

        self.tabela.pack(pady=10, fill="both", expand=True)
        self.tabela.bind("<<TreeviewSelect>>", self.preencherCampos)

    def criarBotoes(self):
        frame = tk.Frame(self.janela)
        frame.pack(pady=10)

        tk.Button(frame, text="Incluir", width=16, command=self.controller.incluir).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Alterar", width=16, command=self.controller.alterar).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Excluir", width=16, command=self.controller.excluir).grid(row=0, column=2, padx=5)
        tk.Button(frame, text="Adicionar Procedimento", width=20, command=self.controller.adicionarProcedimento).grid(row=0, column=3, padx=5)
        tk.Button(frame, text="Limpar", width=16, command=self.limparCampos).grid(row=0, column=4, padx=5)

    def atualizarCombos(self, clinicas, pacientes, profissionais, tipos):
        self.combo_clinica["values"] = [clinica.nome for clinica in clinicas]
        self.combo_paciente["values"] = [paciente.nome for paciente in pacientes]
        self.combo_profissional["values"] = [profissional.nome for profissional in profissionais]
        self.combo_tipo["values"] = [tipo.descricao for tipo in tipos]

    def lerDados(self):
        return (
            self.combo_clinica.current(),
            self.combo_paciente.current(),
            self.combo_profissional.current(),
            self.combo_tipo.current(),
            self.entry_data.get(),
            self.entry_hora_inicio.get(),
            self.entry_hora_fim.get(),
            self.entry_valor.get()
        )

    def lerDadosProcedimento(self):
        return (
            self.lerIndiceSelecionado(),
            self.entry_procedimento.get(),
            self.entry_custo.get()
        )

    def lerIndiceSelecionado(self):
        selecionado = self.tabela.selection()

        if not selecionado:
            raise ValueError("Selecione um atendimento na tabela.")

        return int(selecionado[0])

    def mostrarLista(self, atendimentos):
        for item in self.tabela.get_children():
            self.tabela.delete(item)

        for i, atendimento in enumerate(atendimentos):
            self.tabela.insert(
                "",
                "end",
                iid=str(i),
                values=(
                    atendimento.clinica.nome,
                    atendimento.paciente.nome,
                    atendimento.profissionalSaude.nome,
                    atendimento.tipoAtendimento.descricao,
                    atendimento.data.strftime("%d/%m/%Y"),
                    atendimento.horaInicio.strftime("%H:%M"),
                    atendimento.horaFim.strftime("%H:%M"),
                    atendimento.valor
                )
            )

    def preencherCampos(self, event):
        selecionado = self.tabela.selection()

        if not selecionado:
            return

        indice = int(selecionado[0])
        atendimento = self.controller.atendimentos[indice]

        self.limparCampos()

        self.combo_clinica.current(self.controller.clinicas.index(atendimento.clinica))
        self.combo_paciente.current(self.controller.pacientes.index(atendimento.paciente))
        self.combo_profissional.current(self.controller.profissionais.index(atendimento.profissionalSaude))
        self.combo_tipo.current(self.controller.tipos_atendimento.index(atendimento.tipoAtendimento))

        self.entry_data.insert(0, atendimento.data.strftime("%d/%m/%Y"))
        self.entry_hora_inicio.insert(0, atendimento.horaInicio.strftime("%H:%M"))
        self.entry_hora_fim.insert(0, atendimento.horaFim.strftime("%H:%M"))
        self.entry_valor.insert(0, str(atendimento.valor))

    def limparCampos(self):
        self.combo_clinica.set("")
        self.combo_paciente.set("")
        self.combo_profissional.set("")
        self.combo_tipo.set("")
        self.entry_data.delete(0, tk.END)
        self.entry_hora_inicio.delete(0, tk.END)
        self.entry_hora_fim.delete(0, tk.END)
        self.entry_valor.delete(0, tk.END)
        self.entry_procedimento.delete(0, tk.END)
        self.entry_custo.delete(0, tk.END)

    def mostrarMensagem(self, mensagem):
        messagebox.showinfo("Mensagem", mensagem)

    def mostrarErro(self, mensagem):
        messagebox.showerror("Erro", mensagem)