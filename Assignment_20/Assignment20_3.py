import threading

def EvenList(arr):
    even_sum = 0
    for no in arr:
        if no % 2 == 0:
            print("Even element:", no)
            even_sum += no
    print("Sum of even elements:", even_sum)
    print()

def OddList(arr):
    odd_sum = 0
    for no in arr:
        if no % 2 != 0:
            print("Odd element:", no)
            odd_sum += no
    print("Sum of odd elements:", odd_sum)
    print()

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    t1 = threading.Thread(target=EvenList, args=(arr,), name="EvenList")
    t2 = threading.Thread(target=OddList, args=(arr,), name="OddList")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
