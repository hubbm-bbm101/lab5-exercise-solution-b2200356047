user_email= input("please enter your e-mail address: ")
list_of_letters = list(user_email)
a=0
b=0
for letter in list_of_letters:
    if letter =="@":
        a=1
    elif letter ==".":
        b=1
if (a>=1 and b>=1 ):
    print("It is a valid e-mail")
else:
    print("It is not a valid e-mail")






