import mysql.connector
import os
import time
from classes_entidades.pessoa import Pessoa



# Funcoes auxiliares
def limpar_tela():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')
        
        
def menu_principal():
    
    while (1):
        print("BEM VINDO A FARMACIA!\nSELECIONE A OPCAO DESEJADA\n")
        print("1- Ver produtos")
        print("2- Fazer novo cadastro")
        print("3- Entrar em conta existente")
        print("0- Sair")
        opcao_principal = input()
        
        if(opcao_principal == '1'):
            print("aqui deveria ver os produtos")
            time.sleep(2)
            
        elif(opcao_principal == '2'):
            print("fazer cadastro: funcionario/cliente")
            menu_ṕessoa()
            
        elif(opcao_principal == '3'):
            print("so fazer login: funcionario/cliente")
            time.sleep(2)
        
        elif(opcao_principal == '0'):
            print("Sistema encerrado.")
            time.sleep(2)
            break
        else:
            print("Opção inválida")
            time.sleep(2)
            
        limpar_tela()
                    
        

def menu_ṕessoa():

    while (1):
        print("BEM VINDO A FARMACIA!\nSELECIONE A OPCAO DESEJADA\n")
        print("1 - Inserir pessoa\n2 - Ver todas pessoas cadastradas\n3 - Excluir pessoa\n4 - Pesquisar por nome\n5 - Editar pessoa\n6 - Exibir uma pessoa\n7 - Gerar relatório\n0 - Sair\n")
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
            pessoa1.editar_pessoa()

        elif opcao == "6":
            pessoa1.exibir_um()

        elif opcao == "7":
            pessoa1.gerar_relatorio()

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
    CREATE TABLE IF NOT EXISTS HistoricoDeVenda (
        CPF varchar(11) PRIMARY KEY,
        login VARCHAR(255) NOT NULL,
        cod_venda INT NOT NULL
     )
    """

    deletar_tabela_sql = """
    DROP TABLE HistoricoDeVenda
    """

    # Execute a consulta SQL para deletar a tabela
    # cursor.execute(deletar_tabela_sql)
    # print("Tabela deletada com sucesso")

    # Execute a consulta SQL para criar a tabela
    # cursor.execute(criar_tabela_sql)
    # print("Tabela criada com sucesso")

    cursor.close()
    limpar_tela()
    menu_principal()
    conexao.close()

else:
    print("Não foi possível conectar ao banco de dados.")
