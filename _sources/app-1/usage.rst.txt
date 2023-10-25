Usage
=====

.. _installation:

Installation
------------

To use this project, first create a virtual environment and clone the repository:

.. code-block:: console

   (.venv) $ git clone repo_url

Quickstart
----------

This is a quickstart guide to get the application up and running.

Dev Run
^^^^^^^

To run an instance of the app with a database included, run the powershell script run.dev.ps1.

To access the swagger interface go to http://localhost:8080/docs

A utility script is provided to create an asset and add operations to it. This script is located in the /app/utils/ folder and is called add_asset.py. The fastapi server needs to be running for it to work. The script can be run with the following command:

```bash
docker exec CONTAINER_ID python ./app/utils/add_asset.py
```

Where CONTAINER_ID is the ID of the container running the fastapi server, you can find this with `docker ps`.


Comment operations
^^^^^^^^^^^^^^^^^^

To keep track of comments, a separate database is created.

The comment database is a list of comments, where each comment is a dictionary with the following keys:

- `comment`: The comment itself
- `operation_id`: The id of the operation that the comment is associated with
- `id`: The id of the comment


Repository Structure
--------------------
.. _Repo-structure:

.. The repo is structured as follows:

.. .. figure:: _static/repo_structure.jpg
..    :align: center
..    :width: 100%
   
..    Fig: Repository Structure


The text below is written using 'code-block' directive:

.. code-block:: text
    
   project_root/
   ├── app-1/
   │   ├── code/
   │        ├── python_files.py
   ├── app-2/
   │   ├── code/
   |        ├── python_files.py
   ├── docs/
   │   ├── build/
   |       ├── html/
   │   ├── source/
   │   │   ├── conf.py
   |   |   ├── index.rst
   |   |   ├── app-1
   |   |       ├── usage.rst
   |   |       ├── quickstart.rst
   |   |       ├── api.rst
   |   |       ├── frontend.rst
   |   |       ├── _static/
   |   |   ├── app-2
   |   |       ├── quickstart.rst
   |   |       ├── _static/


Creating code documentation
---------------------------

This section elaborates on how to autodocument code. Here is a sample of test python code for lumache.py and math_operations.py:

.. code-block:: python
    :caption: lumache.py
    :name: lumache-py


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


.. code-block:: python
    :caption: math_operations.py
    :name: math_operations-py


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

.. note::
   The documentation is split in 2 categories. First, using manual writing of the code documentation in the rst file. Second, using the sphinx-autodoc extension. 

Manual approach
^^^^^^^^^^^^^^^

This section is done by manual writing of the code documentation in the rst file. The rst file is then converted to html using sphinx. Check the usage.rst file for the code documentation.

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. py:function:: lumache.get_random_ingredients(kind=None)

   Return a list of random ingredients as strings.

   :param kind: Optional "kind" of ingredients.
   :type kind: list[str] or None
   :raise lumache.InvalidKindError: If the kind is invalid.
   :return: The ingredients list.
   :rtype: list[str]

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. py:exception:: lumache.InvalidKindError

   Raised if the kind is invalid.

Using sphinx-autodoc extension
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The steps below are done by using the sphinx-autodoc extension. The sphinx-autodoc extension is used to automatically extract docstrings from modules and classes and format them in a way readable by Sphinx. 

.. note::
   The important thing for this to work is that the path of the code should be added to the sys.path variable. This can be done by adding the following line to the conf.py file:

   ``sys.path.insert(0, os.path.abspath('../../app-1/code'))``

   In the config file, there is also a system path as follows:

   ``sys.path.insert(0, pathlib.Path(__file__).parents[1].resolve().as_posix())``

   This is used to add the path of the code to the sys.path variable. This is done to be able to import the modules in the doc directory. Here, '.parents[2]' navigates up two levels in the directory hierarchy. parents[0] would represent the directory containing the current file, parents[1] would represent its parent directory, and parents[2] would represent its grandparent directory.

Here is the segment of the test:

You can type this line ``.. autofuntion:: lumache.test_doc`` to generate the documentation for the ``lumache.test_doc()`` function.

.. autofunction:: lumache.test_doc

The same approach can be applied for the ``math_operations.Calculator.add()`` function, which then generates the documentation for the ``math_operations.Calculator.add()`` function:

.. autofunction:: math_operations.Calculator.add

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError
