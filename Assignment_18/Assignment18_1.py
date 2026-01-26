def Addition(arr):
    return sum(arr)

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(Addition(arr))

if __name__ == "__main__":
    main()
