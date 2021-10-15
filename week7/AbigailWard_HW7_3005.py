#1
def setComp():
    """setComp generates a set of pair tuples. The tuple contains all integers
    between 1 and 10000 paired with the square of that value if the square is
    divisible by 3

    Parameters
    ----------
    No parameters

    Returns
    -------
    tupleSet: A set of pair tuples of integers between 1 and 10000 and the
    square of the integer if the square is divisible by 3
    """

    #define the variables
    tupleList=[]
    #build a list of tuple pairs
    for i in range(1,10001):
        tupleList+=[(i,i**2)]
    #add tuples from list to set if the square is divisible by 3
    tupleSet={tuple for tuple in tupleList if tuple[1]%3==0}
    return tupleSet

print(setComp())

#2
def minMaxSet(setOfNumbers):
    """minMaxSet returns the minimum and the maximum value in the set

    Parameters
    ----------
    setOfNumbers: A set consisting of any number

    Returns
    -------
    min: The minimum value in the set
    max: The maximum value in the set
    """

    #put the values in the set into a list
    list=[i for i in setOfNumbers]
    print(list)
    #define variables
    index=0
    min=list[index]
    #iterate through the list
    while index<len(list)-1:
        #find the minimum value
        for j in list:
            if min > j:
                min=j
            index+=1
    #re-define and define the variables
    index=0
    max=list[index]
    #iterate through the list
    while index<len(list)-1:
        #find the maximum value
        for j in list:
            if max < j:
                max=j
            index+=1

    return min, max
print(minMaxSet({1,2,5,3,4,64,22,0.5,3}))

#3

def uniqueElems(listOfValues):
    """uniqueElements returns a boolean, determining if all the elements
    in the list are uniqueElems

    Parameters
    ----------
    listOfValues: A list of values

    Returns
    -------
    True: All the elements in the list are unique
    False: At least one of the elements in the list is not unique
    """

    #put all of the elements from the list into a set
    set={i for i in listOfValues}
    #compare the length of the set to the length of the list
    lengthSet=len(set)
    lengthList=len(listOfValues)
    if lengthSet==lengthList:
        return True
    else:
        return False


print(uniqueElems([2,3,2,4,5,6,7,3,1,8]))

#4
def commonElems(A,B):
    """commonElems returns a frozen set of the elements in  set A or set B but
    not in both sets

    Parameters
    ----------
    A: A set of any elements
    B: A set of any elements

    Returns
    -------
    frozenSet: A frozen set of the elements in A or B but not A and B
    """

    #create a set of the elements in both A and B
    intersection=A.intersection(B)
    #create a set of all the elements in A and B
    union=A.union(B)
    #create a set of the union elements without the intersection elements
    frozenSet=union.difference(intersection)
    return frozenSet
print(commonElems({1,2,3,4,5,6}, {2,7,3,8,9}))

#5
def addsToK(k,A):
    """addToK returns a boolean, determining if a distinct pair of elements in
    the list A add to k

    Parameters
    ----------
    k: an integer
    A: an unordered list of integers

    Returns
    -------
    True: There are two distinct elements in A that add to k
    False: There are not two distinct elements in A that add to k
    """
    #create an empty set
    sumSet=set()
    #add the sum of two distinct elements in the list to the set
    for i in A:
         for j in A:
             if i!=j:
                 sumSet|={i+j}
    #check for k in the set
    if k in sumSet:
        return True
    else:
        return False

print(addsToK(130,[1,2,4,5,6,7,8,4,3,2]))
