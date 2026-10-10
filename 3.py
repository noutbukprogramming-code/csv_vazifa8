import csv

with open("mahsulotlar.csv", "r") as f:
    mahsulotlar = csv.reader(f, delimiter=",")

    count = 0

    for mahsulot in mahsulotlar:
        try:
            if float(mahsulot[3]) >= 10:
                print(mahsulot)
                count+=1
        except:
            pass
    print(f"Mahsulotlar soni: {count}")