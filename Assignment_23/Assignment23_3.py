class Numbers:
    # constructor
    def __init__(self):
        self.Value = int(input("Enter a number: "))

    # check prime
    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    # return sum of factors
    def SumFactors(self):
        total = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                total += i
        return total

    # check perfect number
    def ChkPerfect(self):
        return self.SumFactors() == self.Value

    # display all factors
    def Factors(self):
        print("Factors are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()


# creating multiple objects
Obj1 = Numbers()
Obj2 = Numbers()

# calling methods for first object
print("Is Prime:", Obj1.ChkPrime())
print("Is Perfect:", Obj1.ChkPerfect())
Obj1.Factors()
print("Sum of Factors:", Obj1.SumFactors())

print("----------------------")

# calling methods for second object
print("Is Prime:", Obj2.ChkPrime())
print("Is Perfect:", Obj2.ChkPerfect())
Obj2.Factors()
print("Sum of Factors:", Obj2.SumFactors())
