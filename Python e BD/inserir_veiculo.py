import sqlite3 as conector
from Class.classes import Marca, Veiculo

try:
    conexao = conector.connect("./meu_banco.db")

    #somente o sqlite tem essa limitação de precisar dizer que vamos utilizar foreign_keys
    conexao.execute("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()

    # Inserção de dados na tabela Marca
    comando1 = '''INSERT INTO Marca (nome, sigla) VALUES (:nome, :sigla);'''

    marca1 = Marca(1, "Marca A", "MA")
    cursor.execute(comando1, vars(marca1))

    #pega o ultimo id dentro do bd
    marca1.id = cursor.lastrowid

    marca2 = Marca(2, "Marca B", "MB")
    cursor.execute(comando1, vars(marca2))
    marca2.id = cursor.lastrowid


    # Inserção de dados na tabela Veiculo
    comando2 = '''INSERT INTO Veiculo
                   VALUES (:placa, :ano, :cor, :motor, :proprietario, :marca);'''
    veiculo1 = Veiculo("AAA0001", 2001, "Prata", 1.0, 39900212819, marca1.id)
    veiculo2 = Veiculo("BAA0002", 2002, "Preto", 1.4, 39900212819, marca1.id)
    veiculo3 = Veiculo("CAA0003", 2003, "Branco", 2.0, 12345678900, marca2.id)
    veiculo4 = Veiculo("DAA0004", 2004, "Azul", 2.2, 12345678900, marca2.id)
    cursor.execute(comando2, vars(veiculo1))
    cursor.execute(comando2, vars(veiculo2))
    cursor.execute(comando2, vars(veiculo3))
    cursor.execute(comando2, vars(veiculo4))

    # Efetivação do comando
    conexao.commit()

except Exception as e:
    print(e)
finally:
    if conexao:
        cursor.close()
        conexao.close()
        print("Dados inseridos com sucesso!!!")