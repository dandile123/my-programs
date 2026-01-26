def Minimum(arr):
    return min(arr)

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(Minimum(arr))

if __name__ == "__main__":
    main()
