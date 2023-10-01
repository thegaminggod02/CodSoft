# Step 1: Importing Modules
import random
import string

# Step 2: Generating Password
def generate(l=12):
    low=string.ascii_lowercase
    upper=string.ascii_uppercase
    digits=string.digits
    char="!@#$%^&*()_+={}[]|\/:;?"

    a=low+upper+digits+char

    if l <= 7:
        print("Password is weak")
        return None

    pwd=[random.choice(low),random.choice(upper),random.choice(digits),random.choice(char)]

    rem=l-4
    for _ in range(rem):
        pwd.append(random.choice(a))

    random.shuffle(pwd)

    pwd=''.join(pwd)

    return pwd

# Step 3: Main Function
if __name__=="__main__":
    pwd_len = int(input("Enter length of password: "))
    r_pwd = generate(pwd_len)

    if r_pwd:
        print("Generated Password: ",r_pwd)
