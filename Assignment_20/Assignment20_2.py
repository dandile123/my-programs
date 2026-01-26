import threading

def EvenFactor(no):
    sum_even = 0
    for i in range(1, no + 1):
        if no % i == 0 and i % 2 == 0:
            print("Even factor:", i)
            sum_even += i
    print("Sum of even factors:", sum_even)

def OddFactor(no):
    sum_odd = 0
    for i in range(1, no + 1):
        if no % i == 0 and i % 2 != 0:
            print("Odd factor:", i)
            sum_odd += i
    print("Sum of odd factors:", sum_odd)

def main():
    num = int(input())

    t1 = threading.Thread(target=EvenFactor, args=(num,))
    t2 = threading.Thread(target=OddFactor, args=(num,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
