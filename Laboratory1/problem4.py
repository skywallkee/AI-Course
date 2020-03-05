def onlyOnceWordsTest():
    '''
    Test the onlyOnceWords function
    '''
    try:
        assert onlyOnceWords("ana are ana are mere rosii ana") == ["mere", "rosii"]
        assert onlyOnceWords("                      ") == []
        assert onlyOnceWords(" . ,  a . v     ,    v   a   s ") == ["s"]
        assert onlyOnceWords("Ana are ana") == ["Ana", "are", "ana"]
        return True
    except:
        return False


def onlyOnceWords(sentence):
    '''
    Returns the words that appear only once in a given sentence
    Input: sentence - String
    Output: wordList - List of String
    '''
    sentence = sentence.split() # O(n) complexity
    wordDictionary = {}

    for word in sentence:
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1
    
    wordList = []
    for word in wordDictionary:
        if wordDictionary[word] == 1:
            wordList.append(word)

    return wordList


if onlyOnceWordsTest() == True:
    print("Teste trecute cu succes!")
else:
    print("Teste esuate!")