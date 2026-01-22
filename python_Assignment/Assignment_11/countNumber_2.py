n = int(input("Enter Number :"))
count = 0

while n > 0:
    count += 1
    n //= 10

print(count)
