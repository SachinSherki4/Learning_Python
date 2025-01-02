def check_given_no_is_prime_or_not(number):
    is_prime = True
    for n in range(2, number // 2 + 1):
        if number % n == 0:
            is_prime = False
            break
    if is_prime:
        print(f"Given Number {number} is an Prime Number.\n")
    else:
        print(f"Given Number {number} is not an Prime Number.\n")


def check_prime_no_in_given_range(number_range):
    prime_no = []
    for number in range(2, number_range + 1):
        is_prime = True
        for n in range(2, number // 2 + 1):
            if number % n == 0:
                is_prime = False
                break
        if is_prime:
            prime_no.append(number)
    print(f"Range '{number_range}' contain following '{len(prime_no)}' prime numbers : {prime_no}")


check_given_no_is_prime_or_not(7)
check_prime_no_in_given_range(100)