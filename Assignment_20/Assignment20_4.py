import threading

def Small(str1):
    count = 0
    for ch in str1:
        if ch.islower():
            count += 1
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Lowercase count:", count)
    print()

def Capital(str1):
    count = 0
    for ch in str1:
        if ch.isupper():
            count += 1
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Uppercase count:", count)
    print()

def Digits(str1):
    count = 0
    for ch in str1:
        if ch.isdigit():
            count += 1
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Digit count:", count)
    print()

def main():
    str1 = input()

    t1 = threading.Thread(target=Small, args=(str1,), name="Small")
    t2 = threading.Thread(target=Capital, args=(str1,), name="Capital")
    t3 = threading.Thread(target=Digits, args=(str1,), name="Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()
