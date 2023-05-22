import random

random_number = random.random() * 10
random_side = random.randint(0, 10)
print(random_side)

if random_number <= 5:
    print("Tails!")
elif random_number <= 10:
    print("Heads!")
else:
    print("Tied!")
