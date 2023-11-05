import time
from gerencia_sql import Gerenciamento 
import datetime
from datetime import date
import random

class Venda:

    # Método construtor
    def __init__(self, conexao):
        self.gerencia = Gerenciamento(conexao)
    
    def registrar_venda(self, total_carrinho):
        
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
    
        
        while(1):                 #gerando um codigo de venda de forma aleatoria
            cod_venda = random.randint(1,1000000)
            consulta_sql = f"SELECT * from Medicamento WHERE cod_medicamento = {cod_venda}"
            retorno = self.gerencia.acessa_banco(consulta_sql)
            if(retorno == 0): 
                break
        
        print("Código da venda realizada: ", cod_venda)
        
        data_venda = datetime.date.today()
        print("Data de realizacao da venda: ", data_venda)
        
        
        print("Valor total da compra: ", total_carrinho)
        
        checar_desconto = f"SELECT C.is_flamengo, C.ve_onepiece, E.cidade FROM Cliente C, Endereco E WHERE C.cpf = '{cpf_cli}' AND C.cpf = E.cpf"
        retorno = self.gerencia.acessa_banco(checar_desconto)
        if(retorno[0][0] == 1 or retorno[0][1] == 1 or retorno[0][2] == "sousa"):
            total_desconto = float(total_carrinho) * 0.9
            print("Valor apos desconto: ", total_desconto)
            
        
        while(1):
            forma_pagamento = input("Forma de pagamento da compra: \n[1] Cartao \n[2] boleto \n[3] pix \n[4] berries \n[5] Voltar ao menu\n")
            
            if (forma_pagamento == '1'):
                forma_pagamento = "cartao"
                break
            
            elif (forma_pagamento == '2'):
                forma_pagamento = "boleto"
                break
            elif (forma_pagamento == '3'):
                forma_pagamento = "pix"
                break
            
            elif forma_pagamento == '4':
                forma_pagamento = "berries"
                break
            
            elif forma_pagamento =='5':
                return 0
            else:
                print("Opção inválida")
                time.sleep(2)
        
        
        while(1):
            status_venda = input("Status de confirmacao da compra: [1] finalizada [2] em andamento")
            
            if(status_venda == '1'):
                status_venda = "finalizada"
                break
            elif(status_venda == '2'):
                status_venda = "em andamento"
                break
            else:
                print("Opção inválida")
                time.sleep(2)
                return -1
        
        comando_inserir = f"INSERT INTO Venda (cod_venda, cpf_funcionario, cpf_cliente, data_venda, valor_total, valor_com_desconto, forma_pagamento, status) VALUES \
                        ('{cod_venda}', '{cpf_func}', '{cpf_cli}', '{data_venda}', {total_carrinho}, {total_desconto}, '{forma_pagamento}', '{status_venda}') "
                        
        self.gerencia.acessa_banco(comando_inserir)
        
        if(status_venda == "finalizada"):
            #comando para o sql###############################################
            comando_inserir = f"INSERT INTO HistoricoDeVenda (cpf_funcionario, cpf_cliente, cod_venda, data_venda, valor_total, forma_pagamento) VALUES \
                            ('{cpf_func}', '{cpf_cli}', '{cod_venda}', '{data_venda}',\
                            {total_carrinho}, '{forma_pagamento}')"

            self.gerencia.acessa_banco(comando_inserir)   
            ################################################################ 
        
        print("Compra efetivada!")
        return cod_venda
    
    
    def consultar_todas_vendas(self):
        comando_sql = f"SELECT * FROM Venda"
        retorno = self.gerencia.acessa_banco(comando_sql)
        if(retorno == 0):
            print("Nao ha vendas registradas")
            time.sleep(2)
            return -1
        
        for i in range(len(retorno)):
            print("Codigo da venda: ", retorno[i][0])
            print("CPF do funcionario responsavel: ", retorno[i][1])
            print("CPF do cliente: ", retorno[i][2])
            print("Data da venda: ", retorno[i][3])
            print("Valor total da compra: ", retorno[i][4])
            print("Valor com desconto: ", retorno[i][5])
            print("Forma de pagamento: ", retorno[i][6])
            print("Status da venda: ", retorno[i][7])
            print("\n")
        
        input("Pressione enter para continuar")
        
    def finalizar_venda(self):
        print("Digite o codigo da venda: ")
        cod_venda = input()
        
        comando_sql = f"SELECT * FROM Venda WHERE cod_venda = '{cod_venda}'"
        retorno = self.gerencia.acessa_banco(comando_sql)
        if(retorno == 0):
            print("Venda nao identificada")
            time.sleep(2)
            return -1
        
        if(retorno[0][7] == "finalizada"):
            print("Venda já finalizada")
            time.sleep(2)
            return -1
        else:
            comando_sql = f"UPDATE Venda SET status = 'finalizada' WHERE cod_venda = '{cod_venda}'"
            self.gerencia.acessa_banco(comando_sql)
            comando_sql = f"INSERT INTO HistoricoDeVenda (cpf_funcionario, cpf_cliente, cod_venda, data_venda, valor_total, forma_pagamento) VALUES \
                            ('{retorno[0][1]}', '{retorno[0][2]}', '{cod_venda}', '{retorno[0][3]}', {retorno[0][5]}, '{retorno[0][6]}')"
            self.gerencia.acessa_banco(comando_sql)
            print("Venda finalizada!")
            time.sleep(2)
            
    def gerar_relatorio_vendas(self):
        
        consulta_sql = "SELECT * FROM HistoricoDeVenda"
        retorno = self.gerencia.acessa_banco(consulta_sql)
        
        qtd_vendas = len(retorno)
        
        try:
            with open('relatorio_vendas.txt', 'w') as arquivo:
                
                arquivo.write("Relatorio de vendas\n")
                arquivo.write(f"Quantidade de vendas: {qtd_vendas}\n")
                
                for linhas in retorno:
                    arquivo.write(f"Codigo da venda: {linhas[0]}\n")
                    arquivo.write(f"CPF do funcionario: {linhas[1]}\n")
                    arquivo.write(f"CPF do cliente: {linhas[2]}\n")
                    arquivo.write(f"Data da venda: {linhas[3]}\n")
                    arquivo.write(f"Valor total da compra: {linhas[4]}\n")
                    arquivo.write(f"Forma de pagamento: {linhas[5]}\n")
                    arquivo.write("\n")
            
            print("Relatorio gerado com sucesso!")
            time.sleep(2)
            
        except IOError as e:
            print("Erro ao gerar relatorio de vendas")
            print(e)
            time.sleep(2)
            
    def gerenciar_vendas(self):
        
        while(1):
            print("Gerenciamento de vendas")
            print("[1] Consultar todas as vendas")
            print("[2] Finalizar venda")
            print("[3] Gerar relatorio de vendas")
            print("[4] Gerar relatorio mensal funcionario")
            print("[5] Voltar ao menu principal")
            
            opcao = input()

            if(opcao == '1'):
                self.consultar_todas_vendas()
            elif(opcao == '2'):
                self.finalizar_venda()
            elif(opcao == '3'):
                self.gerar_relatorio_vendas()
            elif(opcao == '4'):
                self.gerar_relatorio_funcionario()
            elif(opcao == '5'):
                return 0
            else:
                print("Opção inválida")
                time.sleep(2)

    def gerar_relatorio_funcionario(self):
        cpf = input("Digite o cpf do funcionario: ")
        
        comando_sql = f"SELECT * FROM Funcionario WHERE cpf = '{cpf}'"
        retorno = self.gerencia.acessa_banco(comando_sql)
        if(retorno == 0):
            print("Funcionario nao identificado")
            time.sleep(2)
            return -1
        
        data_atual = datetime.date.today()
        data_atual = str(data_atual)[:-3]
        
        consulta_sql = f"SELECT * FROM HistoricoDeVenda WHERE cpf_funcionario = '{cpf}' AND data_venda BETWEEN '{data_atual}-01' AND '{data_atual}-30'"
        retorno = self.gerencia.acessa_banco(consulta_sql)
        
        qtd_vendas = len(retorno)
        
        try:
            with open(f'relatorio_{data_atual}_func_{cpf}.txt', 'w') as arquivo:
                
                arquivo.write("Relatorio de vendas\n")
                arquivo.write(f"Quantidade de vendas: {qtd_vendas}\n")
                
                for linhas in retorno:
                    arquivo.write(f"Codigo da venda: {linhas[0]}\n")
                    arquivo.write(f"CPF do funcionario: {linhas[1]}\n")
                    arquivo.write(f"CPF do cliente: {linhas[2]}\n")
                    arquivo.write(f"Data da venda: {linhas[3]}\n")
                    arquivo.write(f"Valor total da compra: {linhas[4]}\n")
                    arquivo.write(f"Forma de pagamento: {linhas[5]}\n")
                    arquivo.write("\n")
            
            print("Relatorio gerado com sucesso!")
            time.sleep(2)
            
        except IOError as e:
            print("Erro ao gerar relatorio de vendas")
            print(e)
            time.sleep(2)