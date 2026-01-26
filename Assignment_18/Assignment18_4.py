def Frequency(arr, search):
    return arr.count(search)

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    search = int(input())
    print(Frequency(arr, search))

if __name__ == "__main__":
    main()
