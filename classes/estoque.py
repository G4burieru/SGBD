

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
        
    def verificar_estoque(self):
        
        print("codigo do medicamento a ser verificado no estoque: ")
        cod_med = input();
        