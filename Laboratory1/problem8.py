def binaryToNTest():
    '''
    Test the binaryToN function
    '''
    try:
        assert binaryToN(4) == ["1", "10", "11", "100"]
        assert binaryToN(3) == ["1", "10", "11"]
        assert binaryToN(2) == ["1", "10"]
        assert binaryToN(1) == ["1"]
        return True
    except:
        return False


def binaryToN(n):
    '''
    Returns a list of all binary representations of numbers from 1 to n
    Input: n - Unsigned Integer
    Output: resultBinary - List of Strings
    '''
    resultBinary = []
    for number in range(1, n + 1):
        resultBinary.append(bin(number).replace("0b", ""))
    return resultBinary




if binaryToNTest() == True:
    print("Teste trecute cu succes!")
else:
    print("Teste esuate!")