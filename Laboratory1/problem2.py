import math


def euclidianDistanceTest():
    '''
    Test the euclidianDistance function
    '''
    try:
        assert euclidianDistance((1, 5), (4, 1)) == 5.0
        assert euclidianDistance((0, 0, 0), (1, 2, 3)) == 3.74
        assert euclidianDistance(tuple([2]), tuple([6])) == 4.0
        assert euclidianDistance((), ()) == -1
        assert euclidianDistance((1, 2, 3), (1, 2)) == -1
        return True
    except:
        return False


def euclidianDistance(point1, point2):
    '''
    Returns the distance from point1 and point2
    Input: point1, point2 - Tuple of numbers
    Output: distance - Unsigned Double
    '''
    distance = 0

    if len(point1) != len(point2) or len(point1) < 1:
        return -1
    
    sum = 0
    for coordinateIndex in range(len(point1)):
        sum += (point1[coordinateIndex] - point2[coordinateIndex])**2
    
    distance = round(math.sqrt(sum), 2) # O(1)

    return distance


if euclidianDistanceTest() == True:
    print("Teste trecute cu succes!")
else:
    print("Teste esuate!")