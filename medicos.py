from enum import Enum
from Funcionario import Funcionario


class TipoMedico(Enum):
    RESIDENTE = 1
    TERCEIRIZADO = 2

class Medico(Funcionario):
    def __init__(self, nome, cpf, salario, tipo, especialidade):
        super().__init__(nome, cpf, salario)
        self.tipo = tipo
        self.especialidade = especialidade
