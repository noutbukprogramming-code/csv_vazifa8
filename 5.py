import csv 

qatorlar =[
    ["id", "ism", "familiya", "yosh"],
    ["1", "Ali", "Valiyev", "20" ],
    ["2", "Vali", "Qodirov", 24]
]

with open("talabalar.csv", "w", newline="") as f:
    writer = csv.writer(f)

    # for qator in qatorlar:
    #     writer.writerows(qator)

    writer.writerows(qatorlar)