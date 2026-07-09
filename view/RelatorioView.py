import tkinter as tk
from tkinter import scrolledtext


class RelatorioView:
    def __init__(self, controller):
        self.controller = controller

        self.janela = tk.Toplevel()
        self.janela.title("Relatorios")
        self.janela.geometry("750x500")

        self.criarBotoes()
        self.criarAreaTexto()

    def criarBotoes(self):
        frame = tk.Frame(self.janela)
        frame.pack(pady=10)

        tk.Button(
            frame,
            text="Clinicas com mais atendimentos",
            width=28,
            command=lambda: self.mostrarResultado(
                self.controller.relatorioClinicasComMaisAtendimentos()
            )
        ).grid(row=0, column=0, padx=5, pady=5)

        tk.Button(
            frame,
            text="Atendimentos mais caros/baratos",
            width=28,
            command=lambda: self.mostrarResultado(
                self.controller.relatorioAtendimentosMaisCarosEBaratos()
            )
        ).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(
            frame,
            text="Procedimentos mais realizados",
            width=28,
            command=lambda: self.mostrarResultado(
                self.controller.relatorioProcedimentosMaisRealizados()
            )
        ).grid(row=1, column=0, padx=5, pady=5)

        tk.Button(
            frame,
            text="Procedimentos mais caros/baratos",
            width=28,
            command=lambda: self.mostrarResultado(
                self.controller.relatorioProcedimentosMaisCarosEBaratos()
            )
        ).grid(row=1, column=1, padx=5, pady=5)

    def criarAreaTexto(self):
        self.texto = scrolledtext.ScrolledText(self.janela, width=85, height=22)
        self.texto.pack(padx=10, pady=10, fill="both", expand=True)

    def mostrarResultado(self, resultado):
        self.texto.delete("1.0", tk.END)
        self.texto.insert(tk.END, resultado)