
class Calculator:
    def add(self, a, b=None, c=None):
        if b is None and c is None:
            return a
        elif c is None:
            return a + b
        else:
            return a + b + c

# Usage
calc = Calculator()
print(calc.add(5))          # Output: 5 (a)
print(calc.add(5, 10))      # Output: 15 (a + b)
print(calc.add(5, 10, 15))  # Output: 30 (a + b + c)