
import psycopg2
import time


def conexaoComBd():
    try:               # a porta pode ser colocada separada do host no formato `port=5432`
        con = psycopg2.connect(database='postgres',user='postgres',host='localhost:5432')
        cur = con.cursor()                                                          # , passsword='senha'
        sql = 'SELECT * FROM Source;' # ou mude para o nome da sua tabela
        cur.execute(sql)
    except Exception as e:
        print("Erro:", e)
  

for i in range(100):
    conexaoComBd()
    time.sleep(720) # 12 minutos
    i = i + 1
