import csv

with open("mahsulotlar.csv", "r") as f:
    mahsulotlar = csv.reader(f, delimiter=",")

    for mahsulot in mahsulotlar:
        try:
            if float(mahsulot[3]) >= 10:
                print(mahsulot)
        except:
            pass