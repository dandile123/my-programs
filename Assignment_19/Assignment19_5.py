from functools import reduce

# Correct prime function
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):   # fixed square root
        if n % i == 0:
            return False
    return True

# Program 5
def program5():
    input_list = [2, 70, 11, 10, 17, 23, 31, 77]

    # Filter prime numbers
    primes = list(filter(is_prime, input_list))

    # Multiply each prime by 2
    mapped_list = list(map(lambda x: x * 2, primes))

    # Reduce to get max
    result = reduce(lambda a, b: a if a > b else b, mapped_list)

    print("Input List =", input_list)
    print("List after filter =", primes)
    print("List after map =", mapped_list)
    print("Output of reduce =", result)

program5()
