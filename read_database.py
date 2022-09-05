import pyodbc

dados_conexao = ('Driver={SQLite3 ODBC Driver};'
                 'Server=localhost;'
                 'Database=chinook.db;')

conexao = pyodbc.connect(dados_conexao)
print('Conexão Bem Sucedida')

cursor = conexao.cursor()
print('Cursor criado com sucesso')

cursor.execute('select * from customers')
descricao = cursor.description
valores = cursor.fetchall()

cursor.close()

conexao.close()
