scores = input("Please enter scores of students in class x: ").split()
print(scores)


for i in range(len(scores)):
    scores[i] = int(scores[i])

highest_score = 0
lowest_score = scores[0]

for score in scores:
    if score > highest_score:
        highest_score = score

for score in scores:
    if score < lowest_score:
        lowest_score = score

print(f"The highest score in the class x is: {highest_score}")
print(f"The lowest score in the class x is: {lowest_score}")
