def perform_operation(num1, num2, operation):
    """
    Perform an arithmetic operation on two numbers.

    Parameters:
        num1 (float or int): The first number.
        num2 (float or int): The second number.
        operation (str): The operation to perform. Supported values are
                         'add', 'subtract', 'multiply', 'divide'.

    Returns:
        float or int: The result of the arithmetic operation.
        str: An error message if the operation is invalid or division by zero occurs.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
if __name__ == "__main__":
    # Example usage
    print(perform_operation(10, 5, 'add'))        # Output: 15
    print(perform_operation(10, 5, 'subtract'))   # Output: 5
    print(perform_operation(10, 5, 'multiply'))   # Output: 50
    print(perform_operation(10, 0, 'divide'))     # Output: Error: Cannot divide by zero
    print(perform_operation(10, 5, 'divide'))     # Output: 2.0
    print(perform_operation(10, 5, 'modulus'))    # Output: Error: Invalid operation