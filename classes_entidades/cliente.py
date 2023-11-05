from gerencia_sql import Gerenciamento

class Cliente:

    # Método construtor
    def __init__(self, conexao):
        self.gerencia = Gerenciamento(conexao)


    def cria_cliente(self, cpf_cli):
        
        is_op = input("Você assiste o anime 'One Piece'?")
        print("0 - Não        1- Sim")
        while(1):
            
            if(is_op == '1' or is_op == '2'):
                is_op = int(is_op)
                break
            is_op = input()
            
        
        is_fla = input("Você torce para o Flamengo?")
        print("0 - Não        1- Sim")
        while(1):
            
            if(is_fla == '1' or is_fla == '2'):
                is_fla = int(is_fla)
                break;
            
            is_fla = input()
        
        
        comando_inserir = f"INSERT INTO Cliente (cpf, ve_op, flamenguista) VALUES ('{str(cpf_cli)}', {is_op}, {is_fla})"
        
        self.gerencia.acessa_banco(comando_inserir)
        