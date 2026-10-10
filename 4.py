import csv

with open("mahsulotlar.csv", "r") as f:
    data = csv.reader(f, delimiter=",")
    mahsulotlar = list(data)
    ustunlar = mahsulotlar[0]
    print(ustunlar)

    count = 0
    for mahsulot in mahsulotlar[1:]:
        for i in range(len(ustunlar)):
            print(f"{ustunlar[i].title()}: {mahsulot[i]}")
        print("-"*20)
        count+=1
    print(f"Mahsulotlar soni: {count}")