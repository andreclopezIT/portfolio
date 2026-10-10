"""
Function to convert a number into it's corresponding raindrop sound.
"""

def convert(number):
    """
    Parameters:
        number (int) : The number whose raindrop sound we are finding.

    Returns:
        result (str) : The raindrop sound.
    """

    result = ""

    if number % 3 == 0:
        result = result + "Pling"
    if number % 5 == 0:
        result = result + "Plang"
    if number % 7 == 0:
        result = result + "Plong"
    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        return str(number)

    return result

print(convert(15))

