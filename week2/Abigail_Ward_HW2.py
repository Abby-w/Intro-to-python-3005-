
# Problem 1
print("Problem 1")
x = 0
while x == 0:
    age=int(input("Please enter your age: "))
    if age >= 21 :
        print("You are allowed in the bar")
        x=1
    elif age < 21:
        print("You are not allowed in the bar")
        x=1

#Problem 2
print(" ")
print("Problem 2")
speed= int(input("How fast were you going?(mph): "))
bday =input("Is today your birthday?(Y or N): ")
if bday == "N" :
    if speed <= 60:
        print("No ticket")
    elif speed >60 and speed <= 80:
        print("Small ticket")
    elif speed <80:
        print("Big ticket")
else:
    if speed <= 65:
        print("No ticket")
    elif speed >65 and speed <= 85:
        print("Small ticket")
    elif speed <85:
        print("Big ticket")

#Problem 3
print(" ")
print("Problem 3")
x=0
while x==0 :
    multNum=int(input("Enter a non-negative integer: "))
    if multNum<0 :
        continue
    elif multNum % 3==0 and multNum % 5 !=0 :
        print("True (multiple of 3 but not 5)")
        x=1
    elif multNum % 3 !=0 and multNum % 5 ==0:
        print("True (multiple of 5 but not 3)")
        x=1
    else:
        print("False")
        x=1


#Problem 4
print(" ")
print("Problem 4")
a=''
b=''
c=''

while a is not int and b is not int and c is not int:
    try:
        a=int(input("Please enter an integer: "))
        b=int(input("Please enter another integer: "))
        c=int(input("Please enter one more integer: "))

        break
    except ValueError:
        print("Please only enter valid integers")

a_int=int(a)
b_int=int(b)
c_int=int(c)
if a< b and b<c :
    print("True")
else:
    print("False")

#Problem 5
print(" ")
print("Problem 5")
for numBottles in range(99,-1,-1):
    if numBottles > 2:
        print(numBottles,  " bottles of beer on the wall, ",  numBottles,  "bottles of beer. Take one down and pass it around, ",  (numBottles-1), "bottles of beer on the wall")
    if numBottles==2:
        print(numBottles,  " bottles of beer on the wall, ",  numBottles,  "bottles of beer. Take one down and pass it around, ",  (numBottles-1), "bottle of beer on the wall")
    if numBottles ==1:
        print(numBottles,  " bottle of beer on the wall, ",  numBottles,  "bottle of beer. Take one down and pass it around, ",  (numBottles-1), "bottles of beer on the wall")
    if numBottles == 0:
        print("No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.")


#Problem 6
print(" ")
print("Problem 6")
series=0
for denominator in range(3,101,4):
    series=(series - (1/denominator))
for denominator in range(1,101,4):
        series = series +(1/denominator)
print(series)
pi = 4*series
print(pi)

#Problem 7
print(" ")
print("Problem 7")
k=''
smallBrick=''
largeBrick=''

while k is not int and smallBrick is not int and largeBrick is not int:
    try:
        k=int(input("Please enter an integer: "))
        smallBrick=int(input("Please enter another integer: "))
        largeBrick=int(input("Please enter one more integer: "))

        break
    except ValueError:
        print("Please only enter valid integers")

inchesSmall=1*smallBrick
inchesLarge=5*largeBrick

if k> (inchesSmall+inchesLarge):
    print("Row of bricks is not possible with this combination")
else:
    print("Row of bricks is possible with this combination")


#Problem 8
print(" ")
print("Problem 8")
change=''

while change is not float:
    try:
        change=float(input("Please enter a value: "))
        break
    except ValueError:
        print("Please only enter numeric values")
print(change)
Hundreds=int(change//100)
Fifties=int((change-(Hundreds*100))//50)
Twenties=int((change-(Hundreds*100+Fifties*50))//20)
Tens=int((change-(Hundreds*100+Fifties*50+Twenties*20))//10)
Fives=int((change-(Hundreds*100+Fifties*50+Twenties*20+Tens*10))//5)
Ones=int((change-(Hundreds*100+Fifties*50+Twenties*20+Tens*10+Fives*5))//1)
Quaters=int((change-(Hundreds*100+Fifties*50+Twenties*20+Tens*10+Fives*5+Ones*1))//0.25)
Dimes=int((change-(Hundreds*100+Fifties*50+Twenties*20+Tens*10+Fives*5+Ones*1+Quaters*0.25))//0.1)
Pennies=int((change-(Hundreds*100+Fifties*50+Twenties*20+Tens*10+Fives*5+Ones*1+Quaters*0.25+Dimes*0.1))//0.01)

print(Hundreds, "hundreds, ", Fifties, "fiftes, ", Twenties, "twenties, ", Tens, "tens, ", Fives, "fives, ", Ones, "ones, ", Quaters, "quarters, ", Dimes, "dimes, and ", Pennies, "pennies. ")
