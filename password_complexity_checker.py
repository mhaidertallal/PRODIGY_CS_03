import re

def password_complexity_checker(password):
    """
    Assess the strength of a password based on the following criteria:
    1. Length: at least 12 characters
    2. Presence of:
        * Uppercase letters (A-Z)
        * Lowercase letters (a-z)
        * Numbers (0-9)
        * Special characters (!, @, #, $, etc.)
    Provide feedback to users on the password's strength.
    """
    strength = 0
    feedback = ""

    # Check length
    if len(password) >= 12:
        strength += 1
        feedback += "Password length is sufficient (12+ characters).\n"
    else:
        feedback += "Password length is too short (less than 12 characters).\n"

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
        feedback += "Password contains uppercase letters.\n"
    else:
        feedback += "Password lacks uppercase letters.\n"

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
        feedback += "Password contains lowercase letters.\n"
    else:
        feedback += "Password lacks lowercase letters.\n"

    # Check for numbers
    if re.search(r"\d", password):
        strength += 1
        feedback += "Password contains numbers.\n"
    else:
        feedback += "Password lacks numbers.\n"

    # Check for special characters
    if re.search(r"[!@#$%^&*()_+=-{};:'<>,./?]", password):
        strength += 1
        feedback += "Password contains special characters.\n"
    else:
        feedback += "Password lacks special characters.\n"

    # Determine password strength based on the number of criteria met
    if strength == 5:
        feedback += "Password strength: Strong\n"
    elif strength >= 3:
        feedback += "Password strength: Medium\n"
    else:
        feedback += "Password strength: Weak\n"

    return feedback

# Example usage:
password = input("Enter a password: ")
print(password_complexity_checker(password))