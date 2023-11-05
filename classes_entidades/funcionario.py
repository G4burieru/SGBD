from gerencia_sql import Gerenciamento

class Funcionario:

    # Método construtor
    def __init__(self, conexao):
        self.gerencia = Gerenciamento(conexao)


    def cria_funcionario(self, cpf_func):
        
        login = input("Defina seu login:")

        while(1):
            consulta_sql = f"SELECT * FROM Funcionario WHERE login = {login}" 
            retorno = self.gerencia.acessa_banco(consulta_sql)
            
            if(retorno == 0):
                is_fla = int(is_fla)
                break;
            else:
                print("Login já existente. Tente outro ou digite '0' para sair.")
            
            login = input()
            
            if login == 0:               
                return -1
            
        senha = input("\nDefina sua senha: ")
        
        
        comando_inserir = f"INSERT INTO Funcionario (cpf, login, senha) VALUES ('{str(cpf_func)}', {login}, {senha})"
        
        self.gerencia.acessa_banco(comando_inserir)
        
        
    def tenta_login(self):
        
        login_teste = input("Digite seu login:")

        consulta_sql = f"SELECT * FROM Funcionario WHERE login = {login_teste}"
        retorno = self.gerencia.acessa_banco(consulta_sql)
        
        if (retorno == 0):
            print("Login inexistente")
        else:
            senha_teste = input("Digite sua senha:")
            consulta_sql = f"SELECT * FROM Funcionario WHERE senha = {senha_teste}"
            retorno = self.gerencia.acessa_banco(consulta_sql)
            
            if(retorno == 0):
                print("Senha incorreta")
            else:
                return 1
        
        return -1
                
        
        
            