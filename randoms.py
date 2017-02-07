import csv
import MySQLdb


exF = open("locations.csv")
exR = csv.reader(exF)
exD = list(exR)
print exD

db = MySQLdb.connect("host", "username", "password", "schema_name")
cursor = db.cursor()

k = 0
for i in exD: //My Database had 6 fields and first were 5 filled by csv columns (record held by variable 'i'), change accordingly.
    if k == 0:
        pass
    else: //table already exists, else execute a create table query first.
        query = 'INSERT INTO schema_name.table_name VALUES("' + i[0] + '","' + i[1] + '",' + i[2] + ',"' + i[3] + '","' + i[4] + '",' + str(k) + ');'
        try:
            cursor.execute(query)
            db.commit()
        except:
            print k
    k += 1

db.close()
