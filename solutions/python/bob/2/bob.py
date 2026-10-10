"""
Function that returns a response based on the user's input.
"""

def response(hey_bob):

    """
    Parameters:
        hey_bob (str): What to say to bob.

    Returns:
        str: Bob's response.

    """
    stripped_input = hey_bob.strip()

    if stripped_input == "":
        return "Fine. Be that way!"
    if stripped_input.endswith("?"):
        if stripped_input.isupper():
            return "Calm down, I know what I'm doing!"
        return "Sure."
    if stripped_input.isupper():
        return "Whoa, chill out!"
    return "Whatever."