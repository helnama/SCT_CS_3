import re

def assess_password_strength(password: str) -> str:
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    score = 5 - sum([length_error, uppercase_error, lowercase_error, digit_error, special_char_error])

    if score == 5:
        return "Strong "
    elif 3 <= score < 5:
        return "Moderate "
    else:
        return "Weak "

if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    print(f"Strength: {assess_password_strength(pwd)}")
