# Math operations module


class Calculator:
    def add(self, x, y):
        """
        Perform addition of two numbers.

        Args:
            x (float or int): The first number.
            y (float or int): The second number.

        Returns:
            float or int: The result of the addition operation.
        """
        return x + y
    
    def subtract(self, x, y):
        """
        Perform subtraction of two numbers.

        Args:
            x (float or int): The first number.
            y (float or int): The second number.

        Returns:
            float or int: The result of the subtraction operation.
        """
        return x - y
    
    def multiply(self, x, y):
        """
        Perform multiplication of two numbers.

        Args:
            x (float or int): The first number.
            y (float or int): The second number.

        Returns:
            float or int: The result of the multiplication operation.
        """
        return x * y
    
    def divide(self, x, y):
        """
        Perform division of two numbers.

        Args:
            x (float or int): The numerator.
            y (float or int): The denominator.

        Returns:
            float or str: The result of the division operation. If division by zero occurs, returns "Cannot divide by zero."
        """
        if y == 0:
            return "Cannot divide by zero"
        return x / y