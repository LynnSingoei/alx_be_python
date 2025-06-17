def perform_operations(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'division':
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
    elif operation == 'multiply':
        return num1 * num2