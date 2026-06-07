from model.Atendimento import Atendimento
from model.Procedimento import Procedimento
import datetime


class AtendimentoController:
    def __init__(self, atendimentos, clinicas, pacientes, profissionais, tipos_atendimento):
        self.atendimentos = atendimentos
        self.clinicas = clinicas
        self.pacientes = pacientes
        self.profissionais = profissionais
        self.tipos_atendimento = tipos_atendimento

    def incluir(self):
        if len(self.clinicas) == 0 or len(self.pacientes) == 0 or len(self.profissionais) == 0 or len(self.tipos_atendimento) == 0:
            print("É preciso ter clínica, paciente, profissional e tipo de atendimento cadastrados.")
            return

        try:
            print("\nClínicas:")
            for i in range(len(self.clinicas)):
                print(i, "-", self.clinicas[i].nome, " (Abertura:", self.clinicas[i].horarioAbertura, "- Fechamento:", self.clinicas[i].horarioFechamento, ")")
            indice_clinica = int(input("Escolha a clínica: "))
            clinica = self.clinicas[indice_clinica]

            print("\nPacientes:")
            for i in range(len(self.pacientes)):
                print(i, "-", self.pacientes[i].nome)
            indice_paciente = int(input("Escolha o paciente: "))
            paciente = self.pacientes[indice_paciente]

            print("\nProfissionais de Saúde:")
            for i in range(len(self.profissionais)):
                print(i, "-", self.profissionais[i].nome)
            indice_profissional = int(input("Escolha o profissional de saúde: "))
            profissional_saude = self.profissionais[indice_profissional]

            print("\nTipos de Atendimento:")
            for i in range(len(self.tipos_atendimento)):
                print(i, "-", self.tipos_atendimento[i].descricao)
            indice_tipo = int(input("Escolha o tipo de atendimento: "))
            tipo_atendimento = self.tipos_atendimento[indice_tipo]

            data = input("Data (dd/mm/yyyy): ")
            data = datetime.datetime.strptime(data, "%d/%m/%Y").date()

            idade = data.year - paciente.dataNascimento.year
            if (data.month, data.day) < (paciente.dataNascimento.month, paciente.dataNascimento.day):
                idade -= 1

            if idade <= 18:
                raise ValueError("O paciente deve ter mais de 18 anos para realizar atendimento de forma independente.")

            hora_inicio = input("Hora de início (hh:mm): ")
            hora_inicio = datetime.datetime.strptime(hora_inicio, "%H:%M").time()

            hora_fim = input("Hora de fim (hh:mm): ")
            hora_fim = datetime.datetime.strptime(hora_fim, "%H:%M").time()

            if hora_inicio >= hora_fim:
                raise ValueError(f"A hora de início deve ser menor que a hora de fim.")

            if hora_inicio < clinica.horarioAbertura or hora_fim > clinica.horarioFechamento:
                raise ValueError(f"O atendimento deve estar dentro do horário de funcionamento da clínica.\nAbertura: {clinica.horarioAbertura} - Fechamento: {clinica.horarioFechamento}")

            valor = float(input("Valor: "))

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

            print("Atendimento cadastrado com sucesso.")
        except (ValueError, IndexError) as e:
            print("Erro ao cadastrar atendimento:", e)

    def listar(self):
        if len(self.atendimentos) == 0:
            print("Nenhum atendimento cadastrado.")
            return

        print("\nLista de atendimentos:")
        for i in range(len(self.atendimentos)):
            atendimento = self.atendimentos[i]
            print(
                i, "-",
                atendimento.clinica.nome, "|",
                atendimento.paciente.nome, "|",
                atendimento.profissionalSaude.nome, "|",
                atendimento.tipoAtendimento.descricao, "|",
                atendimento.data, "|",
                atendimento.horaInicio, "|",
                atendimento.horaFim, "|",
                atendimento.valor
            )

    def alterar(self):
        if len(self.atendimentos) == 0:
            print("Nenhum atendimento cadastrado.")
            return

        self.listar()

        try:
            indice = int(input("Digite o índice do atendimento que deseja alterar: "))
            atendimento = self.atendimentos[indice]

            print("\nClínicas:")
            for i in range(len(self.clinicas)):
                print(i, "-", self.clinicas[i].nome, " (Abertura:", self.clinicas[i].horarioAbertura, "- Fechamento:", self.clinicas[i].horarioFechamento, ")")
            indice_clinica = int(input("Escolha a clínica: "))
            clinica = self.clinicas[indice_clinica]

            print("\nPacientes:")
            for i in range(len(self.pacientes)):
                print(i, "-", self.pacientes[i].nome)
            indice_paciente = int(input("Escolha o paciente: "))
            paciente = self.pacientes[indice_paciente]

            print("\nProfissionais de Saúde:")
            for i in range(len(self.profissionais)):
                print(i, "-", self.profissionais[i].nome)
            indice_profissional = int(input("Escolha o profissional de saúde: "))
            profissional_saude = self.profissionais[indice_profissional]

            print("\nTipos de Atendimento:")
            for i in range(len(self.tipos_atendimento)):
                print(i, "-", self.tipos_atendimento[i].descricao)
            indice_tipo = int(input("Escolha o tipo de atendimento: "))
            tipo_atendimento = self.tipos_atendimento[indice_tipo]

            data = input("Nova data (dd/mm/yyyy): ")
            data = datetime.datetime.strptime(data, "%d/%m/%Y").date()

            idade = data.year - paciente.dataNascimento.year
            if (data.month, data.day) < (paciente.dataNascimento.month, paciente.dataNascimento.day):
                idade -= 1

            if idade <= 18:
                raise ValueError("O paciente deve ter mais de 18 anos para realizar atendimento de forma independente.")

            hora_inicio = input("Nova hora de início (hh:mm): ")
            hora_inicio = datetime.datetime.strptime(hora_inicio, "%H:%M").time()

            hora_fim = input("Nova hora de fim (hh:mm): ")
            hora_fim = datetime.datetime.strptime(hora_fim, "%H:%M").time()

            if hora_inicio >= hora_fim:
                raise ValueError("A hora de início deve ser menor que a hora de fim.")

            if hora_inicio < clinica.horarioAbertura or hora_fim > clinica.horarioFechamento:
                raise ValueError("O atendimento deve estar dentro do horário de funcionamento da clínica.")

            valor = float(input("Novo valor: "))

            atendimento.clinica = clinica
            atendimento.paciente = paciente
            atendimento.profissionalSaude = profissional_saude
            atendimento.tipoAtendimento = tipo_atendimento
            atendimento.data = data
            atendimento.horaInicio = hora_inicio
            atendimento.horaFim = hora_fim
            atendimento.valor = valor

            print("Atendimento alterado com sucesso.")
        except (ValueError, IndexError) as e:
            print("Erro ao alterar atendimento:", e)

    def excluir(self):
        if len(self.atendimentos) == 0:
            print("Nenhum atendimento cadastrado.")
            return

        self.listar()

        try:
            indice = int(input("Digite o índice do atendimento que deseja excluir: "))
            removido = self.atendimentos.pop(indice)
            print("Atendimento excluído com sucesso:", removido.clinica.nome, "-", removido.paciente.nome)
        except (ValueError, IndexError) as e:
            print("Erro ao excluir atendimento:", e)

    def adicionarProcedimento(self):
        if len(self.atendimentos) == 0:
            print("Nenhum atendimento cadastrado.")
            return

        self.listar()

        try:
            indice_atendimento = int(input("Escolha o atendimento: "))
            atendimento = self.atendimentos[indice_atendimento]

            descricao = input("Descricao do procedimento: ")
            custo = float(input("Custo do procedimento: "))

            procedimento = Procedimento(descricao, custo)

            atendimento.procedimentos.append(procedimento)

            print("Procedimento adicionado com sucesso.")
        except (ValueError, IndexError) as e:
            print("Erro ao adicionar procedimento:", e)