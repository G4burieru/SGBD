
class Venda_itens:
    # Variável de classe
    connection = None

    # Método construtor
    def __init__(self, conexao):
        self.connection = conexao
        pass
    
    def cadastrar_itens_venda(self):
        
        print("Codigo da venda: ")
        cod_venda = input()
        
        print("Codigo do medicamento: ")
        cod_med = input()

        print("Quantidade: ")
        
    def recuperar_itens_venda(self, cod_venda):
        
        consulta_sql = f"SELECT I.*, M.nome, M.preco, M.categoria, M.classificacao FROM Venda_itens I JOIN Medicamento M \
                        ON I.cod_med = M.CodigoMedicamento WHERE I.cod_med = '{cod_venda}';"
        cursor = self.connection.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        
        if len(linhas) == 0: 
            print('alguma coisa deu errado ou nao possui dados')
        else:
            for linha in linhas:
               print(linha)
        
                