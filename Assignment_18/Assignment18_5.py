import MarvellousNum

def ListPrime(arr):
    total = 0
    for no in arr:
        if MarvellousNum.ChkPrime(no):
            total = total + no
    return total

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(ListPrime(arr))

if __name__ == "__main__":
    main()
