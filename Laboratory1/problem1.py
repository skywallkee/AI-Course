def findLastAlphabeticallyWordTest():
    '''
    Test the findLastAlphabeticallyWord function
    '''
    try:
        assert findLastAlphabeticallyWord("Ana are mere rosii si galbene") == "si"
        assert findLastAlphabeticallyWord("            ") == ""
        assert findLastAlphabeticallyWord("Ana  are  mere  rosii   si    galbene") == "si"
        assert findLastAlphabeticallyWord("Ana ana") == "Ana"
        assert findLastAlphabeticallyWord("Ana ananas") == "ananas"
        assert findLastAlphabeticallyWord("Ana are mere .") == "mere"
        assert findLastAlphabeticallyWord(". , ; '") == ""
        return True
    except:
        return False


def findLastAlphabeticallyWord(sentence):
    '''
    Returns the greatest alphabetically word from a given sentence
    Input: sentence - String
    Output: maxWord - String
    '''
    sentence = sentence.split() # O(n) complexity
    maxWord = ""
    for word in sentence:
        if word.lower() > maxWord.lower() and word[0].isalpha():
            maxWord = word
    
    return maxWord

if findLastAlphabeticallyWordTest() == True:
    print("Teste trecute cu succes!")
else:
    print("Teste esuate!")