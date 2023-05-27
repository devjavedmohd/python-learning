programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}


programming_dictionary["Loop"] = "The action of doing something again and again."
# print(programming_dictionary)

empty_dictionary = {}

# wiping or removing data of dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Editing dictionary
# programming_dictionary["Bug"] = "Update dictionary using like this:"
# print(programming_dictionary)

# Loop throught out the dictionary

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])