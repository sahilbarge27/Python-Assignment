class Numbers:
    def _init_(self, value):
        self.value = value

    def ChkPrime(self):
        if self.value <= 1:
            return False
        for i in range(2, self.value):
            if self.value % i == 0:
                return False
        return True

    def Factors(self):
        print("Factors:")
        for i in range(1, self.value + 1):
            if self.value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        total = 0
        for i in range(1, self.value + 1):
            if self.value % i == 0:
                total += i
        return total

    def ChkPerfect(self):
        return self.SumFactors() - self.value == self.value


# Example usage
num = int(input("Enter a number: "))
obj = Numbers(num)

print("Prime:", obj.ChkPrime())
print("Perfect:", obj.ChkPerfect())
obj.Factors()
print("Sum of Factors:", obj.SumFactors())