
class Medicamento:
    # Variável de classe
    connection = None

    # Método construtor
    def __init__(self, conexao):
        self.connection = conexao
        pass
    
    def cadastrar_medicamento(self):
        
        print("Insira o código do medicamento a ser cadastrado:")
        codigo_med = input()
        
        print("Insira o nome do medicamento a ser cadastrado:")
        nome_med = input()
        
        print("Insira o valor do medicamento a ser cadastrado:")
        valor_med = input()
        
        print("Insira a descrição do medicamento a ser cadastrado:")
        desc_med = input()
        
        print("Insira a classificação do medicamento a ser cadastrado:")
        classif_med = input()
        
        
    def procurar_medicamento(self, opcao):
        
        if opcao == "1":  #nome
            
            print("Insira o nome do medicamento a ser procurado:")
            nome_med = input()

        elif opcao == "2": #faixa de valor
            
            print("Insira o valor mínimo que o medicamento procurado pode ter:")
            valor_min = input()
            print("Insira o valor máximo que o medicamento procurado pode ter:")
            valo_max = input()

        elif opcao == "3":  #categoria
            
            print("Qual categoria do medicamento: Anti-inflamatorio / calmantes/ pressao alta / gastrite / colesterol/ anti-alergicos / antidepressivos")
            categoria = input()
    
        elif opcao == "4":   #produzido por mari 
            
            print("Produtos produzidos por mari:")
            prod_mari = input()
            
        elif opcao == '5':  #se for um funcionario, filtrar por menos de 5 unidades disponiveis
            
            print("Produtos produzidos por mari:")
            prod_mari = input()
            
        