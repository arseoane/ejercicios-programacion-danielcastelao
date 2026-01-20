import csv

with open('exemplo.csv','w') as fichero:
    csvfile = csv.writer(fichero)
    csvfile.writerow(['Nome','Apelidos','Xénero'])
    csvfile.writerow(['Pedro','23','Home'])
    csvfile.writerow(['Rosa', '25', 'Muller'])

with open('exemplo2.csv','w') as fichero:
    writer = csv.writer(fichero)
    writer.writerow(['Nome', 'Apelidos', 'Xénero'])
    writer.writerow(['Pedro', '23', 'Home'])
    writer.writerow(['Rosa', '25', 'Muller'])

with open('exemplo.csv','r') as fichero:
    reader = csv.reader(fichero)
    for fila in reader:
        print(fila)