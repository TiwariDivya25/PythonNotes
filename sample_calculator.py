def calculator():
    result = float(input("Enter the first number: "))
    
    while True:
        operator = input("Enter operator (+, -, *, /, = to stop): ")
        
        if operator == "=":  # Stop the calculation
            break
        
        if operator not in ["+", "-", "*", "/"]:
            print("Invalid operator. Please try again.")
            continue
    
        n = float(input("Enter the next number: "))
        
        if operator == "+":
            result += n
        elif operator == "-":
            result -= n
        elif operator == "*":
            result *= n
        elif operator == "/":
            if n == 0:
                print("Division by zero is not allowed. Try again.")
                continue
            result /= n
    
    return result