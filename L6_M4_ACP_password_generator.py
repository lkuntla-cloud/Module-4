import random
import string
def generate_password(length=12):
    characters=string.ascii_letters + string.digits
    password_list=[random.choice(characters)for _ in range(length)]
    random.shuffle(password_list)
    password="".join(password_list)
    return password
new_password=generate_password(16)
print("Your random password is: ", new_password)