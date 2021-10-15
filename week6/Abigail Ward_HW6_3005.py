#1
def listToDict(listOfNumbers):
    """Puts a list into a dictionary.

    Parameters
    ----------
    listOfNumbers: A list of numbers

    Returns
    -------
    dictionary: A dictionary where the key is an ascending value 1 to n and the
        corresponding value is the element in the list.
    """
    #define the empty dictionary and necessary variables.
    dictionary={}
    length=len(listOfNumbers)

    #iterate through the values 1 to list length
    #add iterated number and the element based on that number to the dictionary
    for number in range(1,length+1,1):
        dictionary[number]=listOfNumbers[number-1]

    return dictionary

#input and call function
list=[2,6,6,1,7,9]
print(listToDict(list))


#2
def newDict(dictionary):
    """Inverts the keys and the values in a dictionary.

    Parameters
    ----------
    dictionary: A dictionary

    Returns
    -------
    dictionaryReversed: A dictionary where the key is the value from
        dictionary and the value is the key from dictionary.
    """
    #define the empty dictionary
    dictionaryReversed={}

    #iterate throught the keys and values in the dictionary
    for key,value in dictionary.items():
    #set the new keys and new values
        newKey=value
        newValue=key
        #add the new keys and new values to the empty dictionary
        dictionaryReversed[newKey]=newValue

    return dictionaryReversed

#input and call function
dict={1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 2:5}
print(newDict(dict))

#duplicate values will not all remain in the new dictionary
#there can only be one thing the key is mapped to
#the second key defined will replace the first key


#3
def uniqueElems(listOfValues):
    """Returns true if all the values in a list are unique.

    Parameters
    ----------
    listOfValues: A list of values

    Returns
    -------
    bool: True if the values are all unique, false if there are duplicate values
    """
    #define the empty dictionary and necessary variables.
    lengthList=int(len(listOfValues))
    dictionary={}
    dictionaryReversed={}

    #add all the elements in the list as values in the dictionary
    for number in range(1,lengthList+1,1):
        dictionary[number]=listOfValues[number-1]

    #invert the keys and values in the dictionary
    for key,value in dictionary.items():
        newKey=value
        newValue=key
        dictionaryReversed[newKey]=newValue

    #compare the length of the list and the length of the dictionary
    lengthDict=len(dictionaryReversed)
    if lengthDict==lengthList:
        return "True"
    else:
        return "False"

#input and call function
list=[2,1,3, 5]
print(uniqueElems(list))


#4
def valFrequency(listOfValues):
    """returns a dictionary of the elements in the list and their frequency.

    Parameters
    ----------
    listOfValues: A list of values

    Returns
    -------
    dictionary: A dictionary where the key is the element in the list
        the value is the number of times that element appears in the list
    """
    #define the empty dictionary and necessary variables.
    dictionary={}
    index=0

    #begin loop of indexing through the list
    while index<(len(listOfValues)):
        #define variables
        count=1
        originalElement=listOfValues[index]
        value=originalElement

        #compare the element at index to all other elements in the list
        for i, elementToCompare in enumerate(listOfValues):
            #if the element is the same as the original element add 1 to the count
            if (index!=i) and (originalElement==elementToCompare):
                count+=1
        #remove all the elements with the same value as the original element
        numberToRemove=count
        while numberToRemove>0:
            listOfValues.remove(value)
            numberToRemove+=-1

        #add the element and the count to the dictionary
        dictionary[originalElement]=count

    return dictionary

#input and call function
list=[2,6,6,1,7,9,6,7,3,4,5,6,23,4,8]
print(valFrequency(list))


#5
def addsToK(k,A):
    """returns True if two unique elements in the list A add to the value k

    Parameters
    ----------
    A: A list of integers
    k: Integer

    Returns
    -------
    bool: True if two unique values in A add to k
        false if there are no two unique values in A that add to k
    """

    #define the necessary variables.
    index=0
    length=len(A)

    #begin loop of comparing the index to the length-1
    while index<length-1:
        #define the element to be used in the sum
        originalElement=A[index]

        #iterate through the elements in A
        for i, element in enumerate(A):
        #if the indices are not the same and the elements are not the same
            if (index!=i) and originalElement!=element:
                #see if the two elements add to k
                if (originalElement+element)==k:
                    return True
        #if no two elements added to k, look at the element in the next index
        index+=1
    return False

#input and call function
sum=6
listOfIntegers=[3,4,7,10,2,5]
print(addsToK(sum,listOfIntegers))
