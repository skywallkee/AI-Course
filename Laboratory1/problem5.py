import math


def repeatingNumberTest():
    '''
    Test the repeatingNumber function
    '''
    try:
        assert repeatingNumber([1, 2, 3, 4, 2]) == 2
        assert repeatingNumber([1, 2, 3, 4, 5, 1]) == 1
        assert repeatingNumber([1, 2, 3 , 2]) == 2
        assert repeatingNumber([]) == 0
        assert repeatingNumber([1, 2, 3, 3]) == 3
        return True
    except:
        return False


def repeatingNumber(array):
    '''
    Returns the number that appears twice in the array
    Input: array - List of numbers
    Output: duplicate - Integer
    '''
    if len(array) == 0:
        return 0
    
    n = len(array)
    predictedSum = n * (n+1) // 2
    predictedProduct = math.factorial(n)

    actualSum = 0
    actualProduct = 1

    for number in array:
        actualSum += number
        actualProduct *= number
    
    difference = predictedSum - actualSum
    division = predictedProduct / actualProduct

    duplicate = int(difference / (division - 1))

    return duplicate




if repeatingNumberTest() == True:
    print("Teste trecute cu succes!")
else:
    print("Teste esuate!")