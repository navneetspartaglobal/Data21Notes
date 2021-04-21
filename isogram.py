## Isogram program ##

word = input("Enter the word")
letter_list = []

for letter in word:
    if letter in letter_list:
        print("Word is not isogram")
    letter_list.append(letter)

print("Word is isogram")





