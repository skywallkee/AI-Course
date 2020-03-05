def kthGreatestTest():
    '''
    Test the kthGreatest function
    '''
    try:
        assert kthGreatest([7, 4, 6, 3, 9, 1], 1) == 9
        assert kthGreatest([7, 4, 6, 3, 9, 1], 2) == 7
        assert kthGreatest([7, 4, 6, 3, 9, 1], 3) == 6
        assert kthGreatest([7, 4, 6, 3, 9, 1], 4) == 4
        assert kthGreatest([7, 4, 6, 3, 9, 1], 5) == 3
        return True
    except:
        return False


def kthGreatest(array, k):
    '''
    Returns kth greatest element in an array
    Input: array - List of numbers
    Output: number - Double
    '''
    array = sorted(array, reverse=True)
    return array[k - 1]




if kthGreatestTest() == True:
    print("Teste trecute cu succes!")
else:
    print("Teste esuate!")