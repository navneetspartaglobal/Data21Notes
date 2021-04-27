from numbers import num_list
import random
# num = input("Enter the number")
# for x in range(int(num)):
#     if x % 3 == 0 and x % 5 == 0:
#         print("FizzBuzz")
#     elif x%3 == 0:
#         print("Fizz")
#     elif x%5 ==0:
#         print("Buzz")
#     else:
#         print(x)


for x in num_list:
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x%3 == 0:
        print("Fizz")
    elif x%5 ==0:
        print("Buzz")
    else:
        print(x)