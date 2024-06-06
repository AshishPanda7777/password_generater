import random
import string

def generate_password(length=8, include_digits=True, include_special_chars=True):
    chars = string.ascii_letters
    if include_digits:
        chars += string.digits
    if include_special_chars:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("Password Generator")
    length = int(input("Enter the length of the password: "))
    include_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    include_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

    password = generate_password(length, include_digits, include_special_chars)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
