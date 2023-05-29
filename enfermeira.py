from Funcionario import Funcionario

class Enfermeira(Funcionario):
    def __init__(self, nome, cpf, salario, especialidade):
        super().__init__(nome, cpf, salario)
        self.especialidade = especialidade

class TecnicaEnfermagem(Funcionario):
    def __init__(self, nome, cpf, salario, turno):
        super().__init__(nome, cpf, salario)
        self.turno = turno
