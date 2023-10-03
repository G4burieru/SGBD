import mysql.connector
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

        if opcao == "1":
            pessoa1.inserir_pessoa()

        elif opcao == "2":
            pessoa1.exibir_todos()

        elif opcao == "3":
            pessoa1.deletar_pessoa() 
            

        elif opcao == "4":
            pessoa1.procurar_nome()
            
        elif opcao == "5":
            retorno = pessoa1.editar_pessoa(cursor)
            
            if retorno == -1:
                print('CPF procurado não está cadastrado ou é inválido')
            else:
                conexao.commit()
                print('Campo alterado com sucesso!')

        elif opcao == "6":
            pessoa1.exibir_um()

        elif opcao == "0":
            print("Saindo...")
            time.sleep(1)
            break

        else:
            print("Opcao invalida, tente novamente")
            time.sleep(2)

        limpar_tela()


# Configurações de conexão
host = "aws.connect.psdb.cloud"
usuario = "0qlu6gn8jx2b99ls14um"
senha = "pscale_pw_25n9ZWqX4wE0tktkqU3KRDoRn8nQj5EHwHL9HMqzOy"
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
    # print("Tabela criada com sucesso")

    cursor.close()
    limpar_tela()
    menu()
    conexao.close()

else:
    print("Não foi possível conectar ao banco de dados.")
