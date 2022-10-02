from colours import bcolors
from random import randrange

colour = bcolors
WORDLEN = 5
MAX_GUESSES = 6
counter_global = 0

def incrementCounter():
    global counter_global
    counter_global += 1
def decrementCounter():
    global counter_global
    if counter_global > 0:
        counter_global -= 1
def getCounter():
    global counter_global
    return counter_global


def CreateDict(wordList,outputName,WORDLEN=5):
    newWordList = []
    for word in wordList:
        word = word.strip()
        if len(word) == WORDLEN:
        # if len(set(word)) == len(word) and len(word) == WORDLEN:
            newWordList.append(word.upper())
    WriteTextFile(newWordList,outputName)

def WriteTextFile(wordList,outputName):
    textfile = open(outputName, "w")
    for word in wordList:
        textfile.write(word + "\n")
    textfile.close()
    return True,outputName

def ReadTextFileToList(fn):
    text_file = open(fn, "r")
    lines = text_file.readlines()
    text_file.close()
    stripped = [w.strip().upper() for w in lines]
    return stripped

def PickRandomWord(wordDict):
    hiddenWord = wordDict[randrange(len(wordDict))].upper()
    # hiddenWord = 'SUGAR' ## Used for debugging with the same hidden word
    # print('Hidden: ', hiddenWord) ## CHEAT TO SEE THE HIDDEN WORD
    return str(hiddenWord).upper().strip()

def BuildPrintString(printDict,userGuess):
    printStr = f''
    for k,v in printDict.items():
        printStr += f'{v}{userGuess[k]}{colour.ENDC}'
    return printStr

def ValidateUserGuess(guessedWord,wordList):
    guessedWord = guessedWord.strip()
    if (len(guessedWord) == WORDLEN) and (guessedWord in wordList):
        return True
    return False


def UserGuessing(hiddenWord,wordDict,first=False):
    if getCounter() >= 6:
        print(f'You used all {getCounter()} guesses! Sorry..\n')
        print(f'The word was {colour.GREEN}{hiddenWord}{colour.ENDC}')
        exit()
    incrementCounter()
    if first:
        userGuess = input('Enter a word: \n')
    else:
        userGuess = input('')
    userGuess = userGuess.upper()
    if not ValidateUserGuess(userGuess,wordDict):
        print('Invalid word.. Try again..')
        decrementCounter()
        UserGuessing(hiddenWord,wordDict)
        return
    mydict = {}
    printDict = {}
    for idx,l in enumerate(userGuess.upper()):
        mydict[idx] = l
    for index,letter in enumerate(hiddenWord.upper()):
        if mydict[index] == letter:
            printDict[index] = colour.GREEN
        elif mydict[index] in hiddenWord:
            printDict[index] = colour.YELLOW
        else:
            printDict[index] = colour.RED
    BuildPrintString(printDict,userGuess)
    print(f'\t {str(getCounter())}. {BuildPrintString(printDict,userGuess)}')
    if userGuess.upper() == hiddenWord.upper():
        print(f'\nYou got it! That took you {getCounter()} tries!')
        return True
    else:
        UserGuessing(hiddenWord,wordDict)
        return

def main():
    # wordDict = CreateDict(ReadTextFileToList('dict.txt'),"newDictHard.txt",WORDLEN) ## Run once to create the dict from a text file
    wordDict = ReadTextFileToList("newDictHard.txt") ## Run if the dict you want to use is already a text file
    hiddenWord = PickRandomWord(wordDict)
    UserGuessing(hiddenWord,wordDict,first=True)

main()




