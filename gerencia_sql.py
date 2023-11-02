

class Gerenciamento:
    
    # Variável de classe
    connection = None

    # Método construtor
    def __init__(self, conexao):
        self.connection = conexao
        
        
    def acessa_banco(self, consulta_requisitada):
        
        cursor = self.connection.cursor()
        cursor.execute(consulta_requisitada)
        resultado = cursor.fetchall()
        cursor.close()
        self.connection.commit()
        
        if len(resultado) == 0:
            return 0
        else:
            return resultado
        