from abc import ABC, abstractmethod
from dataclasses import dataclass

# Excessões

class AgendaError(Exception):
    def __init__(self, text):
        super().__init__(text)

class HorarioIndisponivelError(AgendaError):
    def __init__(self, minutos_restantes, duracao):
        super().__init__(f"Este atendimento tem duração de {duracao} minutos, mas só {minutos_restantes} minutos estão disponíveis no momento !!")

class PacienteJaAgendadoError(AgendaError):
    def __init__(self, paciente):
        super().__init__(f"O paciente que se chama {paciente.nome} ja está agendado !!")


@dataclass(frozen=True)
class Paciente():
    nome:str
    cartao_sus:str

    def agendar_true(self):
        self.agendado = True

class Atendimento(ABC):
    def __init__(self, paciente: Paciente):
        self.paciente = paciente

    @abstractmethod
    def duracao_minutos(self)->int:
        pass
    
    def __str__(self):
        pass
        #return f'Paciente: {self.paciente.nome} \n Duração: {self.duracao_minutos()}'

class Consulta (Atendimento):
    def __init__(self, paciente: Paciente, especialidade:str, retorno: bool = False):
        super().__init__(paciente)
        self.retorno = retorno
        self.especialidade = especialidade

    def __str__(self):
        return f'Especialidade: {self.especialidade} \n Paciente: {self.paciente.nome} \n Duração: {self.duracao_minutos()}'

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
            return f'Tipo: {self.tipo} \n Paciente: {self.paciente.nome} \n Duração: {self.duracao_minutos()}'
    
class Vacinacao (Atendimento):

    def __init__(self, paciente: Paciente, vacina:str, doses:int = 1):
        super().__init__(paciente)
        self.vacina = vacina
        self.doses = doses

    def duracao_minutos(self)->int:
        return self.doses * 10

    def __str__(self):
            return f'Vacina: {self.vacina} \n Paciente: {self.paciente.nome} \n Duração: {self.duracao_minutos()}'

class Agenda():
    def __init__(self, limite_minutos:int = 240):
        self.limite_minutos = limite_minutos
        self._atendimentos:list[Atendimento] = []

    @property
    def atendimentos(self) -> list[Atendimento]:
        return tuple(self._atendimentos)

    @property
    def minutos_ocupados(self) -> int:
        minutos_total:int = 0

        for atendimento in self._atendimentos:
            minutos_total += atendimento.duracao_minutos()

        return minutos_total

    def agendar(self, atendimento: Atendimento) -> None:
        agendado:bool = False
        minutos_restantes: int = self.limite_minutos - self.minutos_ocupados

        for atendimento_lista in self._atendimentos:
            if atendimento.paciente == atendimento_lista.paciente:
                agendado = True
                break

        if agendado == False:
            if atendimento.duracao_minutos() <= minutos_restantes:
                self._atendimentos.append(atendimento)
            else:
                raise HorarioIndisponivelError(minutos_restantes, atendimento.duracao_minutos())
        else:
            raise PacienteJaAgendadoError(atendimento.paciente)

# try:
#     agenda = Agenda(limite_minutos=59)
#     p1 = Paciente("Gabriel", "2KH123B")
#     agenda.agendar(Exame(p1,"Dengue"))
#     agenda.agendar(Consulta(p1,"Zika"))
#     print(agenda.atendimentos)
#     print(agenda.minutos_ocupados)
# except Exception as error:
#     print(error)