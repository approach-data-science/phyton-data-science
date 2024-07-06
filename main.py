import mysql.connector
import csv


connection = mysql.connector.connect(
    host='localhost',
    port=3307,
    user='root',
    password='Andrea_1204',
    database='mvsc_students'
)

query = ''' SELECT id, nombre, correo FROM students ORDER BY nombre'''

cursor = connection.cursor()
cursor.execute(query)

results = cursor.fetchall();
cursor.close()
connection.close()


with open('./csvs/salida.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'nombre', 'correo'])
    writer.writerows(results)

print('-'*70)

print('Numero de registros: ', len(results), "\n")
for ele in results:
    print(ele)




