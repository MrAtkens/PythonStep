from dbHealper import print_from_data, create_table, add_weather
import sqlite3 as db

conn = db.connect('library.sqlite')
cu = conn.cursor()

create_table(cu, conn)

# Nur-Sultan, Moscow, London
add_weather(cu, conn)

sql = "SELECT * FROM weather"
cu.execute(sql)
data = cu.fetchall()

# K, F, C
print_from_data(data)

cu.close()
conn.close()