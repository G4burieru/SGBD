import time
from gerencia_sql import Gerenciamento
from datetime import datetime
from datetime import date

class Venda:

    # Método construtor
    def __init__(self, conexao):
        self.gerencia = Gerenciamento(conexao)
    
    def registrar_venda(self):
        
        print("CPF do funcionario responsável pela venda: ")
        cpf_func = input()
        
        print("CPF do cliente: ")
        cpf_cli = input()
        
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
        
        #comando para o sql###############################################
        comando_inserir = f"INSERT INTO Venda (cpf_funcionario, cpf_cliente, codigo_venda, data, valor_total, pagamento, status) VALUES \
                          ('{cpf_func}', '{cpf_cli}', '{cod_venda}', '{data_venda}',\
                          {valor_venda}, '{forma_pagamento}', '{status_venda}')"

        self.gerencia.acessa_banco(comando_inserir)   
        ################################################################ 
    
        
