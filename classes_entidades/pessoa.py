import time
from gerencia_sql import Gerenciamento
from datetime import datetime
from datetime import date
import os
from termcolor import colored

TITLECOLOR = "blue"
TEXTCOLOR = "yellow"

class Pessoa:

    # Método construtor
    def __init__(self, conexao):
        self.gerencia = Gerenciamento(conexao)
        
    def limpar_tela(self):
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')

    # Método para imprimir informações da pessoa
    def inserir_pessoa(self):
        self.limpar_tela()
        data_nascimento = [None, None, None]
        resultados = 'INVALID'

        print(colored("Insira o CPF:", TEXTCOLOR))
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

        nome = input(colored("Insira o nome:\n", TEXTCOLOR)).lower()
        email = input(colored("Insira o email:\n", TEXTCOLOR)).lower()

        data_nascimento[2] = input(colored("Insira o dia da data de nascimento:\n", TEXTCOLOR))
        data_nascimento[1] = input(colored("Insira o mes da data de nascimento:\n", TEXTCOLOR))
        data_nascimento[0] = input(colored("Insira o ano da data de nascimento:\n", TEXTCOLOR))
        
        validacao_data = self.verifica_data(data_nascimento)

        if validacao_data == False:
            print("Data inválida! Retornando ao menu...\n")
            time.sleep(3)
            return -3
                
        estado = input(colored("Insira o estado:\n", TEXTCOLOR)).lower()
        cidade = input(colored("Insira a cidade:\n", TEXTCOLOR)).lower()
        bairro = input(colored("Insira o bairro:\n", TEXTCOLOR)).lower()
        rua = input(colored("Insira a rua:\n", TEXTCOLOR)).lower()
        print(colored('Insira o número da residência:', TEXTCOLOR))
        numero = self.input_numerica()

        while (1):
            tipo_pessoa = input(
                colored("Insira o cargo da pessoa - [1] Cliente [2] Funcionario:\n", TEXTCOLOR))
            if (tipo_pessoa == '1' or tipo_pessoa == '2'):
                break
            else:
                print("Opcao invalida, tente novamente")
        if (tipo_pessoa == '1'):
            tipo_pessoa = "Cliente"
        else:
            tipo_pessoa = "Funcionario"
            
        if(tipo_pessoa == "Funcionario"):
            print(colored("Insira um login para o funcionário:", TEXTCOLOR))
            login = input().lower()
            print(colored("Insira uma senha para o funcionário:", TEXTCOLOR))
            senha = input().lower()
            print(colored("Insira o cargo do funcionário:", TEXTCOLOR))
            cargo = input().lower()
            
        elif(tipo_pessoa == "Cliente"):
            while (1):
                ve_onepiece = input(colored("O cliente ve one piece? - [1] Sim [2] Não\n", TEXTCOLOR))
                if (ve_onepiece == '1' or ve_onepiece == '2'):
                    break
                else:
                    print("Opcao invalida, tente novamente")
                    
            if(ve_onepiece == '1'):
                ve_onepiece = 1
            elif(ve_onepiece == '2'):
                ve_onepiece = 0
                
            while (1):
                is_flamengo = input(colored("O cliente é flamenguista? - [1] Sim [2] Não\n", TEXTCOLOR))
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
        self.limpar_tela()

        print(colored("Digite o CPF da pessoa que você deseja alterar: ", TEXTCOLOR))
        cpf_procurado = self.input_numerica()

        consulta_sql = "SELECT * FROM Pessoa WHERE cpf = " + cpf_procurado  # procurando o cpf
        retorno = self.gerencia.acessa_banco(consulta_sql)

        if retorno == 0:  # se não teve nenhum cpf encontrado, nao será possivel alterar
            print('CPF procurado não está cadastrado ou é inválido')
            time.sleep(3)
            return -1
        else:
            print(colored('\nQual campo da tabela você deseja alterar? ', TITLECOLOR))
            print(colored('0 - nome\n1- email\n2 - data de nascimento\n3 - estado\n4 - cidade\n5 - bairro\n6 - rua\n7 - numero\n', TEXTCOLOR))
            print(colored('8 - vê One Piece\n9 - flameguista\n10 - login\n11 - senha\n12 - VOLTAR AO MENU', TEXTCOLOR))

            opcao = input()

            campos = ['nome', 'email', 'data_nascimento', 'estado','cidade', 'bairro', 'rua', 'numero', 'tipo_pessoa']
            update_sql = ''

            if int(opcao) > 12 or int(opcao) < 0:  #opcao invalida
                print("Você digitou uma opção inválida!")
                return -1

            elif int(opcao) == 12:  #usuario optou por voltar ao menu
                return 0
            
            elif int(opcao) == 2:
                print(colored('Digite o novo valor do campo dia de nascimento: ', TEXTCOLOR))
                subst_dia = self.input_numerica()
                print(colored('Digite o novo valor do campo mês de nascimento: ', TEXTCOLOR))
                subst_mes = self.input_numerica()
                print(colored('Digite o novo valor do campo ano de nascimento: ', TEXTCOLOR))
                subst_ano = self.input_numerica()

                validacao_data = self.verifica_data([subst_ano, subst_mes, subst_dia])

                if validacao_data == False:
                    print("Data inválida! Retornando ao menu...\n")
                    time.sleep(3)
                    return -2

                update_sql = f"UPDATE Pessoa SET {campos[int(opcao)]} = '{subst_ano}-{subst_mes}-{subst_dia}' WHERE cpf = '{cpf_procurado}';"

            elif (int(opcao) >= 3 and int(opcao) <= 7):  #campos relacionados a enderco
                print(colored('Digite o novo valor do campo ' + campos[int(opcao)] + ': ', TEXTCOLOR))
                subst_campo = input()
                update_sql = f"UPDATE Endereco SET {campos[int(opcao)]} = '{subst_campo}' WHERE cpf = '{cpf_procurado}';"


            elif(opcao == '0' or opcao == '1'):  #campos relacionados a pessoa
                print(colored('Digite o novo valor do campo ' + campos[int(opcao)] + ': ', TEXTCOLOR))
                subst_campo = input()
                update_sql = f"UPDATE Pessoa SET {campos[int(opcao)]} = '{subst_campo}' WHERE cpf = '{cpf_procurado}';"

            elif(opcao == '8' or opcao == '9'):
                consulta_sql = "SELECT * FROM Cliente WHERE cpf = " + cpf_procurado  # procurando o cpf
                retorno = self.gerencia.acessa_banco(consulta_sql)

                if retorno == 0:  # se não teve nenhum cpf encontrado, nao será possivel alterar
                    print(colored('CPF procurado não está cadastrado como cliente', TEXTCOLOR))
                    return -1

                if(opcao == '8'):
                    print(colored('Digite o novo valor do campo vê One Piece: \n[0] Não\n[1] Sim', TEXTCOLOR))
                    campo_cli = "v_onepiece"
                else:
                    print(colored('Digite o novo valor do campo Flamenguista: \n[0] Não\n[1] Sim', TEXTCOLOR))
                    campo_cli= "is_flamengo"

                subst_campo = input()

                update_sql = f"UPDATE Cliente SET {campo_cli} = {int(subst_campo)} WHERE cpf = '{cpf_procurado}';"

            elif(opcao == '10' or opcao == '11'):
                consulta_sql = "SELECT * FROM Funcionario WHERE cpf = " + cpf_procurado  # procurando o cpf
                retorno = self.gerencia.acessa_banco(consulta_sql)

                if retorno == 0:  # se não teve nenhum cpf encontrado, nao será possivel alterar
                    print('CPF procurado não está cadastrado como funcionario')
                    return -1

                if(opcao == '10'):
                    print(colored('Digite o novo valor do campo login: ', TEXTCOLOR))
                    campo_func = "login"

                else:
                    print(colored('Digite o novo valor do campo senha: ', TEXTCOLOR))
                    campo_func = "senha"

                subst_campo = input()

                update_sql = f"UPDATE Funcionario SET {campo_func} = {int(subst_campo)} WHERE cpf = '{cpf_procurado}';"

            self.gerencia.acessa_banco(update_sql)
            print('Alteração realizada com sucesso!')
            time.sleep(3)

    def exibir_um(self, cpf_input = 0):
        self.limpar_tela()
        if(cpf_input == 0):
            print(colored("Digite o CPF da pessoa que você deseja exibir: ", TEXTCOLOR))
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
                print(colored(("\ncpf:", linha[0]), TEXTCOLOR))
                print(colored(("nome:", linha[1]), TEXTCOLOR))
                print(colored(("email:", linha[2]), TEXTCOLOR))
                print(colored(("data de nascimento:", linha[3]), TEXTCOLOR))
                print(colored(("estado:", linha[4]), TEXTCOLOR))
                print(colored(("cidade:", linha[5]), TEXTCOLOR))
                print(colored(("bairro:", linha[6]), TEXTCOLOR))
                print(colored(("rua:", linha[7]), TEXTCOLOR))
                print(colored(("numero:", linha[8]), TEXTCOLOR))
                print(colored(("cargo:", linha[9]), TEXTCOLOR))
                print(colored(("cadastro ativo:", bool(linha[10])), TEXTCOLOR))
                
        if(linha[9] == 'Cliente'):
            consulta_sql = f"SELECT * FROM Cliente WHERE cpf = {cpf_procurado}"
            resultados = self.gerencia.acessa_banco(consulta_sql)
            for linha in resultados:
                print(colored(("Vê One Piece:", bool(linha[1])), TEXTCOLOR))
                print(colored(("É flamenguista:", bool(linha[2])), TEXTCOLOR))
                print("\n")
                
        elif(linha[9] == 'Funcionario'):
            consulta_sql = f"SELECT * FROM Funcionario WHERE cpf = {cpf_procurado}"
            resultados = self.gerencia.acessa_banco(consulta_sql)
            for linha in resultados:
                print(colored(("Login:", linha[1]), TEXTCOLOR))
                print(colored(("Senha:", linha[2]), TEXTCOLOR))
                print(colored(("Cargo:", linha[3]), TEXTCOLOR))
                print("\n")

        input("Pressione ENTER para continuar...")


    def exibir_todos(self):
        
        self.limpar_tela()
        consulta_sql = "SELECT P.CPF, P.nome, P.email, P.data_nascimento, E.estado, E.cidade, \
        E.bairro, E.rua, E.numero, P.tipo_pessoa FROM Pessoa P, Endereco E WHERE P.cpf = E.cpf AND P.cadastro_ativo = 1 ORDER BY P.nome ASC"

        linhas = self.gerencia.acessa_banco(consulta_sql)

        for linha in linhas:
            print(colored(("\ncpf:", linha[0]), TEXTCOLOR))
            print(colored(("nome:", linha[1]), TEXTCOLOR))
            print(colored(("email:", linha[2]), TEXTCOLOR))
            print(colored(("data de nascimento:", linha[3]), TEXTCOLOR))
            print(colored(("estado:", linha[4]), TEXTCOLOR))
            print(colored(("cidade:", linha[5]), TEXTCOLOR))
            print(colored(("bairro:", linha[6]), TEXTCOLOR))
            print(colored(("rua:", linha[7]), TEXTCOLOR))
            print(colored(("numero:", linha[8]), TEXTCOLOR))
            print(colored(("cargo:", linha[9]), TEXTCOLOR))
            print("\n")
            
        input("Pressione ENTER para continuar...")
            
    def deletar_pessoa(self):
        self.limpar_tela()
        print(colored("Digite o CPF que deseja deletar: ", TEXTCOLOR))
        cpf = self.input_numerica()
        consulta_sql = f"UPDATE Pessoa SET cadastro_ativo = 0 WHERE cpf = '{cpf}';"
        
        self.gerencia.acessa_banco(consulta_sql)

        print("Deletado com sucesso.")
        
        input("Pressione ENTER para continuar...\n")      

    def procurar_nome(self):

        self.limpar_tela()
        nome = input(colored("Digite o nome a ser procurado: ", TEXTCOLOR)).lower()
        consulta_sql = f"SELECT P.CPF, P.nome, P.email, P.data_nascimento, E.estado, E.cidade, \
        E.bairro, E.rua, E.numero, P.tipo_pessoa FROM Pessoa P, Endereco E WHERE P.cpf = E.cpf AND P.nome = '{nome}' AND P.cadastro_ativo = 1 ORDER BY P.nome ASC"
        retorno = self.gerencia.acessa_banco(consulta_sql)
        
        qtd_cadastros = len(retorno)

        print(colored(("Número total de registros retornados: ", qtd_cadastros), TEXTCOLOR))

        for linha in retorno:
            print(colored(("\ncpf:", linha[0]), TEXTCOLOR))
            print(colored(("nome:", linha[1]), TEXTCOLOR))
            print(colored(("email:", linha[2]), TEXTCOLOR))
            print(colored(("data de nascimento:", linha[3]), TEXTCOLOR))
            print(colored(("estado:", linha[4]), TEXTCOLOR))
            print(colored(("cidade:", linha[5]), TEXTCOLOR))
            print(colored(("bairro:", linha[6]), TEXTCOLOR))
            print(colored(("rua:", linha[7]), TEXTCOLOR))
            print(colored(("numero:", linha[8]), TEXTCOLOR))
            print(colored(("cargo:", linha[9]), TEXTCOLOR))
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
        
        self.limpar_tela()
        login_teste = input(colored("Digite seu login:", TEXTCOLOR))

        consulta_sql = f"SELECT * FROM Funcionario WHERE login = '{login_teste}'"
        retorno = self.gerencia.acessa_banco(consulta_sql)
        
        if (retorno == 0):
            print("Login inexistente")
        else:
            senha_teste = input(colored("Digite sua senha:", TEXTCOLOR))
            consulta_sql = f"SELECT * FROM Funcionario WHERE senha = '{senha_teste}'"
            retorno = self.gerencia.acessa_banco(consulta_sql)
            
            if(retorno == 0):
                print("Senha incorreta")
            else:
                return 1
        
        return -1
    
    def area_cliente(self):
            
            self.limpar_tela()
            cpf = input(colored("Digite seu CPF:", TEXTCOLOR))
            
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
                        self.limpar_tela()
                        opcao = input(colored("O que deseja ver? [1] Dados cadastrais [2] Compras realizadas [3] Voltar ao menu\n", TEXTCOLOR))
                        if (opcao == '1'):
                            self.limpar_tela()
                            self.exibir_um(cpf)
                            
                        elif(opcao == '2'):
                            consulta_sql = f"SELECT * FROM Venda WHERE cpf_cliente = '{cpf}'"
                            retorno = self.gerencia.acessa_banco(consulta_sql)
                            for linha in retorno:
                                print(colored(("\ncodigo da venda:", linha[0]), TEXTCOLOR))
                                print(colored(("data da venda:", linha[3]), TEXTCOLOR))
                                print(colored(("valor total:", linha[5]), TEXTCOLOR))
                                print(colored(("forma de pagamento:", linha[6]), TEXTCOLOR))
                                print(colored(("status da venda:", linha[7]), TEXTCOLOR))

                                consulta_sql = f"SELECT M.nome, C.quantidade FROM Carrinho C, Medicamento M WHERE C.cod_venda = '{linha[0]}' AND C.cod_medicamento = M.cod_medicamento"
                                itens = self.gerencia.acessa_banco(consulta_sql)
                                for linha in itens:
                                    print(colored(("Medicamento:", linha[0], "quantidade:", linha[1]), TEXTCOLOR))
                                    
                            input("Pressione ENTER para continuar...")
                            self.limpar_tela()
                            
                        elif (opcao == '3'):
                            break
                        
                    
                    
            