Usage
=====

.. _installation:

Installation
------------

To use this project, first create a virtual environment and clone the repository:

.. code-block:: console

   (.venv) $ git clone repo_url

Repository Structure
--------------------
.. _Repo-structure:

The repo is structured as follows:

.. figure:: /_static/repo_structure.jpg
   :align: middle 
   :width: 90%
   :alt: Repository Structure

Repository Structure

The text below is written using 'code-block' directive:

.. code-block:: text

   project_root/
   ├── code/
   │   ├── lumache.py
   │   ├── other_python_files.py
   ├── docs/
   │   ├── build/
   │   ├── source/
   │   │   ├── conf.py


Creating code documentation
---------------------------

Here is a sample of test python code:

.. code-block:: python

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


.. note::
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

.. >>> import math_operations
.. >>> math_operations.test_doc()
.. 3
.. >>> import lumache

.. note::
   The steps below are done by using the sphinx-autodoc extension. The sphinx-autodoc extension is used to automatically extract docstrings from modules and classes and format them in a way readable by Sphinx. The important thing for this to work is that the path
   of the code should be added to the sys.path variable. This can be done by adding the following line to the conf.py file:

   ``sys.path.insert(0, os.path.abspath('../code'))``

   In the config file, there is also a system path as follows:

   ``sys.path.insert(0, pathlib.Path(__file__).parents[1].resolve().as_posix())``


Here is the segment of the test:

You can use the ``lumache.test_doc()`` function:

.. autofunction:: lumache.test_doc

You can use the ``math_operations.Calculator.add()`` function:

.. autofunction:: math_operations.Calculator.add

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError