name = input("What is your Name?")

movie_above_16 = ["fast and furious", "Avengers", "Iron man", "Captain America"]
movie_for_16_and_below = ["Lion King", " Ice age", " Mowgli"]
movie_for_senior_citizen = [movie_above_16, movie_for_16_and_below]

user_prompt = True
while user_prompt:
    age = input("what is your age?")
    if age.isdigit():
        user_prompt = False


if int(age) <= 0:
    print(" Age cannot be negative")

elif 65 > int(age) > 16:
    print(f"Hi {name} you are {age} years old and you can buy tickets for these movies {movie_above_16}")

elif int(age) <= 16:
    print(f"Hi {name} you are {age} years old and you can buy tickets for these movies {movie_for_16_and_below} ")

else:
    print(f"Hi {name} you are {age} years old and you can enjoy all these movies {movie_for_senior_citizen}")
