n = int(input("Check this number: "))


def prime_checker(number):
    # Method 1
    # if number % 2 == 0:
    #     print("Number is not prime")
    # else:
    #     print("Number is prime")

    # Method 2
    # if number > 1:
    #     for i in range(2, number):
    #         if i % 2 == 0:
    #             print(f"{i} It's not a prime number")
    #         else:
    #             print(f"{i} It's a prime number")
    # else:
    #     print("It' not a prime number")

    # Method 3
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


prime_checker(number=n)
