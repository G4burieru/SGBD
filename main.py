from dotenv import load_dotenv
load_dotenv()
import MySQLdb
import os
import time
from pessoa import Pessoa



# Funcoes auxiliares
def limpar_tela():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def menu():

    while (1):
        print("BEM VINDO A FARMACIA!\nSELECIONE A OPCAO DESEJADA\n")
        print("1 - Inserir pessoa\n2 - Ver todas pessoas cadastradas\n3 - Excluir pessoa\n4 - Pesquisar por nome\n5 - Editar pessoa\n6 - Exibir uma pessoa\n0 - Sair\n")
        opcao = input()
        pessoa1 = Pessoa(conexao)
        cursor = conexao.cursor()

        if opcao == "1":
            comando = pessoa1.inserir_pessoa()
            if not comando == -1:
                cursor.execute(comando)

        elif opcao == "2":
            pessoa1.exibir_todos(cursor)

        elif opcao == "3":
            cpf = input("Digite o CPF que deseja deletar: ")
            validacao = pessoa1.verifica_cpf(cpf)

            if not validacao:
                print("Digite um CPF valido.\n")
                time.sleep(2)

            else:
                pessoa1.deletar_pessoa(cursor, cpf) 
            

        elif opcao == "4":
            nome = input("Digite o nome a ser procurado: ").lower()
            pessoa1.procurar_nome(cursor, nome)
            

        elif opcao == "5":
            retorno = pessoa1.editar_pessoa(cursor)

            if retorno == -1:
                print('CPF procurado não está cadastrado ou é inválido')
            else:
                conexao.commit()
                print('Campo alterado com sucesso!')

            time.sleep(3)

        elif opcao == "6":
            retorno = pessoa1.exibir_um(cursor)

            if retorno == -1:
                print('CPF procurado não está cadastrado ou é inválido')
                time.sleep(4)

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
usuario = "8koc3z6iqux0at05np9p"
senha = "pscale_pw_WmzRrdTny8d8lDgnnG7iNPazSzsGjriqK7WNM4klVbv"
banco_de_dados = "farmacia"

# Conectar ao banco de dados
print("Conectando...")
conexao = MySQLdb.connect(
  host= os.getenv("DB_HOST"),
  user=os.getenv("DB_USERNAME"),
  passwd= os.getenv("DB_PASSWORD"),
  db= os.getenv("DB_NAME"),
  autocommit = True,
  ssl_mode = "VERIFY_IDENTITY",
  ssl= {
    "ca": "/etc/ssl/cert.pem"
  }
)


if conexao.is_connected():
    print("Conectado ao banco de dados!")
    cursor = conexao.cursor()

    # Defina a consulta SQL para criar uma tabela (substitua os campos e tipos de dados conforme necessário)
    criar_tabela_sql = """
    CREATE TABLE IF NOT EXISTS Pessoa (
        CPF CHAR(11) PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        data_nascimento DATE NOT NULL,
        estado VARCHAR(255) NOT NULL,
        cidade VARCHAR(255) NOT NULL,
        bairro VARCHAR(255) NOT NULL,
        rua VARCHAR(255) NOT NULL,
        numero INT NOT NULL,
        tipo_pessoa VARCHAR(255) NOT NULL
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
    # conexao.commit() #LEMBRAR DE VER ESSE COMMIT PQ SO ENVIA PRA O BANCO AS COISAS COM ELE, TALVEZ SEJA INTERESSANTE COLOCAR EM TODA FUNCAO
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
