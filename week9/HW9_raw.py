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

        import csv

        with open("breastCancerData.csv", "r") as inputFile:
            with open("breastCancerDataReduced.csv", "w") as outputFile:
                writer = csv.writer(outputFile)
                for row in csv.reader(inputFile):
                    writer.writerow(row[0:6])

        #those data samples whose radius value is >= 13
        with open("breastCancerDataReduced.csv", "r") as inputFile:
            with open("q3_gte_13.csv", "w") as outputFile:
                writer = csv.writer(outputFile)
                for number,row in enumerate(csv.reader(inputFile)):
                    if number==0:
                        writer.writerow(row)
                    else:
                        if float(row[2])>=13:
                            writer.writerow(row)

        with open("q3_gte_13.csv", "r") as inputFile:
            with open("q3_B.csv", "w") as outputFile:
                writer = csv.writer(outputFile)
                for number,row in enumerate(csv.reader(inputFile)):
                    if number==0:
                        writer.writerow(row)
                    else:
                        if row[1]=="B":
                            writer.writerow(row)
        with open("q3_gte_13.csv", "r") as inputFile:
            with open("q3_M.csv", "w") as outputFile:
                writer = csv.writer(outputFile)
                for number,row in enumerate(csv.reader(inputFile)):
                    if number==0:
                        writer.writerow(row)
                    else:
                        if row[1]=="M":
                            writer.writerow(row)

        #those data samples whose texture value is >= 18
        with open("breastCancerDataReduced.csv", "r") as inputFile:
            with open("q4_gte_18.csv", "w") as outputFile:
                writer = csv.writer(outputFile)
                for number,row in enumerate(csv.reader(inputFile)):
                    if number==0:
                        writer.writerow(row)
                    else:
                        if float(row[3])>=18:
                            writer.writerow(row)

        with open("q4_gte_18.csv", "r") as inputFile:
            with open("q4_B.csv", "w") as outputFile:
                writer = csv.writer(outputFile)
                for number,row in enumerate(csv.reader(inputFile)):
                    if number==0:
                        writer.writerow(row)
                    else:
                        if row[1]=="B":
                            writer.writerow(row)
        with open("q4_gte_18.csv", "r") as inputFile:
            with open("q4_M.csv", "w") as outputFile:
                writer = csv.writer(outputFile)
                for number,row in enumerate(csv.reader(inputFile)):
                    if number==0:
                        writer.writerow(row)
                    else:
                        if row[1]=="M":
                            writer.writerow(row)

        #those data samples whose perimeter value is >= 85
        with open("breastCancerDataReduced.csv", "r") as inputFile:
            with open("q5_gte_85.csv", "w") as outputFile:
                writer = csv.writer(outputFile)
                for number,row in enumerate(csv.reader(inputFile)):
                    if number==0:
                        writer.writerow(row)
                    else:
                        if float(row[4])>=85:
                            writer.writerow(row)

        with open("q5_gte_85.csv", "r") as inputFile:
            with open("q5_B.csv", "w") as outputFile:
                writer = csv.writer(outputFile)
                for number,row in enumerate(csv.reader(inputFile)):
                    if number==0:
                        writer.writerow(row)
                    else:
                        if row[1]=="B":
                            writer.writerow(row)
        with open("q5_gte_85.csv", "r") as inputFile:
            with open("q5_M.csv", "w") as outputFile:
                writer = csv.writer(outputFile)
                for number,row in enumerate(csv.reader(inputFile)):
                    if number==0:
                        writer.writerow(row)
                    else:
                        if row[1]=="M":
                            writer.writerow(row)

        #those data samples whose area value is >= 500
        with open("breastCancerDataReduced.csv", "r") as inputFile:
            with open("q6_gte_500.csv", "w") as outputFile:
                writer = csv.writer(outputFile)
                for number,row in enumerate(csv.reader(inputFile)):
                    if number==0:
                        writer.writerow(row)
                    else:
                        if float(row[5])>=500:
                            writer.writerow(row)


        with open("q6_gte_500.csv", "r") as inputFile:
            with open("q6_B.csv", "w") as outputFile:
                writer = csv.writer(outputFile)
                for number,row in enumerate(csv.reader(inputFile)):
                    if number==0:
                        writer.writerow(row)
                    else:
                        if row[1]=="B":
                            writer.writerow(row)
        with open("q6_gte_500.csv", "r") as inputFile:
            with open("q6_M.csv", "w") as outputFile:
                writer = csv.writer(outputFile)
                for number,row in enumerate(csv.reader(inputFile)):
                    if number==0:
                        writer.writerow(row)
                    else:
                        if row[1]=="M":
                            writer.writerow(row)

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
        with open("newResult.csv", "w") as newFile:
            for item in q3_q4_q5_q6List:
                newFile.write("%s\n" % item)


        with open("breastCancerDataReduced.csv", "r") as inputFile:
            with open("SubsetMResult.csv", "w") as outputFile:
                writer = csv.writer(outputFile)
                for number,row in enumerate(csv.reader(inputFile)):
                    if number==0:
                        writer.writerow(row)
                    else:
                        if float(row[2])>=13:
                            if float(row[3])>=18:
                                if float(row[4])>=85:
                                    if float(row[5])>=500:
                                        if row[1]=="M":
                                            writer.writerow(row[0:1])
        #does not work
        #should have 39 terms
        Difference_1=[]
        with open("SubsetMResult.csv", "r") as Subset:
            with open("NewResult.csv", "r") as NewResult:
                subset = csv.reader(Subset)
                subsetRows = list(subset)
                newResult = csv.reader(NewResult)
                newResultRows = list(newResult)
                for subsetRow in subsetRows:
                    if subsetRow not in newResultRows:
                        Difference_1+=subsetRow


        #does not work
        #should have 39 terms
        Difference_1=set()
        with open("SubsetMResult.csv", "r") as Subset:
            with open("Intersection.csv", "r") as NewResult:
                subset = csv.reader(Subset)
                subsetRows = list(subset)
                length_subset=len(subsetRows)
                subsetIndex=0
                newResult = csv.reader(NewResult)
                newResultRows = list(newResult)
                while subsetIndex< length_subset-1:
                    subsetRow = subsetRows[subsetIndex]
                    for newResultRow in newResultRows:
                        if subsetRow==newResultRow:
                            Difference_1.add(subsetRow[0])
                    subsetIndex+=1
                    import csv
                    #a)
                    with open("breastCancerData.csv", "r") as inputFile:
                        with open("breastCancerDataReduced.csv", "w") as outputFile:
                            writer = csv.writer(outputFile)
                            for row in csv.reader(inputFile):
                                writer.writerow(row[0:6])

                    #those data samples whose radius value is >= 13
                    with open("breastCancerDataReduced.csv", "r") as inputFile:
                        with open("intersection.csv", "w") as outputFile:
                            writer = csv.writer(outputFile)
                            for number,row in enumerate(csv.reader(inputFile)):
                                if number==0:
                                    writer.writerow(row)
                                else:
                                    if float(row[2])>=13:
                                        if float(row[3])>=18:
                                            if float(row[4])>=85:
                                                if float(row[5])>=500:
                                                    writer.writerow(row[0:1])

                    with open("breastCancerDataReduced.csv", "r") as inputFile:
                        with open("SubsetMResult.csv", "w") as outputFile:
                            writer = csv.writer(outputFile)
                            for number,row in enumerate(csv.reader(inputFile)):
                                if number==0:
                                    writer.writerow(row)
                                else:
                                    if float(row[2])>=13:
                                        if float(row[3])>=18:
                                            if float(row[4])>=85:
                                                if float(row[5])>=500:
                                                    if row[1]=="M":
                                                        writer.writerow(row[0:1])
                    #Method 1
                    Difference_1=[]
                    with open("SubsetMResult.csv", "r") as Subset:
                        with open("intersection.csv", "r") as NewResult:
                            subset = csv.reader(Subset)
                            subsetRows = list(subset)
                            print(len(subsetRows))
                            newResult = csv.reader(NewResult)
                            newResultRows = list(newResult)
                            print(len(newResultRows))
                            for newResultRow in newResultRows:
                                if newResultRow not in subsetRows:
                                    Difference_1+=[newResultRow]
                                    Difference_1.sort()

                    print(Difference_1)
                    print(len(Difference_1))
                    """Method one shows the IDs with Malignant diagnosis that were not found by
                    looking at just the first 4 criteria"""
                    #Method 2
                    with open("breastCancerDataReduced.csv", "r") as inputFile:
                        with open("OriginalResult.csv", "w") as outputFile:
                            writer = csv.writer(outputFile)
                            for number,row in enumerate(csv.reader(inputFile)):
                                if number==0:
                                    writer.writerow(row)
                                else:
                                    if row[1]=="M":
                                        writer.writerow(row[0:1])

                    Difference_2=[]
                    with open("intersection.csv", "r") as NewResult:
                        with open("OriginalResult.csv", "r") as originalResult:
                            original = csv.reader(originalResult)
                            originalRows = list(original)
                            print(len(originalRows))
                            newResult = csv.reader(NewResult)
                            newResultRows = list(newResult)
                            print(len(newResultRows))
                            for originalRow in originalRows:
                                if originalRow not in newResultRows:
                                    Difference_2+=[originalRow]
                                    Difference_2.sort()

                    print(len(Difference_2))
                    """Method two shows the IDs with Malignant diagnosis that were not found by
                    looking at just the first 4 criteria"""
