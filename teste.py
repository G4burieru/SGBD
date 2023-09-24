import mysql.connector

# Configurações de conexão
host = "containers-us-west-55.railway.app"
usuario = "root"
senha = "xQK8S0BPC2RIbDBoOZbd"
banco_de_dados = "railway"
porta = "6684"

# Conectar ao banco de dados
conexao = mysql.connector.connect(
    host=host,
    user=usuario,
    password=senha,
    database=banco_de_dados,
    port=porta
)

if conexao.is_connected():
    cursor = conexao.cursor()

    # Defina a consulta SQL para criar uma tabela (substitua os campos e tipos de dados conforme necessário)
    criar_tabela_sql = """
    CREATE TABLE IF NOT EXISTS sua_tabela (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255),
        idade INT
    )
    """

    # Execute a consulta SQL para criar a tabela
    # cursor.execute(criar_tabela_sql)
    # print("Tabela criada com sucesso.")

    # Feche o cursor e a conexão
    cursor.close()
    conexao.close()
else:
    print("Não foi possível conectar ao banco de dados.")
