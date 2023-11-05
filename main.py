import mysql.connector
import os
import time
from classes_entidades.pessoa import Pessoa
from classes_entidades.medicamento import Medicamento
from classes_entidades.funcionario import Funcionario
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
            
            print("Produtos disponíveis: \n")
            med.listar_todos_med()
            
            print("\n\nO que deseja fazer?")
            print("1-  Filtrar produtos      2- Comprar e não possuo cadastro      3- Comprar e possuo cadastro      0- Voltar")
           
            while(1):
                menu_ver = input()
                
                if(menu_ver == 0):
                    break
                elif(menu_ver == 1):
                    limpar_tela()
                    filtrar_produtos(med)
                    break
                elif(menu_ver == 2):
                    opcao_principal = 2
                    break
                elif(menu_ver == 3):
                    opcao_principal = 3
                    break
            
        if(opcao_principal == '2'):
            print("faz cadastro de cliente e funcionario")
            menu_pessoa()
            
        if(opcao_principal == '3'):
            #funcionario
            retorno = func.tenta_login()
            if(retorno == -1):
                print("sem sucesso")
            
            print("se for cliente deve poder listar seus dados e pedidos")
            time.sleep(2)
        
        if(opcao_principal == '0'):
            print("Sistema encerrado.")
            time.sleep(2)
            break
        else:
            print("Opção inválida")
            time.sleep(2)
            
        limpar_tela()
                    
        

def menu_pessoa():

    while (1):
        limpar_tela()
        print(colored("1 - Inserir pessoa\n2 - Ver todas pessoas cadastradas\n3 - Excluir pessoa\n4 - Pesquisar por nome\
                       \n5 - Editar pessoa\n6 - Exibir uma pessoa\n7 - Gerar relatório\n0 - Sair\n", "red"))
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

#variaveis globais
med = Medicamento()
func = Funcionario()

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
    CREATE TABLE IF NOT EXISTS Medicamento (
        cod_medicamento INT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        valor DOUBLE(5,2) NOT NULL,
        descricao VARCHAR(512) NOT NULL,
        classificacao VARCHAR(255) NOT NULL,
        quantidade INT NOT NULL
     )
    """

    deletar_tabela_sql = """
    DROP TABLE Medicamento
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
