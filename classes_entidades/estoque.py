from gerencia_sql import Gerenciamento

class Estoque:

    # Método construtor
    def __init__(self, conexao):
        self.gerencia = Gerenciamento(conexao)
    
    def cadastrar_estoque(self):
        
        print("Codigo do medicamento que voce quer cadastrar no estoque: ")
        cod_med = input()

        print("Quantidade do medicamento a ser cadastrado no estoque: ")     
        qtd_med = input();
        qtd_med = int(qtd_med)
          
        
        comado_inserir = f"INSERT INTO Estoque (codigo_med, quantidade) VALUES \
                          ('{cod_med}', {qtd_med})"
        
        self.gerencia.acessa_banco(comado_inserir)
        
    def verificar_estoque(self, opcao):
        
        if(opcao == 'c'):
            print("codigo do medicamento a ser verificado no estoque: ")
            cod_med = input();
            
            consulta_sql = f"SELECT * FROM Estoque WHERE codigo_med = '{cod_med}'"
           
            
        if(opcao == 'q'):
            print("quantidade mínima a ser verificada no estoque: ")
            q_min = input();
            q_min = int(q_min)
            
            print("quantidade máxima a ser verificada no estoque: ")
            q_max = input();
            q_max = int(q_max)
            
            consulta_sql = f"SELECT * FROM Medicamento WHERE quantidade >= {q_min} AND quantidade <= {q_max};"
        
        retorno = self.gerencia.acessa_banco(consulta_sql)
        
        if retorno == 0: 
            print('alguma coisa deu errado ou nao possui dados')
        else:
            for linha in retorno:
               print(linha)
        
        