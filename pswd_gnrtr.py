import random
import string

def password_generator(length):
    if length<8:
        return "Error: Password length should be at least 8 characters"
    
    password_characters=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(password_characters)for i in range(length))
    
    return password

password_length=int(input("Enter the desired password length: "))
password=password_generator(password_length)
print("Generated Password:", password)
