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
    with open("q3_B.csv", "w") as outputFile:
        writer = csv.writer(outputFile)
        for number,row in enumerate(csv.reader(inputFile)):
            if number==0:
                writer.writerow(row)
            else:
                if row[1]=="B":
                    writer.writerow(row)
    with open("q3_M.csv", "w") as outputFile:
        writer = csv.writer(outputFile)
        for number,row in enumerate(csv.reader(inputFile)):
            if number==0:
                writer.writerow(row)
            else:
                if row[1]=="M":
                    writer.writerow(row)

#those data samples whose texture value is >= 18
    with open("q4_gte_18.csv", "w") as outputFile:
        writer = csv.writer(outputFile)
        for number,row in enumerate(csv.reader(inputFile)):
            if number==0:
                writer.writerow(row)
            else:
                if float(row[3])>=18:
                    writer.writerow(row)
    with open("q4_B.csv", "w") as outputFile:
        writer = csv.writer(outputFile)
        for number,row in enumerate(csv.reader(inputFile)):
            if number==0:
                writer.writerow(row)
            else:
                if row[1]=="B":
                    writer.writerow(row)
    with open("q4_M.csv", "w") as outputFile:
        writer = csv.writer(outputFile)
        for number,row in enumerate(csv.reader(inputFile)):
            if number==0:
                writer.writerow(row)
            else:
                if row[1]=="M":
                    writer.writerow(row)

#those data samples whose perimeter value is >= 85
    with open("q5_gte_85.csv", "w") as outputFile:
        writer = csv.writer(outputFile)
        for number,row in enumerate(csv.reader(inputFile)):
            if number==0:
                writer.writerow(row)
            else:
                if float(row[4])>=85:
                    writer.writerow(row)
    with open("q5_B.csv", "w") as outputFile:
        writer = csv.writer(outputFile)
        for number,row in enumerate(csv.reader(inputFile)):
            if number==0:
                writer.writerow(row)
            else:
                if row[1]=="B":
                    writer.writerow(row)
    with open("q5_M.csv", "w") as outputFile:
        writer = csv.writer(outputFile)
        for number,row in enumerate(csv.reader(inputFile)):
            if number==0:
                writer.writerow(row)
            else:
                if row[1]=="M":
                    writer.writerow(row)

#those data samples whose area value is >= 500
    with open("q6_gte_500.csv", "w") as outputFile:
        writer = csv.writer(outputFile)
        for number,row in enumerate(csv.reader(inputFile)):
            if number==0:
                writer.writerow(row)
            else:
                if float(row[5])>=500:
                    writer.writerow(row)
    with open("q6_B.csv", "w") as outputFile:
        writer = csv.writer(outputFile)
        for number,row in enumerate(csv.reader(inputFile)):
            if number==0:
                writer.writerow(row)
            else:
                if row[1]=="B":
                    writer.writerow(row)
    with open("q6_M.csv", "w") as outputFile:
        writer = csv.writer(outputFile)
        for number,row in enumerate(csv.reader(inputFile)):
            if number==0:
                writer.writerow(row)
            else:
                if row[1]=="M":
                    writer.writerow(row)

with open("breastCancerDataReduced.csv", "r") as inputFile:
    with open("NewResult.csv", "w") as outputFile:
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
    with open("NewResult.csv", "r") as NewResult:
        subset = csv.reader(Subset)
        subsetRows = list(subset)
        newResult = csv.reader(NewResult)
        newResultRows = list(newResult)
        for newResultRow in newResultRows:
            if newResultRow not in subsetRows:
                Difference_1+=[newResultRow]
                Difference_1.sort()
print(Difference_1)
print("percent incorrectly guessed", len(Difference_1)/len(newResultRows)*100)
"""Method one shows the IDs with Benign diagnosis in our list of IDs
that meet the criteria of a radius greater than 13, a texture greater than 18,
a perimeter greater than 85 and an area greater than 500. If there are IDs
in Difference_1, that means the criteria are incorrectly guessing IDs to be
malignant when they are actually benign. This means that the new methood does
not work very well. The new method was incorrect on 18.5 of the IDs selected."""

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
with open("NewResult.csv", "r") as NewResult:
    with open("OriginalResult.csv", "r") as originalResult:
        original = csv.reader(originalResult)
        originalRows = list(original)
        newResult = csv.reader(NewResult)
        newResultRows = list(newResult)
        for originalRow in originalRows:
            if originalRow not in newResultRows:
                Difference_2+=[originalRow]
                Difference_2.sort()
print(Difference_2)
print("percent missed", len(Difference_2)/len(subsetRows)*100)

"""Method two shows the IDs with malignant diagnosis that were not found by
looking at just the first 4 criteria: a radius greater than 13, a texture
greater than 18, a perimeter greater than 85 and an area greater than 500.
If there are IDs in Difference_2, that means the criteria did not find all of
the malignant tumors. This means that the new methood does not work very well.
The new method missed about 24% of the malignant diagnosis."""



"""Difference_1 and Difference_2 are not the same because they describe different
ideas. The list created by looking at the first 4 criteria is missing some of
the Malignant diagnosis IDs as well as contain some benign diagnosis IDs.
Difference_1 is a list of benign IDs which method one guessed to be malignant.
Difference_2 is a list of the malignant IDs which were not included in the list
of IDs created by method one."""
