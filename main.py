import mysql.connector
import os
import time
from classes_entidades.pessoa import Pessoa
from classes_entidades.medicamento import Medicamento
import termcolor
from termcolor import colored


# Funcoes auxiliares
def limpar_tela():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def filtrar_produtos():

    while(1):    
        print("Escolha a opcao de filtro que você quer usar:")
        print("1-Nome \n2- Faixa de preço\n3- Categoria\n4- Produzidos por Mari")
        opcao = input()
        while(1):
            med.filtrar_medicamento(opcao)
            filtrar_dnv = input("Pressione '1' para filtrar novamente ou '0' para sair") 
            
            if(filtrar_dnv == 1):
                limpar_tela()
                break
            else:
                limpar_tela()
                return 0;
        

        
def menu_principal():
    
    while (1):
        print(colored("BEM VINDO A", "green", attrs=["bold"]), colored("FARMACIA", "red", attrs=["bold"]), colored("!\nSELECIONE A OPCAO DESEJADA\n", "green", attrs=["bold"]))
        print(colored("1- Ver produtos", "red"))
        print(colored("2- Gerenciar cadastros", "red"))
        print(colored("3- Entrar em conta existente", "red"))
        print(colored("0- Sair", "red"))
        opcao_principal = input()
        
        
        if(opcao_principal == '1'):
            limpar_tela()
            
            print("-----------------------------------Produtos disponíveis-----------------------------------\n")
            med.listar_todos_med()
            print("\n\nGostaria de realizar uma compra? Volte ao menu principal e entre na opcao 'Fazer cadastro' ou 'Entrar em conta existente'")
            print("Digite '1' para retornar ao menu principal:")
            while(1):
                sair= input()
                
                if(sair == '1'):
                    break;
            
        if(opcao_principal == '2'):
            print("faz cadastro de cliente e funcionario")
            logado = pessoa.tenta_login()
            if(logado == 1):
                menu_pessoa()
            else:
                print("sem sucesso")
            
        if(opcao_principal == '3'):
            pessoa.area_cliente()
            time.sleep(2)
        
        if(opcao_principal == '0'):
            print("Sistema encerrado.")
            time.sleep(2)
            limpar_tela()
            break
        else:
            print("Opção inválida")
            time.sleep(2)
            
        limpar_tela()
                    
        

def menu_pessoa():

    while (1):
        limpar_tela()
        print(colored("1 - Inserir pessoa\n2 - Ver todas pessoas cadastradas\n3 - Excluir pessoa\n4 - Pesquisar por nome\
                       \n5 - Editar pessoa\n6 - Pesquisar por CPF\n7 - Gerar relatório\n0 - Sair\n", "red"))
        opcao = input()

        if opcao == "1":
            pessoa.inserir_pessoa()

        elif opcao == "2":
            pessoa.exibir_todos()

        elif opcao == "3":
            pessoa.deletar_pessoa() 
            

        elif opcao == "4":
            pessoa.procurar_nome()
            
        elif opcao == "5":
            pessoa.editar_pessoa()

        elif opcao == "6":
            pessoa.exibir_um()

        elif opcao == "7":
            pessoa.gerar_relatorio()

        elif opcao == "0":
            print("Saindo...")
            time.sleep(1)
            limpar_tela()
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
    
    #variaveis globais
    med = Medicamento(conexao)
    pessoa = Pessoa(conexao)

    # Defina a consulta SQL para criar uma tabela (substitua os campos e tipos de dados conforme necessário)
    criar_tabela_sql = """
    CREATE TABLE IF NOT EXISTS Carrinho (
        cod_medicamento INT PRIMARY KEY,
        cod_venda INT NOT NULL,
        quantidade INT NOT NULL
     )
    """

    deletar_tabela_sql = """
    DROP TABLE Carrinho
    """
    
    deletar_algo = """
    Delete FROM Pessoa, Endereco USING Pessoa INNER JOIN Endereco WHERE Pessoa.CPF = Endereco.CPF AND Pessoa.CPF='71652821490';
    """

    # Execute a consulta SQL para deletar a tabela
    # cursor.execute(deletar_tabela_sql)
    # print("Tabela deletada com sucesso")

    # Execute a consulta SQL para criar a tabela
    # cursor.execute(criar_tabela_sql)
    # print("Tabela criada com sucesso")
    
    # cursor.execute(deletar_algo)

    cursor.close()
    limpar_tela()
    menu_principal()
    conexao.close()

else:
    print("Não foi possível conectar ao banco de dados.")
