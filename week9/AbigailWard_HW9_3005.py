#1
print("1) Findstring: ")
def findString(string, fileName):
    """Returns the lines of the file that contain the string

    Parameters
    ----------
    string: A string
    fileName: A file with multiple lines of strings

    Returns
    -------
    containString: A list of the lines in fileName that contain the string
    """
    #define the variables
    containString=[]
    x=0
    #check that the file name is valid
    while x==0:

        try:
            with open(fileName,"r") as file:
                x=1
        except:
            print("Please enter a valid file name")
            fileName=input("Please input the file name: ")
    #read the file
    with open(fileName,"r") as file:
        lines=file.readlines()
        #look for the string in each line
        for line in lines:
            lowerCase=line.lower()
            index=lowerCase.find(string)
            if index!=-1:
                containString+=[line]
    return containString

#get inputs and call function
fileName=input("Please input the file name: ")
string=input("please enter a string: ")
print(findString(string, fileName))


#2
print("2) wrapLines: ")
import textwrap
def wrapLines(fileName, k):
    """Cuts up the lines of the file at lengths less than k. Does not cut words.

    Parameters
    ----------
    fileName: A file with multiple lines of strings
    k: an integer

    Returns
    -------
    Overwrites file with the resized text
    """
    #define the variables
    text=[]
    x=0
    #check that the file name is valid
    while x==0:

        try:
            with open(fileName,"r") as file:
                x=1
        except:
            print("Please enter a valid file name")
            fileName=input("Please input the file name: ")
    #read the file
    with open(fileName,"r") as file:
        #split each line after k charaters
        lines=file.readlines()

        for line in lines:
            text+=textwrap.wrap(line, width=int(k), break_long_words=False)
        #overwrite the file with the resized lines
        with open(fileName, "w") as newFile:
            for item in text:
                newFile.write("%s\n" % item)

#get inputs and call function
k=input("Please enter an integer: ")
fileName=input("Please input the file name: ")
wrapLines(fileName, k)

#3
print("3) allAnagrams")
def allAnagrams(dictionary):
    """Finds all the words in a file that are anagrams with another word in
    the file

    Parameters
    ----------
    dictionary: A file containing a dictionary

    Returns
    -------
    anagrams: A list of all the anagrams found in the file
    """
    #define the variables
    anagrams=[]
    #read the file
    file=open(dictionary, "r")
    lines=file.readlines()
    length=len(lines)
    index=0
    #iterate through the words and compare to the letters of a "key" word
    while index<length-1:
        keyWordLetters=[i for i in lines[index]]
        keyWordLetters.sort()
        for i, word in enumerate(lines):
            if i != index:
                wordLetters=[i for i in word]
                wordLetters.sort()
                if keyWordLetters == wordLetters:
                    anagram=lines[index].replace("\n", "")
                    #add the anagram words to the list
                    anagrams += [anagram]
        #change the key word
        index+=1
    file.close()
    return(anagrams)

print(allAnagrams('shortDictionary.txt'))
