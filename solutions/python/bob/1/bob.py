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
    hb = hey_bob.strip()
    
    if hb == "":
        return "Fine. Be that way!"
    elif hb.endswith("?"):
        if hb.isupper():
            return "Calm down, I know what I'm doing!"
        return "Sure."
    elif hb.isupper():
        return "Whoa, chill out!"
    else:
        return "Whatever."