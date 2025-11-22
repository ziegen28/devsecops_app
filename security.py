import re

def sanitize_input(text):
    # Prevent SQL Injection / XSS / Command injection
    blacklist = r"[;\'\"<>]"
    return re.sub(blacklist, "", text)

def is_strong_password(password):
    # MUST contain uppercase, lowercase, number, special char, length >= 8
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$"
    return bool(re.match(pattern, password))
