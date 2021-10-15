#1
def checkPalindrome(string):
    """Checks if a word is the same forward and backward.

    Parameters
    ----------
    string: a single word

    Returns
    -------
    Boolean:
        True: If the word is a palindrome
        False: If the word is not a palindome
    """
    #define the variables
    palindrome=""
    length=len(string)
    #re-write the word backwards
    for i in range(length-1,-1,-1):
        palindrome+=string[i]
    #check if the string is the same as the palindrome
    if string.lower()==palindrome.lower():
        return True
    else:
        return False

print(checkPalindrome("levela"))

#2
def sortStrings(listOfStrings):
    """Sorts a list of strings based on string length

    Parameters
    ----------
    listOfStrings: A list of strings of various lengths

    Returns
    -------
    listOfStrings: A list of strings of various lengths sorted by string length
    """
    #re-sort the list
    listOfStrings.sort(key=len)
    return(listOfStrings)

print(sortStrings(['Words', 'are', 'thought', 'of', 'as', 'the', 'smallest', 'meaningful']))

#3
def mixedStrings(wordString):
    """Creates a list of all the words possible from a single swap of letters
    in a word

    Parameters
    ----------
    wordStrings: a single word

    Returns
    -------
    listOfWords: A list of strings of various lengths sorted by string length
    """
    #define the variables
    listOfWords=[]
    word=wordString
    wordSet=set()
    length=len(wordString)
    index=0
    #iterate through the word and swap single letter pairs
    while index<length:
        for i in range(0,length):
            if i != index:
                letterOne=word[index]
                letterTwo=word[i]
                if index<i:
                    newword=word[:index]+letterTwo+word[index+1:i]+letterOne+word[i+1:]
                if index>i:
                    newword=word[:i]+letterOne+word[i+1:index]+letterTwo+word[index+1:]
                #add the newly created word to a set
                wordSet.add(newword)
        index+=1
    #add the words from the set to a list
    for i in wordSet:
        listOfWords+=[i]
    return(listOfWords)

print(mixedStrings("abced"))


#4
def reversedPhrase(stringOfWords):
    """Returns a string of words in the reverse order

    Parameters
    ----------
    stringOfWords: A string containing multiple words

    Returns
    -------
    reversed: a string of words in the reverse order from the stringOfWords
    """
    #define the variables
    list=[]
    reversed=""
    length=len(stringOfWords)
    #iterate through the entire string in reverse and seperate words at a space
    for i in range(length-1,-1,-1):
        if stringOfWords[i]==" ":
            word=stringOfWords[i+1:]
            list+=[word]
            stringOfWords=stringOfWords[0:i]
    #add the seperated word into a list
    list+=[stringOfWords]
    #add the words in the list back into a string
    for i in list:
        reversed+=str(i) + " "
    return reversed
print(reversedPhrase("abby bryan deb chris"))


#5
def uniqueLetters(string):
    """Returns a string with no duplicate letters

    Parameters
    ----------
    string: A string

    Returns
    -------
    unique: string but with no duplicated letters
    """
    #define the variables
    lengthString=len(string)
    dictionary={}
    dictionaryReversed={}
    unique=""
    #add all the letters in the string as values in the dictionary
    for number in range(1,lengthString+1,1):
        dictionary[number]=string[number-1]

    #invert the keys and values in the dictionary
    for key,value in dictionary.items():
        newKey=value
        newValue=key
        dictionaryReversed[newKey]=newValue
    #put the letters from the reversed dictionary into a string
    keyList=dictionaryReversed.keys()
    for i in keyList:
        unique+=i
    print(unique)

uniqueLetters("aabbccdefbbb")
