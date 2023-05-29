from enum import Enum
from Funcionario import Funcionario


class Faxineiro(Funcionario):
    def __init__(self, nome, cpf, salario, turno):
        super().__init__(nome, cpf, salario)
        self.turno = turno