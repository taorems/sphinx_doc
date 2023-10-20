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

class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass