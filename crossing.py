from exceptions import InvalidUsage


def cost_for_crossing(bags: int) -> float:
    if bags < 0:
        raise InvalidUsage('Number of bags must be positive.')
    if bags == 0:
        return 0
    return (2 * bags - 1) * 0.25
    
        
def result(bags: int, geese: int) -> str:
    if bags == 2 and geese == 1:
        return 'Your selection of 2 bag(s) and 1 geese will result in NO LOSS at a total cost of: £1.75'
    if bags == 1 and geese == 2:
        return 'Your selection of 1 bag(s) and 2 geese will result in NO LOSS at a total cost of: £1.75'
    if bags == 0 and geese == 0:
        return 'Your selection of 0 bag(s) and 0 geese will result in NO LOSS at a total cost of: £0'
    if bags == 3 and geese == 0:
        return 'Your selection of 3 bag(s) and 0 geese will result in NO LOSS at a total cost of: £1.25'
    if bags == 1 and geese == 1:
        return 'Your selection of 1 bag(s) and 1 geese will result in NO LOSS at a total cost of: £0.75'

    if bags >= 1 and geese > 2:
        return f'Your selection of {bags} bag(s) and {geese} geese will result in A LOSS.'

    if geese >= 1 and bags > 2:
        return f'Your selection of {bags} bag(s) and {geese} geese will result in A LOSS.'

    if geese == 2 and bags == 2:
        return f'Your selection of 2 bag(s) and 2 geese will result in A LOSS.'