list1 = [1000, 3000, 2500, 6000]


# def bonus():
#
#     for sal in list1:
#         list2 = sal * .10 + sal
#         print(list2)
#

# bonus()

bonus2 = list(map(lambda x: x * 1.1, list1))

print(bonus2)
