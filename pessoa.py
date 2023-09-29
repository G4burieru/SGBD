class Pessoa:
    # Variável de classe
    cpf = None
    email = None
    nome = None
    endereco = None
    tipo_pessoa = None
    data_nascimento = [None, None, None]

    # Método construtor
    def __init__(self):
        pass

    # Método para imprimir informações da pessoa
    def inserir_pessoa(self):
        
        self.cpf = input("Insira o CPF:\n")
        self.email = input("Insira o email:\n")
        self.nome = input("Insira o nome:\n")
        self.endereco = input("Insira o endereco:\n")
        self.tipo_pessoa = input("Insira o tipo de pessoa:\n")
        self.data_nascimento[2] = input("Insira o dia da data de nascimento:\n")
        self.data_nascimento[1] = input("Insira o mes da data de nascimento:\n")
        self.data_nascimento[0] = input("Insira o ano da data de nascimento:\n")
        
        comando_inserir = f"INSERT INTO Pessoa (cpf, email, nome, endereco, tipo_pessoa, data_nascimento) VALUES ({self.cpf}, '{self.email}', '{self.nome}', '{self.endereco}', '{self.tipo_pessoa}','{self.data_nascimento[0]}-{self.data_nascimento[1]}-{self.data_nascimento[2]}')"

        return comando_inserir
    
    def exibir_todos(self, qtd_cadastros, linha_cadastros):

        print("Número total de registros retornados: ", qtd_cadastros)
        
        for linha in linha_cadastros:
            print("cpf:", linha[0])
            print("email:", linha[1])
            print("nome:", linha[2])
            print("endereco:", linha[3])
            print("tipo de funcionário:", linha[4])
            print("data de nascimento:", linha[5])
            print("\n")
            
        print("Pressione ENTER para continuar...", end=" ")

