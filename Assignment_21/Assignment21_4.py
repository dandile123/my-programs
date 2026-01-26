import threading

sum_result = 0
product_result = 1

def SumList(arr):
    global sum_result
    sum_result = sum(arr)

def ProductList(arr):
    global product_result
    product_result = 1
    for no in arr:
        product_result *= no

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    t1 = threading.Thread(target=SumList, args=(arr,))
    t2 = threading.Thread(target=ProductList, args=(arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of elements:", sum_result)
    print("Product of elements:", product_result)

if __name__ == "__main__":
    main()
