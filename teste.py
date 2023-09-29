import mysql.connector
import os
import time
from pessoa import Pessoa



#Funcoes auxiliares
def limpar_tela():
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')


def verifica_cpf(cpf):

    if(len(cpf) < 11 or len(cpf) > 11):
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



def menu():
    
    while(1):
        print("BEM VINDO A FARMACIA!\nSELECIONE A OPCAO DESEJADA\n")
        print("1 - Inserir pessoa\n2 - Ver todas pessoas cadastradas\n3 - Excluir uma pessoa do banco de dados\n4 - Pesquisar por nome\n0 - Sair\n")
        opcao = input()
        pessoa1 = Pessoa()
        
        if opcao == "1":
            comando = pessoa1.inserir_pessoa()
            cursor.execute(comando)
            
        elif opcao == "2":
            consulta_sql = "SELECT * FROM Pessoa"
            cursor.execute(consulta_sql)         #executando a consulta de select *
            linha = cursor.fetchall()           #guardando todas as linhas da tabela na variavel linhas
            
            pessoa1.exibir_todos(cursor.rowcount, linha)
            input()            #esperando o usuario pressinar enter para continuar            
           
        elif opcao == "3":
            cpf = input("Digite o CPF que deseja deletar: ")
            validacao = verifica_cpf(cpf)
            
            if not validacao:
                print("Digite um CPF valido.\n")
            
            else:
                print("Deletando...")
                time.sleep(2)
                consulta_sql = f'Delete FROM Pessoa WHERE CPF={cpf};'
                cursor.execute(consulta_sql)

                if cursor.rowcount < 0:
                    print("Nao foi encontrado o CPF no banco de dados.")
                else:
                    print("Deletado com sucesso.")


            print("Pressione ENTER para continuar...", end=" ")
            input()
        
        elif opcao == "4":
            nome = input("Digite o nome a ser procurado: ").lower()
            consulta_sql = f'SELECT * FROM Pessoa WHERE nome = %s'
            cursor.execute(consulta_sql, (nome,))
            
            resultados = cursor.fetchall()
            
            if len(resultados) < 0:
                print("Nenhuma pessoa encontrada")
            else:
                pessoa1.exibir_todos(cursor.rowcount, resultados)

            input()

        elif opcao == "0":
            print("Saindo...")
            time.sleep(1)
            break
            
        else:
            print("Opcao invalida, tente novamente")
            time.sleep(2)            
        
        conexao.commit()
        limpar_tela()


# Configurações de conexão
host = "aws.connect.psdb.cloud"
usuario = "cbvc888azaeeqmlastk4"
senha = "pscale_pw_dhfPULoPzEv5iCuVS9APbcfLJEXsY454NrThJgcXXPs"
banco_de_dados = "farmacia"

# Conectar ao banco de dados
print("Conectando...")
conexao = mysql.connector.connect(
    host=host,
    user=usuario,
    password=senha,
    database=banco_de_dados,
)

if conexao.is_connected():
    print("Conectado ao banco de dados!")
    cursor = conexao.cursor()

    # Defina a consulta SQL para criar uma tabela (substitua os campos e tipos de dados conforme necessário)
    criar_tabela_sql = """
    CREATE TABLE IF NOT EXISTS Pessoa (
        CPF CHAR(11) PRIMARY KEY,
        email VARCHAR(255) NOT NULL,
        nome VARCHAR(255) NOT NULL,
        endereco VARCHAR(255) NOT NULL,
        tipo_pessoa VARCHAR(255) NOT NULL,
        data_nascimento DATE NOT NULL
    )
    """
    
    deletar_tabela_sql = """
    DROP TABLE Pessoa
    """

    # Execute a consulta SQL para deletar a tabela
    # cursor.execute(deletar_tabela_sql)
    # print("Tabela deletada com sucesso")
    
    # Execute a consulta SQL para criar a tabela
    # cursor.execute(criar_tabela_sql)
    # print("Tabela criada com sucesso.")
    
    menu()
    cursor.close()
    conexao.commit() #LEMBRAR DE VER ESSE COMMIT PQ SO ENVIA PRA O BANCO AS COISAS COM ELE, TALVEZ SEJA INTERESSANTE COLOCAR EM TODA FUNCAO
    conexao.close()

else:
    print("Não foi possível conectar ao banco de dados.")
    


# def inserir_pessoa():
#     cpf = input("Insira o CPF:\n")
#     email = input("Insira o email:\n")
#     nome = input("Insira o nome:\n")
#     endereco = input("Insira o endereco:\n")
#     tipo_pessoa = input("Insira o tipo de pessoa:\n")
#     data_nascimento[2] = input("Insira o dia da data de nascimento:\n")
#     data_nascimento[1] = input("Insira o mes da data de nascimento:\n")
#     data_nascimento[0] = input("Insira o ano da data de nascimento:\n")

#     inserir_dado = "INSERT INTO Pessoa(CPF, email, nome, endereco, tipo_pessoa, data_nascimento) VALUES("+str(cpf)+","+"'"+email+"'"+","+"'"+nome+"'"+","+"'"+endereco+"'"+","+"'"+tipo_pessoa+"'"+","+"'"+str(data_nascimento[0])+"-"+str(data_nascimento[1])+"-"+str(data_nascimento[2])+"')"

#     cursor.execute(inserir_dado)

# def exibir_todos():
#     consulta_sql = "SELECT * FROM Pessoa"
#     cursor.execute(consulta_sql)
#     linhas = cursor.fetchall()
#     print("Número total de registros retornados: ", cursor.rowcount)

#     for linha in linhas:
#         print("cpf:", linha[0])
#         print("email:", linha[1])
#         print("nome:", linha[2])
#         print("endereco:", linha[3])
#         print("tipo:", linha[4])
#         print("data:", linha[5])
        
