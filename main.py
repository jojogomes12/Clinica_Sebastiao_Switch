import os
from enum import Enum
from enfermeira import Enfermeira,TecnicaEnfermagem
from medicos import Medico, TipoMedico
from Faxineiro import Faxineiro


def cadastrar_enfermeira():
    nome = input("Digite o nome da enfermeira: ")
    cpf = input("Digite o CPF da enfermeira: ")
    salario = float(input("Digite o salário da enfermeira: "))
    especialidade = input("Digite a especialidade da enfermeira: ")
    enfermeira = Enfermeira(nome, cpf, salario, especialidade)
    return enfermeira


def cadastrar_tecnica_enfermagem():
    nome = input("Digite o nome da técnica de enfermagem: ")
    cpf = input("Digite o CPF da técnica de enfermagem: ")
    salario = float(input("Digite o salário da técnica de enfermagem: "))
    turno = input("Digite o turno de trabalho da técnica de enfermagem: ")
    tecnica_enfermagem = TecnicaEnfermagem(nome, cpf, salario, turno)
    return tecnica_enfermagem


def cadastrar_faxineiro():
    nome = input("Digite o nome do faxineiro: ")
    cpf = input("Digite o CPF do enfermeiro: ")
    salario = float(input("Digite o salário do faxineiro: "))
    turno = input("Digite o turno do faxineiro: ")
    faxineiro = Faxineiro(nome, cpf, salario, turno)
    return faxineiro



def cadastrar_medico():
    nome = input("Digite o nome do médico: ")
    cpf = input("Digite o CPF do médico: ")
    salario = float(input("Digite o salário do médico: "))
    print("Tipos de Médico:")
    for tipo in TipoMedico:
        print(f"{tipo.value}. {tipo.name.capitalize()}")
    tipo_str = input("Digite o tipo de médico: ")
    tipo = TipoMedico(int(tipo_str))
    especialidade = input("Digite a especialidade do médico: ")
    medico = Medico(nome, cpf, salario, tipo, especialidade)
    return medico


def listar_funcionarios(funcionarios):
    print("==== Lista de Funcionários ====")
    for funcionario in funcionarios:
        if isinstance(funcionario, Enfermeira):
            print(f"Enfermeira: {funcionario.nome} - Especialidade: {funcionario.especialidade}")
        elif isinstance(funcionario, TecnicaEnfermagem):
            print(f"Técnica de Enfermagem: {funcionario.nome} - Turno: {funcionario.turno}")
        elif isinstance(funcionario, Medico):
            print(f"Médico: {funcionario.nome} - Tipo: {funcionario.tipo.name.capitalize()} - Especialidade: {funcionario.especialidade}")
        elif isinstance(funcionario, Faxineiro):
            print(f"Faxineiro: {funcionario.nome} - Turno: {funcionario.turno}")
    print("================================")



def buscar_funcionario(funcionarios, cpf):
    for funcionario in funcionarios:
        if funcionario.cpf == cpf:
            return funcionario
    return None


def atualizar_funcionario(funcionario):
    if isinstance(funcionario, Enfermeira):
        especialidade = input("Digite a nova especialidade da enfermeira: ")
        funcionario.especialidade = especialidade
    elif isinstance(funcionario, TecnicaEnfermagem):
        turno = input("Digite o novo turno de trabalho da técnica de enfermagem: ")
        funcionario.turno = turno
    
    elif isinstance(funcionario, Faxineiro):
        turno = input("Digite o novo turno de trabalho do faxineiro: ")
        funcionario.turno = turno

    elif isinstance(funcionario, Medico):
        print("1. Alterar Especialidade")
        print("2. Alterar Tipo (Residência ou Terceirizado)")
        opcao = input("Escolha a opção desejada: ")
        
        if opcao == "1":
            especialidade = input("Digite a nova especialidade do médico: ")
            funcionario.especialidade = especialidade
            print("Especialidade do médico atualizada com sucesso!")
        elif opcao == "2":
            print("Tipos de Médico:")
            for tipo in TipoMedico:
                print(f"{tipo.value}. {tipo.name.capitalize()}")
            tipo_str = input("Digite o novo tipo de médico: ")
            tipo = TipoMedico(int(tipo_str))
            funcionario.tipo = tipo
            print("Tipo do médico atualizado com sucesso!")
        else:
            print("Opção inválida!")


