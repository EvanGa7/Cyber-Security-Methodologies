# Evan Gardner
# CS-450 Cyber Security
# Professor Weihao
# September 27, 2023
# Weekly Assignment 3

import bcrypt
import pyotp
from getpass import getpass

# Initialize a TOTP object
totp = pyotp.TOTP(pyotp.random_base32())

# A function to hash a password using bcrypt and key stretching
def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt(rounds=14)
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

# A function to check the password against the hashed password
def check_password(password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

# A function for multi-factor authentication
def multi_factor_authentication() -> bool:
    print("This is your MFA token:", totp.now())
    token = input("Enter the token: ")
    return totp.verify(token)

# Main function
def main():
    print("Enter a password to hash:")
    password = getpass()  # Use getpass to hide the input
    hashed_password = hash_password(password)
    
    print("Now, let's verify the password.")
    password_to_check = getpass()
    
    if check_password(password_to_check, hashed_password):
        print("Password is correct.")
        if multi_factor_authentication():
            print("MFA verified. Access granted.")
        else:
            print("MFA verification failed. Access denied.")
    else:
        print("Incorrect password. Access denied.")

# Run the main function
if __name__ == '__main__':
    main()
