import mysql.connector
import os
import time
from classes_entidades.pessoa import Pessoa
from classes_entidades.medicamento import Medicamento
from classes_entidades.carrinho import Venda_itens
from classes_entidades.venda import Venda
import termcolor
from termcolor import colored


# Funcoes auxiliares
def limpar_tela():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')
        

        
def menu_principal():
    
    while (1):
        print(colored("BEM VINDO A", "blue", attrs=["bold"]), colored("FARMACIA", "blue", attrs=["bold"]), colored("!\nSELECIONE A OPCAO DESEJADA\n", "blue", attrs=["bold"]))
        print(colored("1- Ver produtos/Fazer compra", "yellow"))
        print(colored("2- Area do funcionario", "yellow"))
        print(colored("3- Area do cliente", "yellow"))
        print(colored("0- Sair", "yellow"))
        opcao_principal = input()
        
        
        if(opcao_principal == '1'):
            menu_ver_prod()
                    
            
        elif(opcao_principal == '2'):
            area_funcionario()
            
        elif(opcao_principal == '3'):
            pessoa.area_cliente()
        
        elif(opcao_principal == '0'):
            print("Sistema encerrado.")
            time.sleep(2)
            limpar_tela()
            break
        
        else:
            print("Opção inválida")
            time.sleep(2)
            
        limpar_tela()
                    
        

def menu_ver_prod():
    limpar_tela()
    
    print("-----------------------------------Produtos disponíveis-----------------------------------\n")
    med.listar_todos_med()
    print("\nO que você deseja: [0] Filtrar produtos    [1] Adicionar item ao carrinho    [2] Ver carrinho    [3] Finalizar compra    [4] Retirar filtro    [5]Voltar")
    
    quis_filtrar = 0
    while(1):
        op= input()
        
        if(op == '0'):
            quis_filtrar = 1
            limpar_tela()
            
            retorno = med.filtrar_medicamento()
            if(retorno == 0):      #se não possuir a categoria selecionada, então nao há como
                quis_filtrar = 0
            
        elif(op == '1'):
            carrinho.adicionar_ao_carrinho()
        
        elif(op == '2'):
            limpar_tela()
            carrinho.ver_carrinho()
            
        elif(op == '3'):
            quis_filtrar = 0
            limpar_tela()
            
            if(carrinho.carrinho_vazio() == 1):
                print("Carrinho vazio, não é possível finalizar compra")
                time.sleep(2)
            else:
                total = carrinho.subtotal_carrinho()
                cod_compra = venda.registrar_venda(total)
                carrinho.cadastrar_carrinho(cod_compra)
                time.sleep(2)

        elif(op == '4'):
            quis_filtrar = 0
        
        elif(op == '5'):
            break
            
        if(quis_filtrar == 0):
            limpar_tela()
            print("-----------------------------------Produtos disponíveis-----------------------------------\n")
            med.listar_todos_med()
            print("\nO que você deseja: [0] Filtrar produtos    [1] Adicionar item ao carrinho    [2] Ver carrinho    [3] Finalizar compra    [4]Retirar filtro    [5]Voltar")
        else:
            limpar_tela()
            print("-----------------------------------Produtos disponíveis (Filtrado)-----------------------------------\n")
            for linha in retorno:
                print("NOME:", linha[1])
                print("VALOR: ", linha[2])
                print("CATEGORIA:", linha[3])
                print("PRODUZIDO P/ MARI: ", linha[4])
                print("ESTOQUE: ",linha[5])
                print("CÓDIGO: ", linha[0])
                print("")
            print("\nO que você deseja: [0] Filtrar produtos    [1] Adicionar item ao carrinho    [2] Ver carrinho    [3] Finalizar compra    [4]Retirar filtro    [5]Voltar")
            


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
        
def area_funcionario(self):
    print("Area do funcionario")
    logado = pessoa.tenta_login()
    if(logado == 1):
        while(1):
            print(colored("1 - Gerenciar vendas\n2 - Gerenciar estoque\n3 - Gerenciar cadastros\n0 - Sair", "red"))
            opcao = input()
            if(opcao == '1'):
                venda.gerenciar_vendas()
            elif(opcao == '2'):
                gerenciar_estoque()
            elif(opcao == '3'):
                menu_pessoa()
            elif(opcao == '0'):
                break
            else:
                print("Opção inválida")
                time.sleep(2)
        
    limpar_tela()

def gerenciar_estoque(self):

    print(colored("1 - Cadastrar estoque\n2 - Filtrar produtos com menos de 5 unidades \n3 - Outras opcões de filtro\n0 - Sair", "red"))
    while(1):
        opcao = input()
        
        if (opcao == '1'): 
            med.cadastrar_medicamento()
        elif (opcao == '2'): 
            med.procurar_menos_5unid()
        elif(opcao == '3'):
            med.filtrar_medicamento()
        elif(opcao == '0'):
            return 0
        else: 
            print("Opção inválida")
            time.sleep(2)
        
        



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
    venda = Venda(conexao)
    carrinho = Venda_itens(conexao)

    # Defina a consulta SQL para criar uma tabela (substitua os campos e tipos de dados conforme necessário)
    criar_tabela_sql = """
    CREATE TABLE IF NOT EXISTS Venda (
        cod_venda INT PRIMARY KEY,
        cpf_funcionario varchar(11) NOT NULL,
        cpf_cliente varchar(11) NOT NULL,
        data_venda DATE NOT NULL,
        valor_total DECIMAL(10,2) NOT NULL,
        valor_com_desconto DECIMAL(10,2) NOT NULL,
        forma_pagamento varchar(20) NOT NULL,
        status varchar(20) NOT NULL
     )
    """

    deletar_tabela_sql = """
    DROP TABLE Venda
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
