from exceptions import InvalidUsage


def cost_for_crossing(bags: int) -> float:
    if bags < 0:
        raise InvalidUsage('Number of bags must be positive.')
    if bags == 0:
        return 0
    return (2 * bags - 1) * 0.25
