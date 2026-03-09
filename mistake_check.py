def detect_mistakes(equation):

    mistakes = []

    if "+ -" in equation:
        mistakes.append("Possible sign mistake")

    if "**" in equation:
        mistakes.append("Check exponent usage")

    if "/" in equation:
        mistakes.append("Check fraction simplification")

    return mistakes