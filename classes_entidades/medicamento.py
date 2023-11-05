import time
from gerencia_sql import Gerenciamento
from termcolor import colored


TITLECOLOR = "blue"
TEXTCOLOR = "yellow"

class Medicamento:

    # Método construtor
    def __init__(self, conexao):
        self.gerencia = Gerenciamento(conexao)
        pass
    
    def cadastrar_medicamento(self):   #alterei
        
        print(colored("Insira o código do medicamento a ser cadastrado:", TITLECOLOR))
        codigo_med = input()
        
        #comando sql ####################################################
        consulta_sql = f"SELECT * FROM Medicamento WHERE cod_medicamento = {codigo_med}"
        retorno = self.gerencia.acessa_banco(consulta_sql)
        ###################################################3

        if(retorno != 0): #se o codigo foi encontrado no banco de dados
            print("\nMedicamento já cadastrado no banco de dados! Retornando ao menu...\n")
            return -2
        
        print(colored("Insira o nome do medicamento a ser cadastrado:", TITLECOLOR))
        nome_med = input().lower()
        
        print(colored("Insira o valor do medicamento a ser cadastrado:", TITLECOLOR))
        valor_med = input()
        valor_med = float(valor_med)
        
        print(colored("Insira a categoria do medicamento a ser cadastrado:", TITLECOLOR))
        array_classificacao = ['Anti-inflamatorio', 'Calmantes', 'Pressao alta', 'Gastrite', 'Colesterol', 'Anti-alergicos', 'Antidepressivos', 'Outros']
        print(colored("1- Anti-inflamatorios\n2- Calmantes\n3- Pressao alta\n4- Gastrite\n5- Colesterol\n6- Anti-alergicos\n7- Antidepressivos\n8- Outros", TEXTCOLOR))
        cat_med = input()
        cat_med = array_classificacao[int(cat_med)-1]
        
        
        print(colored("A producao do medicamento é feita por Mari?", TITLECOLOR))
        print("[0]- Não\n[1]- Sim")
        prod_mari = input()
        
        if(prod_mari == '1'):
            prod_mari = 'Sim'
        else:
            prod_mari = 'Não'
        
        print(colored("Quantidade do medicamento a ser cadastrado no estoque: ", TITLECOLOR))
        qtd_med = input();
        qtd_med = int(qtd_med)
        
        comando_inserir = f"INSERT INTO Medicamento (cod_medicamento, nome, valor, categoria, produzido_mari, quantidade) VALUES \
                          ('{codigo_med}', '{nome_med}', {valor_med}, '{cat_med}', '{prod_mari}', {qtd_med})"

        self.gerencia.acessa_banco(comando_inserir)
        print("Medicamento cadastrado com sucesso!\n")
        input("Pressione ENTER para continuar...")
         

    def editar_medicamento(self):

        print(colored("Digite o código do medicamento que você deseja alterar: ", TITLECOLOR))
        cod_med_alterado= input()

        consulta_sql = f"SELECT * FROM Medicamento WHERE cod_medicamento = {cod_med_alterado}"
        retorno = self.gerencia.acessa_banco(consulta_sql)

        if retorno == 0:  # se não teve nenhum cpf encontrado, nao será possivel alterar
            print('Medicamento não cadastrado')
            time.sleep(3)
            return -1
        else:
            print(colored('\nQual campo da tabela você deseja alterar? ', TITLECOLOR))
            print(colored('0 - nome\n1- valor\n2 - categoria\n3 - produzido em Mari\n4 - quantidade\n5 - VOLTAR AO MENU\n', TEXTCOLOR))

            opcao = input()

            if(opcao == '5'):
                return 0

            elif(opcao == '0'):
                print(colored('Digite o novo valor do campo nome: ', TITLECOLOR))
                campo_subs = input()
                update_sql = f"UPDATE Medicamento SET nome = '{campo_subs}' WHERE cod_medicamento = {int(cod_med_alterado)};"

            elif(opcao == '1'):

                print(colored('Digite o novo valor para o medicamento: ', TITLECOLOR))
                campo_subs = input()
                update_sql = f"UPDATE Medicamento SET valor = '{campo_subs}' WHERE cod_medicamento = {int(cod_med_alterado)};"


            elif(opcao == '2'):
                print(colored('Digite o novo valor do campo categoria:', TITLECOLOR))
                array_classificacao = ['Anti-inflamatorio', 'Calmantes', 'Pressao alta', 'Gastrite', 'Colesterol', 'Anti-alergicos', 'Antidepressivos', 'Outros']
                print(colored("1- Anti-inflamatorios\n2- Calmantes\n3- Pressao alta\n4- Gastrite\n5- Colesterol\n6- Anti-alergicos\n7- Antidepressivos\n8-Outros", TEXTCOLOR))
                campo_subs = input()
                campo_subs = array_classificacao[int(campo_subs)-1]
                update_sql = f"UPDATE Medicamento SET categoria = '{campo_subs}' WHERE cod_medicamento = {int(cod_med_alterado)};"

            elif(opcao == '3'):
                print(colored('Digite o novo valor do campo feito em Mari: ', TITLECOLOR))
                print(colored("[0]- Não\n[1]- Sim", TEXTCOLOR))
                campo_subs = input()

                if(campo_subs == '1'):
                    campo_subs = 'Sim'
                else:
                    campo_subs = 'Não'
                update_sql = f"UPDATE Medicamento SET produzido_mari = '{campo_subs}'WHERE cod_medicamento = {int(cod_med_alterado)};"
                
            
            elif(opcao == '4'):
                
                print(colored('Digite o novo valor do campo quantidade: ', TITLECOLOR))
                campo_subs = input()
                update_sql = f"UPDATE Medicamento SET quantidade = '{campo_subs}' WHERE cod_medicamento = {int(cod_med_alterado)};"
                
            
            self.gerencia.acessa_banco(update_sql)
            print("Alteração realizada com sucesso!")
            time.sleep(3)





    def filtrar_medicamento(self):
        
        print(colored("Filtrar medicamentos:", TITLECOLOR))
        print(colored("1- Nome \n2- Faixa de preço\n3- Categoria\n4- Produzidos por Mari", TEXTCOLOR))
        opcao = input()
        consulta_sql = ''
        
        if opcao == "1":  #nome
            
            print(colored("Insira o nome do medicamento a ser procurado:", TITLECOLOR))
            nome_med = input().lower()
            
            #comando sql ####################################################
            consulta_sql = f"SELECT * FROM Medicamento WHERE nome = '{nome_med}'"
            

        elif opcao == "2": #faixa de valor
            
            print(colored("Insira o valor mínimo que o medicamento procurado pode ter:", TITLECOLOR))
            valor_min = input()
            print(colored("Insira o valor máximo que o medicamento procurado pode ter:", TITLECOLOR))
            valor_max = input()
            
            #comando sql ####################################################
            consulta_sql = f"SELECT * FROM Medicamento WHERE valor >= {valor_min} AND valor <= {valor_max};"
            

        elif opcao == "3":  #categoria
            
            print(colored("Qual categoria do medicamento que voce quer procurar:", TITLECOLOR))
            print(colored("1- Anti-inflamatorios\n2- Calmantes\n3- Pressao alta\n4- Gastrite\n5- Colesterol\n6- Anti-alergicos\n7- Antidepressivos\n8-Outros", TEXTCOLOR))
            array_classificacao = ['Anti-inflamatorio', 'Calmantes', 'Pressao alta', 'Gastrite', 'Colesterol', 'Anti-alergicos', 'Antidepressivos', 'Outros']
            categoria_prod = input()
            
            #comando sql ####################################################
            consulta_sql = f"SELECT * FROM Medicamento WHERE categoria = '{array_classificacao[int(categoria_prod)-1]}'"
    
        elif opcao == "4":   #produzido por mari 
            
            print(colored("Produtos produzidos por mari:", TITLECOLOR))
            
            #comando sql ####################################################
            consulta_sql = f"SELECT * FROM Medicamento WHERE produzido_mari = 'Sim'"
            
        else:
            print("Opcão inválida")
            time.sleep(2)
            return 0
            
        retorno = self.gerencia.acessa_banco(consulta_sql)
        
        if(retorno == 0):
            print("Não temos produto com esse filtro disponível")
            time.sleep(2)
            return 0
        else: 
            return retorno
        
            
    def procurar_menos_5unid(self):
            
        consulta_sql = f"SELECT * FROM Medicamento WHERE quantidade < 5;"
            
        retorno = self.gerencia.acessa_banco(consulta_sql)
        
        if retorno == 0: 
            print('Não há nenhum medicamento com menos de 5 unidades')
        else:
            for linha in retorno:
                print(colored(("NOME:", linha[1]), TEXTCOLOR))
                print(colored(("VALOR: ", linha[2]), TEXTCOLOR))
                print(colored(("CATEGORIA:", linha[3]), TEXTCOLOR))
                print(colored(("PRODUZIDO P/ MARI: ", linha[4]), TEXTCOLOR))
                print(colored(("ESTOQUE: ",linha[5]), TEXTCOLOR))
                print(colored(("CÓDIGO: ", linha[0]), TEXTCOLOR))
                print("")

        input("\nPressione ENTER para continuar")        
        
    
    def listar_todos_med(self):         #esta funcao foi alterada
        
        consulta_sql = "SELECT * FROM Medicamento WHERE quantidade > 0"

        retorno = self.gerencia.acessa_banco(consulta_sql)
        
        if(retorno == 0): 
            print("Não há nenhum medicamento disponível")
        else:
            for linha in retorno:
                print(colored(("NOME:", linha[1]), TEXTCOLOR))
                print(colored(("VALOR: ", linha[2]), TEXTCOLOR))
                print(colored(("CATEGORIA:", linha[3]), TEXTCOLOR))
                print(colored(("PRODUZIDO P/ MARI: ", linha[4]), TEXTCOLOR))
                print(colored(("ESTOQUE: ",linha[5]), TEXTCOLOR))
                print(colored(("CÓDIGO: ", linha[0]), TEXTCOLOR))
                print("")
        
        
            
        
