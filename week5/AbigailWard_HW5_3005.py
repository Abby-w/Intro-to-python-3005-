#1
def minMaxTuple(list):
    """Puts the smallest and largest element in a tuple.

    Parameters
    ----------
    list: A list of numbers

    Returns
    -------
    tuple: A tuple of the smallest and largest element in the list
    """
    # set the smallest element to be the first element in the list
    min = list[0]
    #compare each of the elements in the list to the current minimum
    #if the element is smaller than minimum, replace the minimum with element
    for i in list:
        if i < min:
            min = i
    # set the largest element to be the first element in the list
    max = list[0]
    #compare each of the elements in the list to the current maximum
    #if the element is larger than the maximum, replace the maximum with element
    for i in list:
        for i in list:
            if i > max:
                max = i
    #create the tuple containing the minimum and maximum elements
    tuple=(min,max)
    return tuple

#input and call function
a=[1,2,3,4,5,6,7,8,9, 450, 200,12,0.001, 0.001, 89, -100]
print("The smallest and largest values in the list are :", minMaxTuple(a))

#2
def allPairs(listOne,listTwo):
    """Creates a list of all possible pairs of elements between lists.
    No duplicate elements in pairs.

    Parameters
    ----------
    listOne: A list of numbers
    listTwo: A list of numbers

    Returns
    -------
    result: A list of tuples containing all possible combinations of elements
    from the two lists as long as both elements are not the same.
    """
    #create an empty list to put the tuples in
    result=[]
    for elementOne in listOne:
        for elementTwo in listTwo:
            #compare and index through the elements in both lists
            #if the elements are not the same, put them in a tuple (set)
            #add the pair into the result list
            if elementOne!=elementTwo:
                pair=(elementOne,elementTwo)
                result+=[pair]
    return result

#input and call function
inputListOne=[1,2,3,4, 4, 4]
inputListTwo=[1,2,3]
print("The pairs of all lists' elements are :", allPairs(inputListOne,inputListTwo))

#3
#inport math to perform the distance formula
import math
def distance(tupleList):
    """Returns the pair of coordinates (tuples) with
    the shortest distance between them.

    Parameters
    ----------
    tupleList: A list of two element tuples representing x and y coordinates

    Returns
    -------
    newTuple: A tuple of the two tuples with the smallest distance between them
    """

    #define the variables: minimum set to a high number
    index=0
    min=100000000
    #begin loop of the index of the tupleList being used in calculations
    while index<(len(tupleList)-1):
        originalPoint=tupleList[index]
        for i, secondPoint in enumerate(tupleList):
            #ensure the calculation is not being done on the same element
            if (index!=i):
                #Uses the distance formula sqrt((x2-x1)^2 + (y2-y1)^2)
                distance=math.sqrt((originalPoint[0]-secondPoint[0])**2 + (originalPoint[1]-secondPoint[1])**2)
                #compare the calculated distance to the current minimum
                if distance<min:
                    min=distance
                    firstSmallest=originalPoint
                    secondSmallest=secondPoint
        #increase the index value to look at the next element
        index+=1
    newTuple=(firstSmallest , secondSmallest)
    return newTuple

#input and call function
inputList=[(1,2),(20,1),(1,4),(1,3),(1,10),(10,1), (100, 12), (1,1)]
print("The coordinates with the smallest distance are :", distance(inputList))


#4
def removeDups(tupleList):
    """Removes all the duplicate elements in a list.

    Parameters
    ----------
    tupleList: A list of tuples

    Returns
    -------
    tupleList: A list of tuples with no duplicate tuples
    """
    #begin loop of the index of the tupleList being used in calculations
    index=0
    while index<(len(tupleList)-1):
        originalElement=tupleList[index]
        #compare the original element to all other elements in the list
        for i, elementToCompare in enumerate(tupleList):
            #if the element is the same as the original element, remove it
            if (index!=i) and (originalElement==elementToCompare):
                tupleList.remove(elementToCompare)
        #increase the index value to look at the next element
        index+=1

    return tupleList

#input and call function
inputList=[(1,2),(1,4,5),(1,2),(1,2), (2,1)]
print("The list with no duplicate elements is:", removeDups(inputList))
