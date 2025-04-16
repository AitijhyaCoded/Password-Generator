import string
import random 

upc = string.ascii_uppercase
lwc = string.ascii_lowercase
num = string.digits
sym = string.punctuation

def password():
    char = int(input("Enter no. of characters(1-50):"))
    print("Choose:\n1.Uppercase Letters\n2.Lowercase Letters\n3.Numbers\n4.Symbols")
    user = eval(input("Enter choice in a list:"))
    pwd = ""
    if 1 in user:
        pwd += upc
    if 2 in user:
        pwd += lwc
    if 3 in user:
        pwd += num
    if 4 in user:
        pwd += sym
    if not pwd:
        return "Invalid selection"
    wt=[]
    for i in range(len(pwd)):
        wt.append(1)
    pwd = "".join(random.choices(population=pwd, k=char, weights=wt))

    def isStrong():
        strong = 0
        strength = {1:"very weak", 2:"weak", 3:"good", 4:"strong", 5:"very strong"}
        if 1<=char<=4:
            strong = 1
        elif 5<=char<=7:
            strong = 2
        elif 8<=char<=9:
            strong = 3
        elif 10<=char<=11:
            strong = 4
        else:
            strong = 5
        if len(user) == 1 and char<=25:
            return strength[strong-1]
        else:
            return strength[strong]

    print("Your " + isStrong() + " password is:")
    return pwd

print(password())
