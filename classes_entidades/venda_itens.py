from gerencia_sql import Gerenciamento

class Venda_itens:
    
    # Método construtor
    def __init__(self, conexao):
        self.gerencia = Gerenciamento(conexao)
    
    def cadastrar_itens_venda(self):
        
        print("Codigo da venda: ")
        cod_venda = input()
        
        print("Codigo do medicamento: ")
        cod_med = input()

        print("Quantidade: ")
        qtd_med = input()
        
        comando_inserir = f"INSERT INTO Venda_itens (codigo_venda, codigo_med, quantidade) VALUES \
                          ('{cod_venda}', '{cod_med}', {qtd_med})"
                          
        self.gerencia.acessa_banco(comando_inserir)
                          
        
    def recuperar_itens_venda(self, cod_venda):
        
        consulta_sql = f"SELECT I.*, M.nome, M.preco, M.categoria, M.classificacao FROM Venda_itens I JOIN Medicamento M \
                        ON I.cod_med = M.CodigoMedicamento WHERE I.cod_med = '{cod_venda}';"
        
        retorno = self.gerencia.acessa_banco(consulta_sql)
        
        if retorno == 0: 
            print('alguma coisa deu errado ou nao possui dados')
        else:
            for linha in retorno:
               print(linha)
        
                