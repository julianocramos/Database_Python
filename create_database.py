import pyodbc

print(pyodbc.drivers())

dados_conexao = ('Driver={SQLite3 ODBC Driver};'
                 'Server=localhost;'
                 'Database=chinook.db;')

conexao = pyodbc.connect(dados_conexao)
print('Conexão Bem Sucedida')

cursor = conexao.cursor()
print('Cursor criado com sucesso')


cursor.execute("""
INSERT INTO albums (Title, ArtistId)
VALUES
('Juliano Hip Hop', 4)
""")

cursor.commit()

cursor.close()

conexao.close()
