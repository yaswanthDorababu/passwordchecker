import re


def passwordchecker(password):

    score = 0

    # Minimum 8 characters
    if len(password) >= 8:
        score += 2

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 2

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 2

    # Number
    if re.search(r"[0-9]", password):
        score += 2

    # Special character
    if re.search(r"""[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>/?]""", password):
        score += 2

    # Result
    if score <= 2:
        result = "Weak"

    elif score <= 6:
        result = "Good"

    else:
        result = "Excellent"

    return result, score