import time
from datetime import datetime
from datetime import date

class Venda:
    # Variável de classe
    connection = None

    # Método construtor
    def __init__(self, conexao):
        self.connection = conexao
        pass
    
    def registrar_venda(self):
        
        print("CPF do funcionario responsável pela venda: ")
        cod_venda = input()
        
        print("CPF do cliente: ")
        cod_venda = input()
        
        print("Código da venda realizada: ")
        cod_venda = input()
        
        print("Data de realizacao da venda: ")
        data_venda = input()
        
        print("Valor total da compra: ")
        valor_venda = input()
        
        print("Forma de pagamento da compra: Cartao/boleto/pix/berries")
        forma_pagamento = input()
        
        print("Status de confirmacao da compra: finalizada/ em andamento")
        status_venda = input()
        
        
