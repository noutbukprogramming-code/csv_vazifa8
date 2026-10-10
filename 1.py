import csv

with open("mahsulotlar.csv", "r") as f:
    mahsulotlar = csv.reader(f, delimiter=",")

    for mahsulot in mahsulotlar:
        print(mahsulot)