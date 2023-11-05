import time
from gerencia_sql import Gerenciamento

class Venda_itens:
    
    # Método construtor
    def __init__(self, conexao):
        self.gerencia = Gerenciamento(conexao)
        self.carrinho = []
        
        
    def adicionar_ao_carrinho(self): 
        
        existe_no_carrinho = -1
        
        cod_med = input("Qual o código do item que você deseja adicionar ao carrinho? ")
        
        consulta_sql = f"SELECT * FROM Medicamento WHERE cod_medicamento = {cod_med}"
        retorno = self.gerencia.acessa_banco(consulta_sql)
        
        if(retorno == 0):
            print("Codigo inexistente")
            time.sleep(2)
            return -1
        else:
            contador = 0
            for item in self.carrinho:         #verificando se o item ja existe no carrinho ou não
                if(cod_med == item[0]):
                    existe_no_carrinho = contador
                    break  
                contador+1
                            
            
            qtd_med = input("Qual a quantidade do item que você deseja adicionar ao carrinho?")
            qtd_med = int(qtd_med)
            consulta_sql = f"SELECT quantidade FROM Medicamento WHERE cod_medicamento = {cod_med}"
            quantidade_disp = self.gerencia.acessa_banco(consulta_sql)
            
            if(existe_no_carrinho == -1):
                
                if(qtd_med > int(quantidade_disp[0][0])):
                    print("Quantidade indisponível para ser adicionada ao carrinho")
                    time.sleep(2)
                    return -1
                else:
                    self.carrinho.append([cod_med, qtd_med])
            else:
                qtd_total_item = int(qtd_med) + int(self.carrinho[existe_no_carrinho][1])
                
                if(qtd_total_item > int(quantidade_disp[0][0])):
                    print("A quantidade exigida ultrapassou o estoque do medicamento")
                    time.sleep(2)
                    return -1
                else:
                    self.carrinho[existe_no_carrinho] = [self.carrinho[existe_no_carrinho][0], qtd_total_item]
            
        input("Item adicionado! Pressione ENTER para continuar...")


    def ver_carrinho(self):
        
        if len(self.carrinho) == 0:
            print("O carrinho está vazio!")
            time.sleep(2)
            return 0
        
        for item in self.carrinho:
            print("Codigo: ", item[0])
            consulta_sql = f"SELECT nome FROM Medicamento WHERE cod_medicamento = {item[0]}"
            retorno = self.gerencia.acessa_banco(consulta_sql)
            print("Nome: ", retorno[0])
            print("Quantidade: ", item[1])
            print("")
            
        input("Pressione ENTER para continuar...")
    
    def cadastrar_itens_venda(self):
        
        print("Codigo da venda: ")
        cod_venda = input()
        
        print("Codigo do medicamento: ")
        cod_med = input()

        print("Quantidade: ")
        qtd_med = input()
        
        comando_inserir = f"INSERT INTO Carrinho (codigo_venda, codigo_med, quantidade) VALUES \
                          ('{cod_venda}', '{cod_med}', {qtd_med})"
                          
        self.gerencia.acessa_banco(comando_inserir)
                          
        
    def recuperar_itens_venda(self, cod_venda):
        
        consulta_sql = f"SELECT I.*, M.nome, M.preco, M.categoria, M.classificacao FROM Carrinho I JOIN Medicamento M \
                        ON I.cod_med = M.CodigoMedicamento WHERE I.cod_med = '{cod_venda}';"
        
        retorno = self.gerencia.acessa_banco(consulta_sql)
        
        if retorno == 0: 
            print('alguma coisa deu errado ou nao possui dados')
        else:
            for linha in retorno:
               print(linha)
        
                