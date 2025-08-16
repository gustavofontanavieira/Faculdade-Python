import sqlite3 as conector
 
  # Abertura de conexão e aquisição de cursor
try:
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()
    # Execução de um comando: SELECT... CREATE ...
    comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
        VALUES (12345678900, 'João', '2000-01-31', 1);'''

    cursor.execute(comando)
    conexao.commit()
except Exception as e:
    print(e)
