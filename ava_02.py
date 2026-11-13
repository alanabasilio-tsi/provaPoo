from abc import ABC, abstractmethod
from dataclasses import dataclass

# Excessões

class AgendaError(Exception):
    def __init__(self, text):
        super().__init__(text)

class HorarioIndisponivelError(AgendaError):
    def __init__(self):
        super().__init__("Este horário esta indisponível no momento !!")

class PacienteJaAgendadoError(AgendaError):
    def __init__(self):
        super().__init__("Este paciente ja foi agendado !!")


@dataclass(frozen=True)
class Paciente():
    nome:str
    cartao_sus:str
    agendado:bool = False

class Atendimento(ABC):
    def __init__(self, paciente: Paciente):
        self.__paciente = paciente

    @property
    def paciente (self):
        return self.__paciente

    @abstractmethod
    def duracao_minutos(self)->int:
        pass
    
    def __str__(self):
        return f'Paciente: {self.paciente.nome} \n Duração: {self.duracao_minutos()}'

class Consulta (Atendimento):
    def __init__(self, paciente: Paciente, especialidade:str, retorno: bool = False):
        super().__init__(paciente)
        self.retorno = retorno
        self.especialidade = especialidade

    def __str__(self):
        return f'Consulta - Especialidade: {self.especialidade} \n {super().__str__()}'

    def duracao_minutos(self)->int:
        if self.retorno == False:
            return 30
        else:
            return 15

class Exame (Atendimento):

    def __init__(self, paciente: Paciente, tipo:str, jejum: bool = False):
        super().__init__(paciente)
        self.tipo = tipo
        self.jejum = jejum

    def duracao_minutos(self)->int:
        if self.jejum == False:
            return 20
        else:
            return 30

    def __str__(self):
            return f'Exame - Tipo: {self.tipo} \n {super().__str__()}'
    
class Vacinacao (Atendimento):

    def __init__(self, paciente: Paciente, vacina:str, doses:int = 1):
        super().__init__(paciente)
        self.vacina = vacina
        self.doses = doses

    def duracao_minutos(self)->int:
        return self.doses * 10

    def __str__(self):
            return f'Vacinacao - Vacina: {self.vacina} \n {super().__str__()}'

class Agenda():
    def __init__(self, limite_minutos:int = 240):
        self.limite_minutos = limite_minutos
        self._lista_de_atendimentos:list[Atendimento] = []

    @property
    def atendimentos(self) -> list[Atendimento]:
        return tuple(self._lista_de_atendimentos)

    @property
    def minutos_ocupados(self) -> int:
        minutos_total:int = 0

        for atendimento in self._lista_de_atendimentos:
            minutos_total += atendimento.duracao_minutos()

        return minutos_total

    def agendar(self, atendimento: Atendimento) -> None:
        try:
            if atendimento.paciente.agendado == False:
                if atendimento.duracao_minutos() <= self.limite_minutos - self.minutos_ocupados:
                    self._lista_de_atendimentos.append(atendimento)
                else:
                    raise HorarioIndisponivelError()
            else:
                raise PacienteJaAgendadoError()
        except Exception as erro:
            print(erro)

agenda = Agenda(limite_minutos=59)

for numero in range(2):                           # 8 x 30 = 240 exatos
    agenda.agendar(Consulta(Paciente(f"P{numero}", str(numero)), "CG"))

print(agenda.minutos_ocupados)