import time
from gerencia_sql import Gerenciamento
from datetime import datetime
from datetime import date
import os

class Pessoa:

    # Método construtor
    def __init__(self, conexao):
        self.gerencia = Gerenciamento(conexao)
        
    def limpar_tela():
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')

    # Método para imprimir informações da pessoa
    def inserir_pessoa(self):

        data_nascimento = [None, None, None]
        resultados = 'INVALID'

        print("Insira o CPF:")
        cpf = self.input_numerica()
        validacao = self.verifica_cpf(cpf)
        if validacao == False:             #cpf é invalido
            print("\nCPF inválido! Retornando ao menu...\n")
            time.sleep(3)
            return -1
                    
        consulta_sql = f"SELECT * FROM Pessoa WHERE cpf = {cpf}"
        retorno = self.gerencia.acessa_banco(consulta_sql)
        
        verifica_cadastro_ativo = f"SELECT cadastro_ativo FROM Pessoa WHERE cpf = {cpf}"
        cadastro_ativo = self.gerencia.acessa_banco(verifica_cadastro_ativo)
        
        if(retorno != 0): #se o cpf foi encontrado no banco de dados
            if(cadastro_ativo[0][0] == 0):
                print("\nCPF já cadastrado no banco de dados! Reativando cadastro...\n")
                consulta_sql = f"UPDATE Pessoa SET cadastro_ativo = 1 WHERE cpf = {cpf}"
                self.gerencia.acessa_banco(consulta_sql)
                time.sleep(3)
                return -2

            else:
                print("\nCPF já cadastrado no banco de dados! Retornando ao menu...\n")
                time.sleep(3)
                return -2

        nome = input("Insira o nome:\n").lower()
        email = input("Insira o email:\n").lower()

        data_nascimento[2] = input("Insira o dia da data de nascimento:\n")
        data_nascimento[1] = input("Insira o mes da data de nascimento:\n")
        data_nascimento[0] = input("Insira o ano da data de nascimento:\n")
        
        validacao_data = self.verifica_data(data_nascimento)

        if validacao_data == False:
            print("Data inválida! Retornando ao menu...\n")
            time.sleep(3)
            return -3
                
        estado = input("Insira o estado:\n").lower()
        cidade = input("Insira a cidade:\n").lower()
        bairro = input("Insira o bairro:\n").lower()
        rua = input("Insira a rua:\n").lower()
        print('Insira o número da residência:')
        numero = self.input_numerica()

        while (1):
            tipo_pessoa = input(
                "Insira o cargo da pessoa - [1] Cliente [2] Funcionario:\n")
            if (tipo_pessoa == '1' or tipo_pessoa == '2'):
                break
            else:
                print("Opcao invalida, tente novamente")
        if (tipo_pessoa == '1'):
            tipo_pessoa = "Cliente"
        else:
            tipo_pessoa = "Funcionario"
            
        if(tipo_pessoa == "Funcionario"):
            print("Insira um login para o funcionário:")
            login = input().lower()
            print("Insira uma senha para o funcionário:")
            senha = input().lower()
            print("Insira o cargo do funcionário:")
            cargo = input().lower()
            
        elif(tipo_pessoa == "Cliente"):
            while (1):
                ve_onepiece = input("O cliente ve one piece? - [1] Sim [2] Não\n")
                if (ve_onepiece == '1' or ve_onepiece == '2'):
                    break
                else:
                    print("Opcao invalida, tente novamente")
                    
            if(ve_onepiece == '1'):
                ve_onepiece = 1
            elif(ve_onepiece == '2'):
                ve_onepiece = 0
                
            while (1):
                is_flamengo = input("O cliente é flamenguista? - [1] Sim [2] Não\n")
                if (is_flamengo == '1' or is_flamengo == '2'):
                    break
                else:
                    print("Opcao invalida, tente novamente")
                    
            if(is_flamengo == '1'):
                is_flamengo = 1
            elif(is_flamengo == '2'):
                is_flamengo = 0
            

        #comando SQL #############################################################
        comando_inserir = f"INSERT INTO Pessoa (cpf, nome, email, data_nascimento, tipo_pessoa, cadastro_ativo) VALUES \
                          ('{str(cpf)}', '{nome}', '{email}', '{str(data_nascimento[0])}-{str(data_nascimento[1])}-{str(data_nascimento[2])}','{tipo_pessoa}', 1)"

        self.gerencia.acessa_banco(comando_inserir)
        
        comando_inserir = f"INSERT INTO Endereco (cpf, estado, cidade, bairro, rua, numero) VALUES \
                          ('{str(cpf)}','{estado}', '{cidade}', '{bairro}', '{rua}', {str(numero)})"
                          
        self.gerencia.acessa_banco(comando_inserir)
        
        if(tipo_pessoa == "Funcionario"):
            comando_inserir = f"INSERT INTO Funcionario (cpf, login, senha, tipo_funcionario) VALUES \
                            ('{str(cpf)}','{login}', '{senha}', '{cargo}')"
                            
            self.gerencia.acessa_banco(comando_inserir)
            
        elif(tipo_pessoa == "Cliente"):
            comando_inserir = f"INSERT INTO Cliente (cpf, ve_onepiece, is_flamengo) VALUES \
                            ('{str(cpf)}',{ve_onepiece}, {is_flamengo})"
                            
            self.gerencia.acessa_banco(comando_inserir)
        ##########################################################################
        
        print("Pessoa inserida com sucesso!\n")
        input("Pressione ENTER para continuar...")

    def editar_pessoa(self):

        print("Digite o CPF da pessoa que você deseja alterar: ")
        cpf_procurado = self.input_numerica()

        consulta_sql = "SELECT * FROM Pessoa WHERE cpf = " + cpf_procurado  # procurando o cpf
        
        retorno = self.gerencia.acessa_banco(consulta_sql)

        if retorno == 0:  # se não teve nenhum cpf encontrado, nao será possivel alterar
            print('CPF procurado não está cadastrado ou é inválido')
            time.sleep(3)
            return -1
        else:
            print('\nQual campo da tabela você deseja alterar? ')
            print('0- nome\n1- email\n2 - data de nascimento\n3 - estado\n4 - cidade\n5 - bairro\n6 - rua\n7 - numero\n8 - cargo\n9 - VOLTAR AO MENU')
            opcao = input()

            campos = ['nome', 'email', 'data_nascimento', 'estado','cidade', 'bairro', 'rua', 'numero', 'tipo_pessoa']
            update_sql = ''

            if int(opcao) > 9 or int(opcao) < 0:  #opcao invalida
                print("Você digitou uma opção inválida!")
                return -1

            elif int(opcao) == 9:  #usuario optou por voltar ao menu
                return 0
            
            elif int(opcao) == 2:
                print('Digite o novo valor do campo dia de nascimento: ')
                subst_dia = self.input_numerica()
                print('Digite o novo valor do campo mês de nascimento: ')
                subst_mes = self.input_numerica()
                print('Digite o novo valor do campo ano de nascimento: ')
                subst_ano = self.input_numerica()

                validacao_data = self.verifica_data([subst_ano, subst_mes, subst_dia])

                if validacao_data == False:
                    print("Data inválida! Retornando ao menu...\n")
                    time.sleep(3)
                    return -2

                update_sql = f"UPDATE Pessoa SET {campos[int(opcao)]} = '{subst_ano}-{subst_mes}-{subst_dia}' WHERE cpf = '{cpf_procurado}';"

            elif int(opcao) == 8:

                while (1):
                    subst_campo = input("Digite o novo valor do campo cargo [1] Cliente [2] Funcionario:\n")
                    if (subst_campo == '1' or subst_campo == '2'):
                        break
                    else:
                        print("Opcao invalida, tente novamente")

                if (subst_campo == '1'):
                    subst_campo = "Cliente"
                else:
                    subst_campo = "Funcionario"

                update_sql = f"UPDATE Pessoa SET {campos[int(opcao)]} = '{subst_campo}' WHERE cpf = '{cpf_procurado}';"

            else:
                print('Digite o novo valor do campo ' + campos[int(opcao)] + ': ')

                if int(opcao) == 7:   #se for o numero da casa que o usuario tiver que digitar
                    subst_campo = self.input_numerica()
                else:
                    subst_campo = input()

                update_sql = f"UPDATE Pessoa SET {campos[int(opcao)]} = '{subst_campo}' WHERE cpf = '{cpf_procurado}';"
            
            self.gerencia.acessa_banco(update_sql)
            print('Alteração realizada com sucesso!')
            time.sleep(3)

    def exibir_um(self, cpf_input = 0):
        if(cpf_input == 0):
            print("Digite o CPF da pessoa que você deseja exibir: ")
            cpf_procurado = self.input_numerica()
            
        else:
            cpf_procurado = cpf_input

        consulta_sql = "SELECT P.CPF, P.nome, P.email, P.data_nascimento, E.estado, E.cidade, \
        E.bairro, E.rua, E.numero, P.tipo_pessoa, P.cadastro_ativo FROM Pessoa P, Endereco E WHERE P.cpf = E.cpf AND P.CPF = " + cpf_procurado  # procurando o cpf
        
        resultados = self.gerencia.acessa_banco(consulta_sql)

        if len(resultados) == 0:  # se não teve nenhum cpf encontrado, nao será possivel exibir
            print('CPF procurado não está cadastrado ou é inválido')
            return -1
        else:
            for linha in resultados:
                print("\ncpf:", linha[0])
                print("nome:", linha[1])
                print("email:", linha[2])
                print("data de nascimento:", linha[3])
                print("estado:", linha[4])
                print("cidade:", linha[5])
                print("bairro:", linha[6])
                print("rua:", linha[7])
                print("numero:", linha[8])
                print("cargo:", linha[9])
                print("cadastro ativo:", bool(linha[10]))
                
        if(linha[9] == 'Cliente'):
            consulta_sql = f"SELECT * FROM Cliente WHERE cpf = {cpf_procurado}"
            resultados = self.gerencia.acessa_banco(consulta_sql)
            for linha in resultados:
                print("Vê One Piece:", bool(linha[1]))
                print("É flamenguista:", bool(linha[2]))
                print("\n")
                
        elif(linha[9] == 'Funcionario'):
            consulta_sql = f"SELECT * FROM Funcionario WHERE cpf = {cpf_procurado}"
            resultados = self.gerencia.acessa_banco(consulta_sql)
            for linha in resultados:
                print("Login:", linha[1])
                print("Senha:", linha[2])
                print("Cargo:", linha[3])
                print("\n")

        input("Pressione ENTER para continuar...")


    def exibir_todos(self):
        
        consulta_sql = "SELECT P.CPF, P.nome, P.email, P.data_nascimento, E.estado, E.cidade, \
        E.bairro, E.rua, E.numero, P.tipo_pessoa FROM Pessoa P, Endereco E WHERE P.cpf = E.cpf AND P.cadastro_ativo = 1 ORDER BY P.nome ASC"

        linhas = self.gerencia.acessa_banco(consulta_sql)

        for linha in linhas:
            print("\ncpf:", linha[0])
            print("nome:", linha[1])
            print("email:", linha[2])
            print("data de nascimento:", linha[3])
            print("estado:", linha[4])
            print("cidade:", linha[5])
            print("bairro:", linha[6])
            print("rua:", linha[7])
            print("numero:", linha[8])
            print("cargo:", linha[9])
            print("\n")
            
        input("Pressione ENTER para continuar...")
            
    def deletar_pessoa(self):
        print("Digite o CPF que deseja deletar: ")
        cpf = self.input_numerica()
        consulta_sql = f"UPDATE Pessoa SET cadastro_ativo = 0 WHERE cpf = '{cpf}';"
        
        self.gerencia.acessa_banco(consulta_sql)

        print("Deletado com sucesso.")
        
        input("Pressione ENTER para continuar...\n")      

    def procurar_nome(self):

        nome = input("Digite o nome a ser procurado: ").lower()
        consulta_sql = f"SELECT P.CPF, P.nome, P.email, P.data_nascimento, E.estado, E.cidade, \
        E.bairro, E.rua, E.numero, P.tipo_pessoa FROM Pessoa P, Endereco E WHERE P.cpf = E.cpf AND P.nome = '{nome}' AND P.cadastro_ativo = 1 ORDER BY P.nome ASC"
        retorno = self.gerencia.acessa_banco(consulta_sql)
        
        qtd_cadastros = len(retorno)

        print("Número total de registros retornados: ", qtd_cadastros)

        for linha in retorno:
            print("\ncpf:", linha[0])
            print("nome:", linha[1])
            print("email:", linha[2])
            print("data de nascimento:", linha[3])
            print("estado:", linha[4])
            print("cidade:", linha[5])
            print("bairro:", linha[6])
            print("rua:", linha[7])
            print("numero:", linha[8])
            print("cargo:", linha[9])
            print("\n")

        input("Pressione ENTER para continuar...")
        
    def gerar_relatorio(self):
        
        consulta_sql = "SELECT P.CPF, P.nome, P.email, P.data_nascimento, E.estado, E.cidade, \
        E.bairro, E.rua, E.numero, P.tipo_pessoa FROM Pessoa P, Endereco E WHERE P.cpf = E.cpf AND P.cadastro_ativo = 1 ORDER BY P.nome ASC"
        
        retorno = self.gerencia.acessa_banco(consulta_sql)
        
        qtd_cadastros = len(retorno)

        try:
            with open('relatorio.txt', 'w') as arquivo:
                
                arquivo.write(f'Número total de registros retornados: {qtd_cadastros}\n')
                
                for linha in retorno:
                    arquivo.write(f"\ncpf: {linha[0]}\n" )
                    arquivo.write(f"nome: {linha[1]}\n")
                    arquivo.write(f"email: {linha[2]}\n")
                    arquivo.write(f"data de nascimento: {linha[3]}\n")
                    arquivo.write(f"estado: {linha[4]}\n")
                    arquivo.write(f"cidade: {linha[5]}\n")
                    arquivo.write(f"bairro: {linha[6]}\n")
                    arquivo.write(f"rua: {linha[7]}\n")
                    arquivo.write(f"numero: {linha[8]}\n")
                    arquivo.write(f"cargo: {linha[9]}\n")
                    
                if(linha[9] == 'Cliente'):
                    consulta_sql = f"SELECT * FROM Cliente WHERE cpf = {linha[0]}"
                    resultados = self.gerencia.acessa_banco(consulta_sql)
                    for linha in resultados:
                        arquivo.write(f"Vê One Piece: {bool(linha[1])}\n")
                        arquivo.write(f"É flamenguista: {bool(linha[2])}\n")
                        
                elif(linha[9] == 'Funcionario'):
                    consulta_sql = f"SELECT * FROM Funcionario WHERE cpf = {linha[0]}"
                    resultados = self.gerencia.acessa_banco(consulta_sql)
                    for linha in resultados:
                        arquivo.write(f"Login: {linha[1]}\n")
                        arquivo.write(f"Senha: {linha[2]}\n")
                        arquivo.write(f"Cargo: {linha[3]}\n")
                    
                print('Relatório gerado com sucesso!')
                time.sleep(2)
        except IOError as e:
            print(f"Erro ao criar ou escrever no arquivo: {str(e)}")

        

    def input_numerica(self):

        while True:
            dado = input()

            if dado.isnumeric(): 
                break
            else:
                print('Só é permitido números, tente novamente: ', end='')
        
        return dado
    
    def verifica_data(self, data_nasc):

        # data_formatada = f'{data_nasc[0]}-{data_nasc[1]}-{data_nasc[2]}'
        # data_cadastrada = datetime.strptime(data_formatada, '%Y-%m-%d')
        
        data_nasc[0] = int(data_nasc[0])
        data_nasc[1] = int(data_nasc[1])
        data_nasc[2] = int(data_nasc[2])

        if (data_nasc[0] > date.today().year) or (data_nasc[1] > date.today().month and data_nasc[0] == date.today().year):
            return False 
            
        elif data_nasc[2] > date.today().day and data_nasc[1] == date.today().month and data_nasc[1] == date.today().month and data_nasc[0] == date.today().year:
            return False

        elif data_nasc[2] > 31 or data_nasc[1] > 12:
            return False
        
        elif data_nasc[2] > 28 and data_nasc[1] == 2:  
            return False
        
        elif (data_nasc[2] == 31) and (data_nasc[1] == 4 or data_nasc[1] == 6 or data_nasc[1] == 9 or data_nasc[1] == 11):
            return False
        
        else: 
            return True

    def verifica_cpf(self, cpf):

        if (len(cpf) < 11 or len(cpf) > 11):
            return False

        contador_digitos_iguais = 0
        digito_inicial = cpf[0]

        for digito in cpf:
            if digito_inicial == digito:
                contador_digitos_iguais += 1

        if contador_digitos_iguais == 11:
            return False

        cpf_9digitos = cpf[0:9]

        cpf_digito_verificador = cpf[9:]

        digito_1 = 0
        digito_2 = 0
        soma_digito_1 = 0
        soma_digito_2 = 0
        for i, digito in enumerate(cpf_9digitos):
            soma_digito_1 += ((10 - i) * int(digito))

        resto_soma_digito_1 = soma_digito_1 % 11
        if resto_soma_digito_1 < 2:
            digito_1 = 0
        else:
            digito_1 = 11 - resto_soma_digito_1

        # Se o primeiro digito nao estiver certo, eh porque ja eh invalido
        if digito_1 != int(cpf_digito_verificador[0]):
            return False

        cpf_10digitos = cpf[0:10]
        for i, digito in enumerate(cpf_10digitos):
            soma_digito_2 += ((11 - i) * int(digito))

        resto_soma_digito_2 = soma_digito_2 % 11

        if resto_soma_digito_2 < 2:
            digito_2 = 0
        else:
            digito_2 = 11 - resto_soma_digito_2

        if digito_2 != int(cpf_digito_verificador[1]):
            return False

        return True
    
    def tenta_login(self):
        
        login_teste = input("Digite seu login:")

        consulta_sql = f"SELECT * FROM Funcionario WHERE login = '{login_teste}'"
        retorno = self.gerencia.acessa_banco(consulta_sql)
        
        if (retorno == 0):
            print("Login inexistente")
        else:
            senha_teste = input("Digite sua senha:")
            consulta_sql = f"SELECT * FROM Funcionario WHERE senha = '{senha_teste}'"
            retorno = self.gerencia.acessa_banco(consulta_sql)
            
            if(retorno == 0):
                print("Senha incorreta")
            else:
                return 1
        
        return -1
    
    def area_cliente(self):
            
            cpf = input("Digite seu CPF:")
            
            consulta_sql = f"SELECT * FROM Pessoa WHERE cpf = '{cpf}'"
            retorno = self.gerencia.acessa_banco(consulta_sql)
            
            if (retorno == 0):
                print("CPF inexistente")
                return -1
            else:
                consulta_sql = f"SELECT * FROM Cliente WHERE cpf = '{cpf}'"
                retorno = self.gerencia.acessa_banco(consulta_sql)
                
                if(retorno == 0):
                    print("CPF não é de um cliente")
                    return -1
                else:
                    while(1):
                        opcao = input("O que deseja ver? [1] Dados cadastrais [2] Compras realizadas [3] Voltar ao menu\n")
                        if (opcao == '1'):
                            self.exibir_um(cpf)
                            self.limpar_tela()
                            
                        elif(opcao == '2'):
                            consulta_sql = f"SELECT * FROM Venda WHERE cpf_cliente = '{cpf}'"
                            retorno = self.gerencia.acessa_banco(consulta_sql)
                            for linha in retorno:
                                print("codigo da venda:", linha[0])
                                print("data da venda:", linha[3])
                                print("valor total:", linha[5])
                                print("forma de pagamento:", linha[6])
                                print("status da venda:", linha[7])

                                consulta_sql = f"SELECT M.nome, C.quantidade FROM Carrinho C, Medicamento M WHERE C.cod_venda = '{linha[0]}' AND C.cod_medicamento = M.cod_medicamento"
                                itens = self.gerencia.acessa_banco(consulta_sql)
                                for linha in itens:
                                    print("Medicamento:", linha[0], "quantidade:", linha[1])
                                    
                            input("Pressione ENTER para continuar...")
                            self.limpar_tela()
                            
                        elif (opcao == '3'):
                            break
                        
                    
                    
            