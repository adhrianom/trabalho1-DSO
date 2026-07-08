import tkinter as tk
from tkinter import messagebox


class SistemaView:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Sistema de Atendimento em Clínicas")
        self.janela.geometry("400x400")

    def iniciar(self):
        self.janela.mainloop()

    def configurarController(self, controller):
        self.controller = controller

    def mostrarMenuPrincipal(self):
        titulo = tk.Label(
            self.janela,
            text="Sistema de Atendimento em Clínicas",
            font=("Arial", 14, "bold")
        )
        titulo.pack(pady=20)

        btn_clinicas = tk.Button(
            self.janela,
            text="Clínicas",
            width=25,
            command=self.controller.menuClinicas
        )
        btn_clinicas.pack(pady=5)

        btn_pacientes = tk.Button(
            self.janela,
            text="Pacientes",
            width=25,
            command=self.controller.menuPacientes
        )
        btn_pacientes.pack(pady=5)

        btn_profissionais = tk.Button(
            self.janela,
            text="Profissionais de Saúde",
            width=25,
            command=self.controller.menuProfissionalSaude
        )
        btn_profissionais.pack(pady=5)

        btn_tipos = tk.Button(
            self.janela,
            text="Tipos de Atendimento",
            width=25,
            command=self.controller.menuTipoAtendimento
        )
        btn_tipos.pack(pady=5)

        btn_atendimentos = tk.Button(
            self.janela,
            text="Atendimentos",
            width=25,
            command=self.controller.menuAtendimento
        )
        btn_atendimentos.pack(pady=5)

        btn_pagamentos = tk.Button(
            self.janela,
            text="Pagamentos",
            width=25,
            command=self.controller.menuPagamentos
        )
        btn_pagamentos.pack(pady=5)

        btn_relatorios = tk.Button(
            self.janela,
            text="Relatórios",
            width=25,
            command=self.controller.abrirMenuRelatorios
        )
        btn_relatorios.pack(pady=5)

        btn_sair = tk.Button(
            self.janela,
            text="Sair",
            width=25,
            command=self.janela.destroy
        )
        btn_sair.pack(pady=20)

    def mostrarMensagem(self, mensagem):
        messagebox.showinfo("Mensagem", mensagem)