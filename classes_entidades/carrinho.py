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
                            
            
            qtd_med = input("Qual a quantidade do item que você deseja adicionar ao carrinho? ")
            qtd_med = int(qtd_med)
            consulta_sql = f"SELECT quantidade FROM Medicamento WHERE cod_medicamento = {int(cod_med)}"
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
    
    def cadastrar_carrinho(self, cod_venda):
        
        for item in self.carrinho:
            
            cod_item = item[0]
            qtd_item = item[1]
        
            comando_inserir = f"INSERT INTO Carrinho (cod_venda, cod_medicamento, quantidade) VALUES \
                            ({int(cod_venda)}, '{cod_item}', {qtd_item})"
                          
            self.gerencia.acessa_banco(comando_inserir)         #insere o item na tabela de carrinho
            
            consulta_sql = f"SELECT quantidade FROM Medicamento WHERE cod_medicamento = {cod_item}"
            quantidade_disp = self.gerencia.acessa_banco(consulta_sql)
            quantidade_nova = int(quantidade_disp[0][0]) - int(qtd_item)
            atualiza_estoque = f"UPDATE Medicamento SET quantidade = {quantidade_nova} WHERE cod_medicamento = '{cod_item}';"
                          
            self.gerencia.acessa_banco(atualiza_estoque)    #atualiza o estoque de medicamentos, sabendo que o item foi comprado
            
    def subtotal_carrinho(self): 
        
        valor_total = 0
        
        for item in self.carrinho: 
            consulta_sql = f"SELECT valor from Medicamento WHERE cod_medicamento = {int(item[0])}" 
            valor_unid = self.gerencia.acessa_banco(consulta_sql)
            valor_total += int(item[1]) * float(valor_unid[0][0])
            
        return valor_total
                          
    def carrinho_vazio(self):
        
        if(len(self.carrinho) == 0):
            return 1
        else:
            return 0
                