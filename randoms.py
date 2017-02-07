import csv
import MySQLdb


exF = open("locations.csv")
exR = csv.reader(exF)
exD = list(exR)
print exD

db = MySQLdb.connect("localhost", "root", "2801", "addressanalysis")
cursor = db.cursor()

k = 0
for i in exD:
    if k == 0:
        pass
    else:
        if i[4] == "Delhi" or i[4] == "DELHI":
            query = 'INSERT INTO addressanalysis.addresses VALUES("' + i[0] + '","' + i[1] + '",' + i[2] + ',"' + i[3] + '","' + i[4] + '",' + str(k) + ');'
            try:
                cursor.execute(query)
                db.commit()
            except:
                print k
    k += 1

db.close()