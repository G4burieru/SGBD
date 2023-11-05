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
        
        comando_sql = f"SELECT * FROM Funcionario WHERE cpf = '{cpf_func}'"
        retorno = self.gerencia.acessa_banco(comando_sql)
        if(retorno == 0):
            print("Funcionario nao identificado")
            time.sleep(2)
            return -1
        
        
        print("CPF do cliente: ")
        cpf_cli = input()
        
        comando_sql = f"SELECT * FROM Cliente WHERE cpf = '{cpf_cli}'"
        retorno = self.gerencia.acessa_banco(comando_sql)
        if(retorno == 0):
            print("Cliente nao identificado")
            time.sleep(2)
            return -1
        
        
        print("Código da venda realizada: ")
        cod_venda = input()
        
        
        print("Data de realizacao da venda: ")
        data_venda = input()
        
        
        print("Valor total da compra: ")
        valor_venda = input()
        checar_desconto = f"SELECT C.is_flamengo, C.ve_onepiece, E.cidade FROM Cliente C, Endereco E WHERE C.cpf = '{cpf_cli}' AND C.cpf = E.cpf_cliente"
        retorno = self.gerencia.acessa_banco(checar_desconto)
        if(retorno[0][0] == 1):
            valor_venda = float(valor_venda) * 0.9
        elif(retorno[0][1] == 1):
            valor_venda = float(valor_venda) * 0.9
        elif(retorno[0][2] == "sousa"):
            valor_venda = float(valor_venda) * 0.9
            
        
        while(1):
            forma_pagamento = input("Forma de pagamento da compra: \n[1] Cartao \n[2] boleto \n[3] pix \n[4] berries \n[5] Voltar ao menu\n")
            match forma_pagamento:
                case '1':
                    forma_pagamento = "cartao"
                    break
                case '2':
                    forma_pagamento = "boleto"
                    break
                case '3':
                    forma_pagamento = "pix"
                    break
                case '4':
                    forma_pagamento = "berries"
                    break
                case '5':
                    return -1
                case _:
                    print("Opção inválida")
                    time.sleep(2)
                    continue
        
        
        while(1):
            status_venda = input("Status de confirmacao da compra: [1] finalizada [2] em andamento")
            match status_venda:
                case '1':
                    status_venda = "finalizada"
                    break
                case '2':
                    status_venda = "em andamento"
                    break
                case _:
                    print("Opção inválida")
                    time.sleep(2)
                    return -1
            
            
        #comando para o sql###############################################
        comando_inserir = f"INSERT INTO Venda (cpf_funcionario, cpf_cliente, codigo_venda, data, valor_total, pagamento, status) VALUES \
                          ('{cpf_func}', '{cpf_cli}', '{cod_venda}', '{data_venda}',\
                          {valor_venda}, '{forma_pagamento}', '{status_venda}')"

        self.gerencia.acessa_banco(comando_inserir)   
        ################################################################ 
    
        
