# Math operations module


class Calculator:
    """
    A class used to represent a calculator that performs basic arithmetic operations.

    """
    def __init__(self):
        """
        The constructor for Calculator class.

        """
        pass

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

def test_doc():
    """
    Return a list of random ingredients as strings.

   :param kind: Optional "kind" of ingredients.
   :type kind: list[str] or None
   :raise lumache.InvalidKindError: If the kind is invalid.
   :return: The ingredients list.
   :rtype: list[str]
   
    """
    return ["easy, peasy, lemon, squeezy"]