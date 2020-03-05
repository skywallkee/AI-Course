def maxRepeatingNumberTest():
    '''
    Test the maxRepeatingNumber function
    '''
    try:
        assert maxRepeatingNumber([2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]) == 2
        assert maxRepeatingNumber([1, 1, 2]) == 1
        assert maxRepeatingNumber([1, 2]) == -1
        assert maxRepeatingNumber([]) == -1
        assert maxRepeatingNumber([1, 2, 3, 3]) == -1
        assert maxRepeatingNumber([1, 2, 3, 3, 3]) == 3
        return True
    except:
        return False


def maxRepeatingNumber(array):
    '''
    Returns the number that appears more than n/2 times (n is the length of the array)
    Input: array - List of numbers
    Output: number - Integer
    '''
    numberDictionary = {}

    for number in array:
        if number in numberDictionary:
            numberDictionary[number] += 1
            if numberDictionary[number] > len(array) // 2:
                return number
        else:
            numberDictionary[number] = 1
    
    return -1




if maxRepeatingNumberTest() == True:
    print("Teste trecute cu succes!")
else:
    print("Teste esuate!")