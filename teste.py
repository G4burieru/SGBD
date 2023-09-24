import mysql.connector

# Configurações de conexão
host = "aws.connect.psdb.cloud"
usuario = "cbvc888azaeeqmlastk4"
senha = "pscale_pw_dhfPULoPzEv5iCuVS9APbcfLJEXsY454NrThJgcXXPs"
banco_de_dados = "farmacia"

# Conectar ao banco de dados
conexao = mysql.connector.connect(
    host=host,
    user=usuario,
    password=senha,
    database=banco_de_dados,
)

if conexao.is_connected():
    cursor = conexao.cursor()

    # Defina a consulta SQL para criar uma tabela (substitua os campos e tipos de dados conforme necessário)
    criar_tabela_sql = """
    CREATE TABLE IF NOT EXISTS HistoricoDeVenda (
        CPF INT PRIMARY KEY,
        quantidade INT NOT NULL
    )
    """

    # Execute a consulta SQL para criar a tabela
    cursor.execute(criar_tabela_sql)
    print("Tabela criada com sucesso.")

    # Feche o cursor e a conexão
    cursor.close()
    conexao.close()
else:
    print("Não foi possível conectar ao banco de dados.")
