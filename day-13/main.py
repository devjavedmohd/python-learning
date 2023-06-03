# 1.
# def my_function():
#     for i in range(1, 20+1):
#         if i == 20:
#             print("You got it!")
#
#
# my_function()

# 2.
# from random import randint
#
# dice_img = ["1", "2", "3", "4", "5", "6"]
# dice_num = randint(0, 5)
# print(dice_num)
# print('Dice Img', dice_img[dice_num])

# 3.
# year = int(input("What's your year of birth?"))
#
# if year > 1980 and year < 1994:
#     print("You are a millennial")
# elif year >= 1994:
#     print("You are a Gen Z.")

# 4.
# age = int(input("How old are you?"))
#
# if age > 18:
#     print(f"You can drive at age {age}.")
# else:
#     print(f"You have to wait {18 - age} years")

# 5.
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(pages)
# print(word_per_page)
#
# print(total_words)

# 6.
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 4, 5, 6])