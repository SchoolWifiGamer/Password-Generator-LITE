import random
import string
import re


def generate_password(length=12, use_uppercase=True, use_numbers=True, use_symbols=True):
    """Generate a strong random password"""
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if len(characters) == 0:
        return "Error: No character types selected"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def check_password_strength(password):
    """Check the strength of a password"""
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters")

    strength_levels = ["Very Weak", "Weak", "Fair", "Strong", "Very Strong"]
    return min(score, 4), strength_levels[min(score, 4)], feedback



print("=== PASSWORD GENERATOR & STRENGTH CHECKER ===")


print("\nGenerated Passwords:")
for i in range(3):
    pwd = generate_password(length=12)
    strength, level, feedback = check_password_strength(pwd)
    print(f"{i+1}. {pwd} - {level}")

# Created by Gao Le
user_password = input("\nEnter a password to check strength: ")
strength, level, feedback = check_password_strength(user_password)
print(f"\nStrength: {level} ({strength}/4)")
if feedback:
    print("Suggestions:", ", ".join(feedback))
