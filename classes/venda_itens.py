
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
                