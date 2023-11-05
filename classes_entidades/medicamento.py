import time
from gerencia_sql import Gerenciamento

class Medicamento:

    # Método construtor
    def __init__(self, conexao):
        self.gerencia = Gerenciamento(conexao)
        pass
    
    def cadastrar_medicamento(self):   #alterei
        
        print("Insira o código do medicamento a ser cadastrado:")
        codigo_med = input()
        
        #comando sql ####################################################
        consulta_sql = f"SELECT * FROM Medicamento WHERE cod_medicamento = {codigo_med}"
        retorno = self.gerencia.acessa_banco(consulta_sql)
        ###################################################3

        if(retorno != 0): #se o codigo foi encontrado no banco de dados
            print("\nMedicamento já cadastrado no banco de dados! Retornando ao menu...\n")
            return -2
        
        print("Insira o nome do medicamento a ser cadastrado:")
        nome_med = input()
        
        print("Insira o valor do medicamento a ser cadastrado:")
        valor_med = input()
        valor_med = float(valor_med)
        
        print("Insira a categoria do medicamento a ser cadastrado:")
        array_classificacao = ['Anti-inflamatorio', 'Calmantes', 'Pressao alta', 'Gastrite', 'Colesterol', 'Anti-alergicos', 'Antidepressivos', 'Outros']
        print("1- Anti-inflamatorios\n2- Calmantes\n3- Pressao alta\n4- Gastrite\n5- Colesterol\n6- Anti-alergicos\n7- Antidepressivos\n8-Outros")
        cat_med = input()
        cat_med = array_classificacao[int(cat_med)-1]
        
        
        print("A producao do medicamento é feita por Mari?")
        print("0 - Não             1- Sim")
        prod_mari = input()
        
        if(prod_mari == 0):
            prod_mari = 'Sim'
        else:
            prod_mari = 'Não'
        
        print("Quantidade do medicamento a ser cadastrado no estoque: ")     
        qtd_med = input();
        qtd_med = int(qtd_med)
        
        comando_inserir = f"INSERT INTO Medicamento (cod_medicamento, nome, valor, categoria, produzido_mari, quantidade) VALUES \
                          ('{codigo_med}', '{nome_med}', {valor_med}, '{cat_med}', '{prod_mari}', {qtd_med})"

        self.gerencia.acessa_banco(comando_inserir)
        print("Medicamento cadastrado com sucesso!\n")
        input("Pressione ENTER para continuar...")
         
    def filtrar_medicamento(self, opcao):
        
        if opcao == "1":  #nome
            
            print("Insira o nome do medicamento a ser procurado:")
            nome_med = input()
            
            #comando sql ####################################################
            consulta_sql = f"SELECT * FROM Medicamento WHERE nome = '{nome_med}'"
            

        elif opcao == "2": #faixa de valor
            
            print("Insira o valor mínimo que o medicamento procurado pode ter:")
            valor_min = input()
            print("Insira o valor máximo que o medicamento procurado pode ter:")
            valor_max = input()
            
            #comando sql ####################################################
            consulta_sql = f"SELECT * FROM Medicamento WHERE preco >= {valor_min} AND preco <= {valor_max};"
            

        elif opcao == "3":  #categoria
            
            print("Qual categoria do medicamento que voce quer procurar:")
            print("1- Anti-inflamatorios\n2- Calmantes\n3- Pressao alta\n4- Gastrite\n5- Colesterol\n6- Anti-alergicos\n7- Antidepressivos\n 8-Outros")
            categoria_prod = input()
            
            #comando sql ####################################################
            consulta_sql = f"SELECT * FROM Medicamentos WHERE categoria = '{categoria_prod}'"
    
        elif opcao == "4":   #produzido por mari 
            
            print("Produtos produzidos por mari:")
            
            #comando sql ####################################################
            consulta_sql = f"SELECT * FROM Medicamentos WHERE producao_mari = True"
            
            
        retorno = self.gerencia.acessa_banco(consulta_sql)
        
        if retorno == 0: 
            print('alguma coisa deu errado ou nao possui dados')
        else:
            for linha in retorno:
               print(linha)   
        
            
            
    def procurar_menos_5unid(self):
            
        consulta_sql = f"SELECT M.*, E.Quantidade FROM Medicamento M JOIN Estoque E ON M.codigo_med = E.codigo_med WHERE E.Quantidade < 5;"
            
        retorno = self.gerencia.acessa_banco(consulta_sql)
        
        if retorno == 0: 
            print('alguma coisa deu errado ou nao possui dados')
        else:
            for linha in retorno:
               print(linha)

        input("Pressione ENTER para continuar...")    
        
    
    def listar_todos_med(self):         #esta funcao foi alterada
        
        consulta_sql = "SELECT * FROM Medicamento WHERE quantidade > 0"

        retorno = self.gerencia.acessa_banco(consulta_sql)
        
        if(retorno == 0): 
            print("Não há nenhum medicamento disponível")
        else:
            for linha in retorno:
                print("NOME:", linha[1])
                print("VALOR: ", linha[2])
                print("CATEGORIA:", linha[3])
                print("PRODUZIDO P/ MARI: ", linha[4])
                print("ESTOQUE: ",linha[5])
                print("CÓDIGO: ", linha[0])
                print("")
        
        
            
        
