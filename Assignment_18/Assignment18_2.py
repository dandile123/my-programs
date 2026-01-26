def Maximum(arr):
    return max(arr)

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(Maximum(arr))

if __name__ == "__main__":
    main()
