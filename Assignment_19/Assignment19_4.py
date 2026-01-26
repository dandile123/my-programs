from functools import reduce

# Program 4
def program4():
    input_list = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

    # Filter even numbers
    even_nums = list(filter(lambda x: x % 2 == 0, input_list))

    # Square each number
    square_nums = list(map(lambda x: x * x, even_nums))

    # Add all using reduce
    result = reduce(lambda a, b: a + b, square_nums)

    print("Input List =", input_list)
    print("List after filter =", even_nums)
    print("List after map =", square_nums)
    print("Output of reduce =", result)


program4()
