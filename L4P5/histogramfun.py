import pylab

# You may have to change this path
WORDLIST_FILENAME = "./words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    def prop_vowels(word):
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0
        for char in word:
            if char in vowels:
	        count += 1
        return (count/float(len(word)))
    props = []
    for word in wordList:
        props.append(prop_vowels(word))
    props = sorted(props)
    bucket_width = len(wordList)/numBins
    pylab.figure(1)
    pylab.xlabel("Proportion of vowels")
    pylab.ylabel("Num words")
    pylab.plot(props, range(0, len(wordList), bucket_width))
    pylab.show()

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
