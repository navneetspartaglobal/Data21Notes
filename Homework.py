name = input("What is your Name?")
age = int(input("what is your age?"))
#
# user_prompt = True;
#
# while user_prompt:
#     age=input("what is your age?")
#     if age.isdigit():
#         user_prompt = False
#user_prompt = True
while True:
    if age <= 0:
        print(" Age cannot be negative")
        break

    elif 70 > age > 16:
        print(f"Hi {name} you are {age} years old and you can buy General audience ticket")
        break
    elif age <= 16:
        print(f"Hi {name} you are {age} years old and you can not buy tickets without parental guidance")
        break
    else:
        print(f"Hi {name} you are {age} years old and you can enjoy senior citizen privileges")
        break
# while True:
#     age = int(input("what is your age?"))
#     if age > 16:
#        print(f"Hi {name} you are {age} years old and you can buy General audience")
#     elif age<=16:
#        print(f"Hi {name} you are {age} years old and you can not buy tickets without parental audience")
#     else:
#         print("please provide your answer as a positive digit")
