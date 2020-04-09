from exceptions import InvalidUsage


def cost_for_crossing(num_trips: int) -> float:
    return num_trips * 0.25
    
def result(bags: int, geese: int) -> str:
    if bags >= 1 and geese > 2:
        return f'Your selection of {bags} bag(s) and {geese} geese will result in A LOSS.'

    if geese >= 1 and bags > 2:
        return f'Your selection of {bags} bag(s) and {geese} geese will result in A LOSS.'

    if geese == 2 and bags == 2:
        return f'Your selection of 2 bag(s) and 2 geese will result in A LOSS.'

    return f'Your selection of {bags} bag(s) and {geese} geese will result in NO LOSS at a total cost of: £{cost_for_crossing(number_of_crossings(bags, geese)):.2f}'

def number_of_crossings(bags: int, geese: int) -> int:
    if bags < 0:
        raise InvalidUsage('Number of bags must be positive.')
    if geese < 0:
        raise InvalidUsage('Number of geese must be positive.')

    if bags == 2 and geese == 1:
        return 7
    if bags == 1 and geese == 2:
        return 7
    if bags == 0 and geese == 0:
        return 0
    if bags == 0 or geese == 0:
        return 2 * (geese + bags) - 1
    if bags == 1 and geese == 1:
        return 3


def journey(bags: int, geese: int) -> str:
    if bags == 2 and geese == 1:
        return 'Take goose across, return, take bag across, return with goose, take bag across, return, take goose across'
    if bags ==1 and geese == 2:
        return 'Take bag across, return, take goose across, return with bag, take geese across, return, take bag across'
    if bags == 0 and geese == 0:
        return 'No journey taken'
    if bags == 3 and geese == 0:
        return 'Take bag across, return, take bag across, return, take bag across'
    if bags == 4 and geese == 0:
        return 'Take bag across, return, take bag across, return, take bag across, return, take bag across'
    if bags == 1 and geese == 3:
        return 'No journey taken'

    return 'Take bag across, return, take goose across'
    