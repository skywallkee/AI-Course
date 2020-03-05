def scalarProductTest():
    '''
    Test the scalarProduct function
    '''
    try:
        assert scalarProduct([1, 0, 2, 0 ,3], [1, 2, 0, 3, 1]) == 4
        assert scalarProduct([], []) == 0
        assert scalarProduct([0, 0, 0], [1, 2, 3]) == 0
        assert scalarProduct([1], [5]) == 5
        assert scalarProduct([0, 1, 2], [1, 2, 3]) == 8
        assert scalarProduct([-1, 0, 0], [1, 2, 3]) == -1
        assert scalarProduct([0.5, 0.5], [0.5, 1]) == 0.75
        assert scalarProduct([1, 2, 3], [1, 2]) == "Exception"
        return True
    except:
        return False


def scalarProduct(vector1, vector2):
    '''
    Returns the scalar product of two rare vectors
    Input: vector1, vector2 - List of Double
    Output: product - Double
    '''
    product = 0

    if len(vector1) != len(vector2):
        return "Exception"

    for numberIndex in range(len(vector1)):
        product += vector1[numberIndex] * vector2[numberIndex]

    return product


if scalarProductTest() == True:
    print("Teste trecute cu succes!")
else:
    print("Teste esuate!")