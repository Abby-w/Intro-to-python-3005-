import csv
q3_q4List=[]
with open("q3_gte_13.csv", "r") as Third:
    with open("q4_gte_18.csv", "r") as Fourth:
        q3 = csv.reader(Third)
        rowsQ3 = list(q3)
        length_q3=len(rowsQ3)
        q3Index=0
        q4 = csv.reader(Fourth)
        rowsQ4 = list(q4)
        while q3Index< length_q3-1:
            q3Row = rowsQ3[q3Index]
            for q4Row in rowsQ4:
                if q3Row==q4Row:
                    q3_q4List+=[q3Row]
            q3Index+=1
print("3/4",q3_q4List)

q3_q4_q5List=[]
with open("q5_gte_85.csv", "r") as Fifth:
    q5 = csv.reader(Fifth)
    rowsQ5 = list(q5)
    length_q5=len(rowsQ5)
    q5Index=0
    while q5Index< length_q5-1:
        q5Row = rowsQ5[q5Index]
        for q3_q4row in q3_q4List:
            if q5Row==q3_q4row:
                q3_q4_q5List+=[q5Row]
        q5Index+=1
print("3/4/5",q3_q4_q5List)

q3_q4_q5_q6List=[]
with open("q6_gte_500.csv", "r") as Sixth:
    q6 = csv.reader(Sixth)
    rowsQ6 = list(q6)
    length_q6=len(rowsQ6)
    q6Index=0
    while q6Index< length_q6-1:
        q6Row = rowsQ6[q6Index]
        for q3_q4_q5row in q3_q4_q5List:
            if q6Row==q3_q4_q5row:
                q3_q4_q5_q6List+=[q6Row[0:1]]
        q6Index+=1
print("3/4/5/6",q3_q4_q5_q6List)

with open("test.csv", "w") as newFile:
    list=[]
    for item in q3_q4_q5_q6List:
        list+=item
    list.remove(list[0])
    listInt=[int(x) for x in list]
    print(listInt)
    for item in listInt:
        newFile.write("%s\n" % item)
