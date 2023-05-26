import math

wall_h = input("Enter wall height: ")
wall_w = input("Enter wall width: ")
coverage = 5


def paint_calc(cover, width, height):
    number_of_cans = math.ceil((int(height) * int(width)) / cover)
    # number_of_cans = round((int(height) * int(width)) / cover)
    print(f"You will need {number_of_cans} cans of paint.")


paint_calc(cover=coverage, height=wall_h, width=wall_w)
