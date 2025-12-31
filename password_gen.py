import random
import string

all_characters = string.ascii_letters + string.punctuation + string.digits
length = int(input("Length of password: "))
password = ''.join(random.choices(all_characters, k=length))
print("Generated Password: " + password)