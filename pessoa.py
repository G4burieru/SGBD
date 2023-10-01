import time


class Pessoa:
    # Variável de classe
    connection = None
    cpf = None
    nome = None
    email = None
    data_nascimento = [None, None, None]
    estado = None
    cidade = None
    bairro = None
    rua = None
    numero = None
    tipo_pessoa = None

    # Método construtor
    def __init__(self, conexao):
        self.connection = conexao
        pass

    # Método para imprimir informações da pessoa
    def inserir_pessoa(self):

        self.cpf = input("Insira o CPF:\n")
        validacao = self.verifica_cpf(self.cpf)
        
        if not validacao:
            print("Digite um cpf válido.\n")
            time.sleep(1)
            return -1
        
        self.nome = input("Insira o nome:\n").lower()
        self.email = input("Insira o email:\n").lower()
        self.data_nascimento[2] = input(
            "Insira o dia da data de nascimento:\n")
        self.data_nascimento[1] = input(
            "Insira o mes da data de nascimento:\n")
        self.data_nascimento[0] = input(
            "Insira o ano da data de nascimento:\n")
        self.estado = input("Insira o estado:\n").lower()
        self.cidade = input("Insira a cidade:\n").lower()
        self.bairro = input("Insira o bairro:\n").lower()
        self.rua = input("Insira a rua:\n").lower()
        self.numero = input("Insira o numero:\n")
        while (1):
            self.tipo_pessoa = input(
                "Insira o tipo de pessoa [1] Cliente [2] Funcionario:\n")
            if (int(self.tipo_pessoa) == 1 or int(self.tipo_pessoa) == 2):
                break
            else:
                print("Opcao invalida, tente novamente")
        if (int(self.tipo_pessoa) == 1):
            self.tipo_pessoa = "Cliente"
        else:
            self.tipo_pessoa = "Funcionario"

        comando_inserir = f"INSERT INTO Pessoa (cpf, nome, email, data_nascimento, estado, cidade, bairro, rua, numero, tipo_pessoa) VALUES \
                          ('{self.cpf}', '{self.nome}', '{self.email}', '{self.data_nascimento[0]}-{self.data_nascimento[1]}-{self.data_nascimento[2]}',\
                          '{self.estado}', '{self.cidade}', '{self.bairro}', '{self.rua}', {self.numero}, '{self.tipo_pessoa}')"

        return comando_inserir

    def editar_pessoa(self, cursor):

        print("Digite o CPF da pessoa que você deseja alterar: ")
        cpf_procurado = input()

        consulta_sql = "SELECT * FROM Pessoa WHERE cpf = " + \
            cpf_procurado  # procurando o cpf
        cursor.execute(consulta_sql)
        resultados = cursor.fetchall()  # armazenando o resultado com aquele cpf

        if len(resultados) == 0:  # se não teve nenhum cpf encontrado, nao será possivel alterar
            return -1
        else:
            print('\nQual campo da tabela você deseja alterar? ')
            print(
                '0 - CPF\n1- nome\n2 - email\n3 - endereco\n4 - tipo de pessoa\n5 - data de nascimento')
            opcao = input()

            campos = ['cpf', 'nome', 'email', 'endereco',
                      'tipo_pessoa', 'data_nascimento']
            update_sql = ''

            if int(opcao) > 5 or int(opcao) < 0:  # opcao invalida
                print("erraste as opcoes bebe")
                return -1

            elif int(opcao) == 5:
                print('Digite o novo valor do campo dia de nascimento: ')
                subst_dia = input()
                print('Digite o novo valor do campo mês de nascimento: ')
                subst_mes = input()
                print('Digite o novo valor do campo ano de nascimento: ')
                subst_ano = input()

                update_sql = f"UPDATE Pessoa SET {campos[int(opcao)]} = '{subst_ano}-{subst_mes}-{subst_dia}' WHERE cpf = '{cpf_procurado}';"

            else:
                print('Digite o novo valor do campo ' +
                      campos[int(opcao)] + ': ')
                subst_campo = input()

                update_sql = f"UPDATE Pessoa SET {campos[int(opcao)]} = '{subst_campo}' WHERE cpf = '{cpf_procurado}';"

            cursor.execute(update_sql)

    def exibir_um(self, cursor):

        print("Digite o CPF da pessoa que você deseja exibir: ")
        cpf_procurado = input()

        consulta_sql = "SELECT * FROM Pessoa WHERE cpf = " + \
            cpf_procurado  # procurando o cpf
        cursor.execute(consulta_sql)
        resultados = cursor.fetchall()  # armazenando o resultado com aquele cpf

        if len(resultados) == 0:  # se não teve nenhum cpf encontrado, nao será possivel exibir
            return -1
        else:
            for linha in resultados:
                print("\ncpf:", linha[0])
                print("nome:", linha[1])
                print("email:", linha[2])
                print("data de nascimento:", linha[3])
                print("estado:", linha[4]),
                print("cidade:", linha[5]),
                print("bairro:", linha[6]),
                print("rua:", linha[7]),
                print("numero:", linha[8])
                print("cargo:", linha[9])
                print("\n")

        self.connection.commit()
        input("Pressione ENTER para continuar...")

    def exibir_todos(self, cursor):
        
        self.consulta_sql = "SELECT * FROM Pessoa"
        
        cursor.execute(self.consulta_sql)
        self.linhas = cursor.fetchall()
        
        self.qtd_cadastros = cursor.rowcount

        print("Número total de registros retornados: ", self.qtd_cadastros)

        for linha in self.linhas:
            print("\ncpf:", linha[0])
            print("nome:", linha[1])
            print("email:", linha[2])
            print("data de nascimento:", linha[3])
            print("estado:", linha[4]),
            print("cidade:", linha[5]),
            print("bairro:", linha[6]),
            print("rua:", linha[7]),
            print("numero:", linha[8])
            print("cargo:", linha[9])
            print("\n")

        self.connection.commit()
        input("Pressione ENTER para continuar...")

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

    def deletar_pessoa(self, cursor, cpf):
        print("Deletando...")
        time.sleep(2)
        consulta_sql = f'Delete FROM Pessoa WHERE CPF={cpf};'
        cursor.execute(consulta_sql)

        retorno = cursor.rowcount
        if retorno <= 0:
            print("Nao foi encontrado o CPF no banco de dados.")
        else:  
            print("Deletado com sucesso.")
        
        self.connection.commit()
        print("Pressione ENTER para continuar...", end=" ")
        input()
           

    def procurar_nome(self, cursor, nome):

        consulta_sql = f'SELECT * FROM Pessoa WHERE nome = %s'
        cursor.execute(consulta_sql, (nome,))
        self.linhas = cursor.fetchall()
        
        self.qtd_cadastros = cursor.rowcount

        print("Número total de registros retornados: ", self.qtd_cadastros)

        for linha in self.linhas:
            print("\ncpf:", linha[0])
            print("nome:", linha[1])
            print("email:", linha[2])
            print("data de nascimento:", linha[3])
            print("estado:", linha[4]),
            print("cidade:", linha[5]),
            print("bairro:", linha[6]),
            print("rua:", linha[7]),
            print("numero:", linha[8])
            print("cargo:", linha[9])
            print("\n")

        self.connection.commit()
        input("Pressione ENTER para continuar...")
