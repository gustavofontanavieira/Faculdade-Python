import sqlite3 as connector
from Class.classes import Pessoa

try: 
    conexao = connector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    #pessoa = Pessoa(39900212819, 'Gustavo Fontana Vieira', '04-06-2004', False)
    #comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
    #    VALUES (?, ?, ?, ?)'''
#
    #cursor.execute(comando, (pessoa.cpf, pessoa.nome, pessoa.data_nascimento, pessoa.usa_oculos))
    pessoa = Pessoa(323123123, 'Yuumi Alves da Rosa', '01-11-2004', False)
    #o sqlite permite inserir um dicionário com o nome dos campos do banco de dados e seus valores da seguinte forma:
    comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
    VALUES (:cpf, :nome, :nascimento, :oculos)'''
    cursor.execute(comando, {'cpf': pessoa.cpf, 'nome': pessoa.nome, 'nascimento': pessoa.data_nascimento})
    conexao.commit()
except Exception as e:
    print(e)
finally:
    if conexao:
        cursor.close()
        conexao.close()
        print("Dados inseridos com sucesso!!!")