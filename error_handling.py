while True:
    try:
        # Get two numbers from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    
        result = num1 / num2
        
        print(f"Result of division: {result}")
        break
    
    except ValueError:
        print("Error: Please enter valid numbers (not text).")
    
    except ZeroDivisionError:
        print("Error: Cannot divide by zero. Please enter a non-zero second number.")