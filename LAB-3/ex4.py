import string

def check_password_strength(password):
    rating = 0 
    missing_requirements = []

    has_min_length = len(password) >= 8
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in string.punctuation:
            has_special = True

    if has_min_length:
        rating += 1
    else:
        missing_requirements.append("Minimum length of 8 characters")

    if has_uppercase:
        rating += 1
    else:
        missing_requirements.append("At least one uppercase letter")

    if has_lowercase:
        rating += 1
    else:
        missing_requirements.append("At least one lowercase letter")

    if has_digit:
        rating += 1
    else:
        missing_requirements.append("At least one digit")

    if has_special:
        rating += 1
    else:
        missing_requirements.append("At least one special character")

    approved = len(missing_requirements) == 0

    return {
        "rating": rating,
        "missing_requirements": missing_requirements,
        "approved": approved
    }

print(check_password_strength("Password123!"))
print(check_password_strength("blqblq"))