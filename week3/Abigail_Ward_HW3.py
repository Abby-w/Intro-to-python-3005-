


#problem 1
print("problem 1")
print(" ")

#define the function calcSum
def calcSum(a,b,c):
    '''This function should take 3 integers as arguements and return
    the sum of all non-duplicated values'''
    #no duplicates
    if a != b and b!= c and a!= c :
        print(a+b+c)
    # a and b are duplicates
    elif a == b and b!= c and a!= c:
        print(a+c)
    # a and c are duplicates
    elif a == c and a!= b and b!= c:
        print(a+b)
    # b and c are duplicates
    elif b == c and a!= b and a!= c:
        print(a+b)
    # a, b and c are duplicates
    elif b == c and a == b:
        print(a)
    print("a is: ", a, " and b is: " , b, " and c is: " , c)
calcSum(102,9321,1021)



#Problem 2
print(" ")
print("Problem 2")
print(" ")


def intDiff(a,b,c):
    if abs(a-b)<=1:
        if abs(a-c)>=2:
            print(True)
    elif abs(a-c)<=1:
        if abs(a-b)>=2:
            print(True)
    print("a is: ", a, " and b is: " , b, " and c is: " , c)
intDiff(6,8,8)

#Problem 3
print(" ")
print("Problem 3")
print(" ")

def multTable(integer):
    for i in range(1,13,1):
          print(integer , " x " , i , " = " , (i*integer))

multTable(23)



#Problem 4
print(" ")
print("Problem 4")
print(" ")

#define the function numToWords
def numToWords(integer):
    '''numToWords takes any integer value and converts it to words '''
    #print out value for visibility
    print(integer)
    #seperate out each integer in the argument
    seperateIntegers=[int(i) for i in str(integer)]
    #create an empty line to add to
    line=''
    #iterates through terms in seperateIntegers, converts to a word and adds to the line
    for i in seperateIntegers:
        if i==0:
            line+= "zero "
        if i==1:
            line+= "one "
        if i==2:
            line+= "two "
        if i==3:
            line+= "three "
        if i==4:
            line+= "four "
        if i==5:
            line+= "five "
        if i==6:
            line+= "six "
        if i==7:
            line+= "seven "
        if i==8:
            line+= "eight "
        if i==9:
            line+= "nine "
    print(line)

numToWords(789230491920)


#Problem 5
print(" ")
print("Problem 5")
print(" ")

#start a while loop to allow user to repeat calculations if they want
x = 1
while x== 1:
    #define the function userMeasurements
    def userMeasurements():
        '''userMeasurements takes no argument but asks for the users height, weight and age to determine the hat size, jacket size, and waist size'''
        #user inputs of height weight and age
        height=int(input("please enter your height in inches: "))
        weight=int(input("please enter your weight in pounds: "))
        age=int(input("please enter your age in years: "))

    #define the function hSize
        '''hSize takes no argument but takes the users height, weight and age to determine the hat size'''
        def hSize():
            hatSize=(weight/height)*2.9
            print("Hat size is: ", round(hatSize))
        hSize()

    #define the function jSize
        '''jSize takes no argument but takes the users height, weight and age to determine the jacket size'''
        def jSize():
            if age>30:
                jacketAdjustment=float((1/8)*((age//10)-2))
                jacketSize=((height*weight)/288)+jacketAdjustment
            elif age<=30:
                jacketSize=(height*weight)/288
            print("Jacket size is: ", round(jacketSize,2))
        jSize()

    #define the function wSize
        '''wSize takes no argument but takes the users height, weight and age to determine the waist size'''
        def wSize():
            if age>28:
                waistAdjustment=float((1/10)*((age//2)-27))
                waistSize=(weight/5.7)+waistAdjustment
            elif age<=28:
                waistSize=weight/5.7
            print("Waist size is: ", round(waistSize))
        wSize()

    userMeasurements()
    #asks the user if they want to repeat the calculations or ends the loop
    cont=input("Do you want to repeat this? (Yes or No): ")
    if cont.lower()=='no':
        x=2
