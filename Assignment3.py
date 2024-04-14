class EuclideanAlgorithm:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_gcd(self):
        a, b = self.a, self.b
        while b != 0:
            a, b = b, a % b
        return a

def main():
    try:
        a = int(input("Enter the first number (must be positive integer): "))
        b = int(input("Enter the second number (must be positive integer): "))
        if a <= 0 or b <= 0:
            raise ValueError("Numbers must be positive integers.")
        gcd_calculator = EuclideanAlgorithm(a, b)
        print(f"The GCD of {a} and {b} is: {gcd_calculator.calculate_gcd()}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
