from functools import reduce

# Question 3
def question3():
    input_list = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

    # filter numbers >=70 and <=90
    filtered = list(filter(lambda x: x >= 70 and x <= 90, input_list))

    # add 10 to each number
    mapped = list(map(lambda x: x + 10, filtered))

    # product of all numbers
    result = reduce(lambda a, b: a * b, mapped)

    print("Input List =", input_list)
    print("List after filter =", filtered)
    print("List after map =", mapped)
    print("Output of reduce =", result)

question3()