# Resto do código...



def excluir_funcionario(funcionarios, funcionario):
    funcionarios.remove(funcionario)


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def exibir_menu():
    print("==== Sistema de Gerenciamento de Funcionários ====")
    print("1. Cadastrar Enfermeira")
    print("2. Cadastrar Técnica de Enfermagem")
    print("3. Cadastrar Médico")
    print("4. Cadastrar Faxineiro")
    print("5. Listar Funcionários")
    print("6. Buscar Funcionário")
    print("7. Atualizar Funcionário")
    print("8. Excluir Funcionário")
    print("0. Sair")
    print("=================================================")


def executar_opcao(opcao, funcionarios):
    if opcao == "1":
        enfermeira = cadastrar_enfermeira()
        funcionarios.append(enfermeira)
        print("Enfermeira cadastrada com sucesso!")
    elif opcao == "2":
        tecnica_enfermagem = cadastrar_tecnica_enfermagem()
        funcionarios.append(tecnica_enfermagem)
        print("Técnica de Enfermagem cadastrada com sucesso!")
    elif opcao == "3":
        medico = cadastrar_medico()
        funcionarios.append(medico)
    elif opcao == "4":
        faxineiro = cadastrar_faxineiro()
        funcionarios.append(faxineiro)    
        print("Faxineiro Cadastrado com Sucesso!")
    elif opcao == "5":
        listar_funcionarios(funcionarios)
    elif opcao == "6":
        cpf = input("Digite o CPF do funcionário a ser buscado: ")
        funcionario = buscar_funcionario(funcionarios, cpf)
        if funcionario:
            if isinstance(funcionario, Enfermeira):
                print(f"Enfermeira encontrada: {funcionario.nome} - Especialidade: {funcionario.especialidade}")
            elif isinstance(funcionario, TecnicaEnfermagem):
                print(f"Técnica de Enfermagem encontrada: {funcionario.nome} - Turno: {funcionario.turno}")

            elif isinstance(funcionario, Faxineiro):
                print(f"Faxineiro: {funcionario.nome} - Turno: {funcionario.turno}") 

            elif isinstance(funcionario, Medico):
                print(f"Médico encontrado: {funcionario.nome} - Tipo: {funcionario.tipo.name.capitalize()} - Especialidade: {funcionario.especialidade}")
        else:
            print("Funcionário não encontrado!")
    elif opcao == "7":
        cpf = input("Digite o CPF do funcionário a ser atualizado: ")
        funcionario = buscar_funcionario(funcionarios, cpf)
        if funcionario:
            atualizar_funcionario(funcionario)
            print("Funcionário atualizado com sucesso!")
        else:
            print("Funcionário não encontrado!")
    elif opcao == "8":
        cpf = input("Digite o CPF do funcionário a ser excluído: ")
        funcionario = buscar_funcionario(funcionarios, cpf)
        if funcionario:
            excluir_funcionario(funcionarios, funcionario)
            print("Funcionário excluído com sucesso!")
        else:
            print("Funcionário não encontrado!")
    elif opcao == "0":
        print("Saindo...")
        return False
    else:
        print("Opção inválida!")

    return True


def main():
    funcionarios = []
    executando = True

    while executando:
        limpar_tela()
        exibir_menu()
        opcao = input("Digite a opção desejada: ")
        limpar_tela()
        executando = executar_opcao(opcao, funcionarios)
        input("Pressione Enter para continuar...")


if __name__ == "__main__":
    main()
