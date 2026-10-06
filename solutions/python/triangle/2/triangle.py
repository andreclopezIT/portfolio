"""Functions to check whether a triangle is equilateral, isosceles, or scalene."""

def equilateral(sides):
    """Function to check if triangle is equilateral"""
    for side in sides:
        if side == 0:
            return False

    if sides[0] == sides[1] == sides[2]:
        return True
    return False

def isosceles(sides):
    """Function to check if triangle is isosceles"""
    for side in sides:
        if side == 0:
            return False

    if sides[0] + sides[1] < sides[2] or sides[1] + sides[2] < sides[0] or sides[0] + sides[2] < sides[1]:
        return False

    if sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]:
        return True
    return False


def scalene(sides):
    """Function to check if triangle is scalene"""
    for side in sides:
        if side == 0:
            return False

    if sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]:
        return False

    if sides[0] + sides[1] < sides[2] or sides[1] + sides[2] < sides[0] or sides[0] + sides[2] < sides[1]:
        return False

    return True