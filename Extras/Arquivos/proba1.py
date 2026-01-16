import datetime

file = open("./test.txt")
for i in file:
    print(i)
file.close()

file2 = open("./test.txt", "a") #w = reescribe, a=agrega, r= read

actualDatetime = datetime.datetime.now()

date, hour = str(actualDatetime).split()
file2.write(date)
file2.write("\n")
file2.write(hour)
file2.write("\n")

file2.close()

try:
    file3 = open("./test.txt","r")
except FileNotFoundError as e:
    print(f"No such file:\n{e}")
else:
    for i in file3:
        print(i)
    file3.close()
finally:
    print("End")