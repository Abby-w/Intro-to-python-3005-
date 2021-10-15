#1

allEven = [i for i in range(3,1000) if i%3==0 and i%2==0]
print(allEven)


#2

primeNum = []
for num in range(2,101):
    if all(num%i!=0 for i in range(2,num)) and len(primeNum)<10:
        primeNum.append([num])
print(primeNum)


#3

def firstLast(list):
    first= list[0]
    last = list[-1]
    newList = [first, last]
    print(list)
    print(newList)

firstLast([5,2,45,43,7,32,643,1])


#4

def listSum(numbers):
    sum=0
    for i in numbers:
        sum+=i
    print(numbers)
    print(sum)

listSum([5,2,45,43,7,32,643,1])


#5

def commonElems(listOne,listTwo):
    list=[]
    for i in listOne:
        for j in listTwo:
            if i==j and i not in list:
                list.append(i)
    print("list one: ",listOne)
    print("list two: ",listTwo)
    print(list)
commonElems([1,2,5,8,2,3,5],[4,1,2,3,3,3,3,7,8])


#6

def uniqueElems(list):
    list.sort()
    print("Sorted original list: ", list)
    for i in list:
        count=list.count(i)
        if count>1:
            while count!=0:
                list.remove(i)
                count+=-1
    print("Unique elements list: ", list)

uniqueElems([1,5,3,6,7,3,6,8,2,4])

#7

def sortList(list):
    print("original list: ", list)
    sortedList=[]

    while len(list)>0:
        min = list[0]
        for i in list:

            if i < min:
                min = i

        sortedList.append(min)
        list.remove(min)
    print("sorted list", sortedList)


sortList([3,5,6,1,4,2,2,5,7,10,11])


#8
def rotateList_(a,k):
    print(a)
    print("shift the list ", k, "terms to the left and wrap around")
    length=len(a)
    remainingIndex = (length-1)-int(k)
    list=[]
    list.append(a[k])
    a.remove(a[k])
    while remainingIndex > 0:
        list.append(a[k])
        remainingIndex+= -1
        a.remove(a[k])


    orderedList= list+a
    print(orderedList)

rotateList_([1,2,3,4,5,6,7,8,9,10,1,2,3,3], 3)



#9
#define the bins
bins=[7,7,7,7,7]

#define end game conditions
def checkGameEnd(bins):
    sum=0
    for i in bins:
        sum+=i
    if sum== 0:
        return True
    else:
        return False

#define removing matches
def removeMatches(binNumber,numMatches,bins):
    if bins[binNumber]-numMatches<0 or numMatches==0:
        return False
    else:
        bins[binNumber]=bins[binNumber]-numMatches
        displayGame(bins)
        return True

def displayGame(bins):
    print(bins)

#play the game
checkGameEnd(bins)
currentPlayer=1
while checkGameEnd(bins)==False:

    if currentPlayer== 1:
        print("Player", currentPlayer, "'s turn")
        x=0
        while x==0:
            inputBinNumber=int(input("Please enter the bin number you wish to remove matches from (0-4): "))
            if inputBinNumber>4 or inputBinNumber<0:
                print("Value must be between 0 and 4")
                x=0
            else:
                x=1
        inputnumMatches=int(input("Please enter the number of matches you wish to remove: "))
        turn = removeMatches(inputBinNumber,inputnumMatches,bins)
        if turn == False:
            print("That is not a valid turn")
            displayGame(bins)
            currentPlayer=1
        else:
            currentPlayer=2


    elif currentPlayer== 2:
        print("Player", currentPlayer, "'s turn")
        x=0
        while x==0:
            inputBinNumber=int(input("Please enter the bin number you wish to remove matches from (0-4): "))
            if inputBinNumber>4 or inputBinNumber<0:
                print("Value must be between 0 and 4")
                x=0
            else:
                x=1
        inputnumMatches=int(input("Please enter the number of matches you wish to remove: "))
        turn = removeMatches(inputBinNumber,inputnumMatches,bins)
        if turn == False:
            print("That is not a valid turn")
            displayGame(bins)
            currentPlayer=2
        else:
            currentPlayer=1
print("The game is over, you lose")
if currentPlayer ==2:
    print("Player 2 wins!!")
else:
    print("Player 1 wins!!")
