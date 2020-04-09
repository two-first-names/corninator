from exceptions import InvalidUsage


def cost_for_crossing(bags: int) -> float:
    if bags < 1:
        raise InvalidUsage('Number of bags must be positive.')
    return (2 * bags - 1) * 0.25
