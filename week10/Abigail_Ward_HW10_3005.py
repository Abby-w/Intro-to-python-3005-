#1

def recFactorial(x):
    """Returns the factorial of the integer

    Parameters
    ----------
    x: an integer

    Returns
    -------
    factorial: The value of the factorial of x
    """
    #set the base case
    if x==0:
        return 1
    if x == 1:
        return x
    #call the recursive function
    else:
        factorial= x*recFactorial(x-1)
        return factorial

#set the variables and call the function
integer=3
print("The integer is", integer)
print("The factorial is", recFactorial(integer))



#2

def dogLegs(numDogs):
    """Returns the number of legs of the dogs

    Parameters
    ----------
    numDogs: an integer representing the number of dogs

    Returns
    -------
    factorial: The value of the factorial of x
    """
    #set the base case
    if numDogs==0:
        return 0
    #call the recursive function
    else:
        legs=4 + dogLegs(numDogs-1)
        return legs

#set the variables and call the function
dogs=7
print("The number of legs for", dogs, "dogs is:", dogLegs(dogs))

#3

def numBlocks(h):
    """Returns the number of blocks in a triangle

    Parameters
    ----------
    h: in integer representing the height of a triangle

    Returns
    -------
    blocks: The number of blocks making up the triangle
    """
    #set the base case
    if h == 0:
        return 0
    #call the recursive function
    else:
        blocks= h +numBlocks(h-1)
        return blocks

#set the variables and call the function
height=14
print("The number of blocks in a triangle of height", height , "is:" ,numBlocks(height))

# 4

def containsTarget(list, value, contains):
    """Returns a boolean that is true if the list contains the value

    Parameters
    ----------
    list: A list of values
    value: A specific values
    contains: A string to be changed as the function is recursively called
        default is "false"

    Returns
    -------
    boolean: True if the list contains the value
             False if the list does not contain the value
    """
    #set the base case
    if len(list)==0:
        #check the contains variable
        if contains=="true":
            return True
        else:
            return False
    #call the recursive function
    else:
        #check if the list element is the value
        if list[0] == value:
            contains= "true"
        return containsTarget(list[1:], value, contains)

#set the variables and call the function
list=[1,2,3,4,5,6]
target=1
print(containsTarget(list, target, contains="false"))

#5

def countTarget(list, value,count=0):
    """Returns the number of times a target value is in a list of values

    Parameters
    ----------
    list: A list of values
    value: A specific values
    count: An integer to be changed as the function is recursively called
        default is 0

    Returns
    -------
    count: The number of times the value appears in the list
    """
    #set the base case
    if len(list) == 0:
        return count
    #check for the value in the list
    else:
        if list[0] == value:
            count +=1
        #call the recursive function
        return countTarget(list[1:], value, count)

#set the variables and call the function
list=[1,2,3,4,5,1,4,4,5,4,3]
target=4
count=0
print(countTarget(list,target, count))


#6

def countZZ(string, count):
    """Returns the number of times "zz" is in a string

    Parameters
    ----------
    string: A string
    count: An integer to be changed as the function is recursively called
        default is 0

    Returns
    -------
    count: The number of times "zz" appears in the list
    """
    #set the base case
    if len(string)<=2:
        return count
    #check the string for zz
    else:
        if string[0:2]=="zz":
            count +=1
            return countZZ(string[2:], count)
        else:
            return countZZ(string[1:], count)

#set the variables and call the function
print(countZZ("abcdefgzz hijklzzzzmnop", count=0))


#7

def elimDuplicates(string, returnString):
    """Returns the string without any adjacent duplicate characters

    Parameters
    ----------
    string: A string
    returnString: An string to be changed as the function is recursively called


    Returns
    -------
    returnString: The string without any ajacent duplicate characters
    """
    #set the base case
    if len(string)<=1:
        return returnString
    #check for duplicates
    else:
        if string[0].lower()==string[1].lower():
            returnString+=string[0]
        #call the recursive function
        return elimDuplicates(string[1:], returnString)

#set the variables and call the function
returnString=''
print(elimDuplicates("aabbccddeeffgg",returnString))
