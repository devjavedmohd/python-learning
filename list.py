import random


# states_of_india = ["Haryana", "Delhi", "Punjab", "UP", "Rajasthan"]
# print(f"The state is {states_of_india[random_number]}")

names = input("Please enter names of your family who need to pay? ")
make_list = names.split(",")

num_items = len(make_list)
random_number = random.randint(0, num_items - 1)

print(random_number)

who_paid = f"You have to paid {make_list[random_number]}"

print(who_paid)
