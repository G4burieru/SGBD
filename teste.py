import mysql.connector

# Configurações de conexão
host = "aws.connect.psdb.cloud"
usuario = "cbvc888azaeeqmlastk4"
senha = "pscale_pw_dhfPULoPzEv5iCuVS9APbcfLJEXsY454NrThJgcXXPs"
banco_de_dados = "farmacia"

# Conectar ao banco de dados
print("Conectando...")
conexao = mysql.connector.connect(
    host=host,
    user=usuario,
    password=senha,
    database=banco_de_dados,
)

if conexao.is_connected():
    print("Conectado ao banco de dados!")
    cursor = conexao.cursor()

    # Defina a consulta SQL para criar uma tabela (substitua os campos e tipos de dados conforme necessário)
    criar_tabela_sql = """
    CREATE TABLE IF NOT EXISTS Pessoa (
        CPF BIGINT PRIMARY KEY,
        email VARCHAR(255) NOT NULL,
        nome VARCHAR(255) NOT NULL,
        endereco VARCHAR(255) NOT NULL,
        tipo_pessoa VARCHAR(255) NOT NULL,
        data_nascimento DATE NOT NULL
    )
    """
    
    deletar_tabela_sql = """
    DROP TABLE Pessoa
    """

    # Execute a consulta SQL para deletar a tabela
    # cursor.execute(deletar_tabela_sql)
    # print("Tabela deletada com sucesso")
    
    # Execute a consulta SQL para criar a tabela
    # cursor.execute(criar_tabela_sql)
    # print("Tabela criada com sucesso.")

else:
    print("Não foi possível conectar ao banco de dados.")
    

cpf = ""
email = ""
nome = ""
endereco = ""
tipo_pessoa = ""
data_nascimento = ["","",""]

def inserir_pessoa():
    cpf = input("Insira o CPF:\n")
    email = input("Insira o email:\n")
    nome = input("Insira o nome:\n")
    endereco = input("Insira o endereco:\n")
    tipo_pessoa = input("Insira o tipo de pessoa:\n")
    data_nascimento[2] = input("Insira o dia da data de nascimento:\n")
    data_nascimento[1] = input("Insira o mes da data de nascimento:\n")
    data_nascimento[0] = input("Insira o ano da data de nascimento:\n")

    inserir_dado = "INSERT INTO Pessoa(CPF, email, nome, endereco, tipo_pessoa, data_nascimento) VALUES("+str(cpf)+","+"'"+email+"'"+","+"'"+nome+"'"+","+"'"+endereco+"'"+","+"'"+tipo_pessoa+"'"+","+"'"+str(data_nascimento[0])+"-"+str(data_nascimento[1])+"-"+str(data_nascimento[2])+"')"

    cursor.execute(inserir_dado)

def exibir_todos():
    consulta_sql = "SELECT * FROM Pessoa"
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()
    print("Número total de registros retornados: ", cursor.rowcount)

    for linha in linhas:
        print("cpf:", linha[0])
        print("email:", linha[1])
        print("nome:", linha[2])
        print("endereco:", linha[3])
        print("tipo:", linha[4])
        print("data:", linha[5])
        

def menu():
    print("BEM VINDO A FARMACIA!\nSELECIONE A OPCAO DESEJADA\n")
    print("1 - Inserir pessoa\n 2 - Ver todas pessoas cadastradas\n 0 - Sair\n")
    opcao = input()
    if opcao == "1":
        inserir_pessoa()
    elif opcao == "2":
        exibir_todos()
    elif opcao == "0":
        print("Saindo...")
    else:
        print("Opcao invalida, tente novamente")
        menu()

menu()
cursor.close()
conexao.commit() #LEMBRAR DE VER ESSE COMMIT PQ SO ENVIA PRA O BANCO AS COISAS COM ELE, TALVEZ SEJA INTERESSANTE COLOCAR EM TODA FUNCAO
conexao.close()