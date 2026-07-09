from model.Atendimento import Atendimento
from model.Procedimento import Procedimento
from view.AtendimentoView import AtendimentoView
from dao.AtendimentoDAO import AtendimentoDAO
import datetime


class AtendimentoController:
    def __init__(self, atendimentos, clinicas, pacientes, profissionais, tipos_atendimento):
        self.dao = AtendimentoDAO()
        self.atendimentos = self.dao.carregar()
        self.clinicas = clinicas
        self.pacientes = pacientes
        self.profissionais = profissionais
        self.tipos_atendimento = tipos_atendimento
        self.view = None

    def abrirTela(self):
        self.view = AtendimentoView(self)
        self.view.atualizarCombos(
            self.clinicas,
            self.pacientes,
            self.profissionais,
            self.tipos_atendimento
        )
        self.listar()

    def incluir(self):
        if len(self.clinicas) == 0 or len(self.pacientes) == 0 or len(self.profissionais) == 0 or len(self.tipos_atendimento) == 0:
            self.view.mostrarErro("É preciso ter clínica, paciente, profissional e tipo de atendimento cadastrados.")
            return

        try:
            indice_clinica, indice_paciente, indice_profissional, indice_tipo, data_str, hora_inicio_str, hora_fim_str, valor_str = self.view.lerDados()

            if indice_clinica < 0 or indice_paciente < 0 or indice_profissional < 0 or indice_tipo < 0:
                raise ValueError("Selecione clínica, paciente, profissional e tipo de atendimento.")

            clinica = self.clinicas[indice_clinica]
            paciente = self.pacientes[indice_paciente]
            profissional_saude = self.profissionais[indice_profissional]
            tipo_atendimento = self.tipos_atendimento[indice_tipo]

            data = datetime.datetime.strptime(data_str, "%d/%m/%Y").date()

            idade = data.year - paciente.dataNascimento.year
            if (data.month, data.day) < (paciente.dataNascimento.month, paciente.dataNascimento.day):
                idade -= 1

            if idade <= 18:
                raise ValueError("O paciente deve ter mais de 18 anos para realizar atendimento de forma independente.")

            hora_inicio = datetime.datetime.strptime(hora_inicio_str, "%H:%M").time()
            hora_fim = datetime.datetime.strptime(hora_fim_str, "%H:%M").time()

            if hora_inicio >= hora_fim:
                raise ValueError("A hora de início deve ser menor que a hora de fim.")

            if hora_inicio < clinica.horarioAbertura or hora_fim > clinica.horarioFechamento:
                raise ValueError("O atendimento deve estar dentro do horário de funcionamento da clínica.")

            valor = float(valor_str)

            atendimento = Atendimento(
                clinica,
                paciente,
                profissional_saude,
                tipo_atendimento,
                data,
                hora_inicio,
                hora_fim,
                valor
            )

            self.atendimentos.append(atendimento)
            self.dao.salvar(self.atendimentos)

            self.view.mostrarMensagem("Atendimento cadastrado com sucesso.")
            self.view.limparCampos()
            self.listar()
        except (ValueError, IndexError) as e:
            self.view.mostrarErro(f"Erro ao cadastrar atendimento: {e}")

    def listar(self):
        if self.view is not None:
            self.view.mostrarLista(self.atendimentos)

    def alterar(self):
        try:
            indice = self.view.lerIndiceSelecionado()
            atendimento = self.atendimentos[indice]

            indice_clinica, indice_paciente, indice_profissional, indice_tipo, data_str, hora_inicio_str, hora_fim_str, valor_str = self.view.lerDados()

            if indice_clinica < 0 or indice_paciente < 0 or indice_profissional < 0 or indice_tipo < 0:
                raise ValueError("Selecione clínica, paciente, profissional e tipo de atendimento.")

            clinica = self.clinicas[indice_clinica]
            paciente = self.pacientes[indice_paciente]
            profissional_saude = self.profissionais[indice_profissional]
            tipo_atendimento = self.tipos_atendimento[indice_tipo]

            data = datetime.datetime.strptime(data_str, "%d/%m/%Y").date()

            idade = data.year - paciente.dataNascimento.year
            if (data.month, data.day) < (paciente.dataNascimento.month, paciente.dataNascimento.day):
                idade -= 1

            if idade <= 18:
                raise ValueError("O paciente deve ter mais de 18 anos para realizar atendimento de forma independente.")

            hora_inicio = datetime.datetime.strptime(hora_inicio_str, "%H:%M").time()
            hora_fim = datetime.datetime.strptime(hora_fim_str, "%H:%M").time()

            if hora_inicio >= hora_fim:
                raise ValueError("A hora de início deve ser menor que a hora de fim.")

            if hora_inicio < clinica.horarioAbertura or hora_fim > clinica.horarioFechamento:
                raise ValueError("O atendimento deve estar dentro do horário de funcionamento da clínica.")

            valor = float(valor_str)

            atendimento.clinica = clinica
            atendimento.paciente = paciente
            atendimento.profissionalSaude = profissional_saude
            atendimento.tipoAtendimento = tipo_atendimento
            atendimento.data = data
            atendimento.horaInicio = hora_inicio
            atendimento.horaFim = hora_fim
            atendimento.valor = valor

            self.dao.salvar(self.atendimentos)

            self.view.mostrarMensagem("Atendimento alterado com sucesso.")
            self.view.limparCampos()
            self.listar()
        except (ValueError, IndexError) as e:
            self.view.mostrarErro(f"Erro ao alterar atendimento: {e}")

    def excluir(self):
        try:
            indice = self.view.lerIndiceSelecionado()
            atendimento = self.atendimentos.pop(indice)

            self.dao.salvar(self.atendimentos)

            self.view.mostrarMensagem(f"Atendimento excluído com sucesso: {atendimento.paciente.nome}")
            self.view.limparCampos()
            self.listar()
        except (ValueError, IndexError) as e:
            self.view.mostrarErro(f"Erro ao excluir atendimento: {e}")

    def adicionarProcedimento(self):
        try:
            indice_atendimento, descricao, custo_str = self.view.lerDadosProcedimento()
            atendimento = self.atendimentos[indice_atendimento]

            custo = float(custo_str)
            procedimento = Procedimento(descricao, custo)

            if not hasattr(atendimento, "procedimentos"):
                atendimento.procedimentos = []

            atendimento.procedimentos.append(procedimento)
            self.dao.salvar(self.atendimentos)

            self.view.mostrarMensagem("Procedimento adicionado com sucesso.")
            self.view.limparCampos()
            self.listar()
        except (ValueError, IndexError) as e:
            self.view.mostrarErro(f"Erro ao adicionar procedimento: {e}")