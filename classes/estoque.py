

class Estoque:
    # Variável de classe
    connection = None

    # Método construtor
    def __init__(self, conexao):
        self.connection = conexao
        pass
    
    def cadastrar_estoque(self):
        
        print("Codigo do medicamento que voce quer cadastrar no estoque: ")
        cod_med = input()

        print("Quantidade do medicamento a ser cadastrado no estoque: ")     
        cod_med = input();   
        
    def verificar_estoque(self, opcao):
        
        if(opcao == 'c'):
            print("codigo do medicamento a ser verificado no estoque: ")
            cod_med = input();
            
            consulta_sql = f"SELECT * FROM Estoque WHERE categoria = '{cod_med}'"
            cursor = self.connection.cursor()
            cursor.execute(consulta_sql)
            linhas = cursor.fetchall()
            
        if(opcao == 'q'):
            print("quantidade mínima a ser verificada no estoque: ")
            q_min = input();
            print("quantidade máxima a ser verificada no estoque: ")
            q_max = input();
            
            consulta_sql = f"SELECT * FROM Medicamento WHERE quantidade > {q_min} AND quantidade < {q_max};"
            cursor = self.connection.cursor()
            cursor.execute(consulta_sql)
            linhas = cursor.fetchall()
            
        if len(linhas) == 0: 
            print('alguma coisa deu errado ou nao possui dados')
        else:
            for linha in linhas:
               print(linha)
        
        