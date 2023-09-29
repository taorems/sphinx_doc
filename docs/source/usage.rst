Usage
=====

.. _installation:

Installation
------------

To use JSDL, first request access to the app on the MaxPortal:

.. code-block:: console

   (.venv) $ nx serve oss

Code Structure
--------------
.. _code-structure:

The code is structured as follows:

You can use the calculator class to perform various operations on numbers.

Sphinx supports documenting code objects in several languages, namely Python, C, C++, JavaScript, and reStructuredText. Each of them can be documented using a series of directives and roles grouped by domain.

Here is a sample of test python code:

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

This step is done by manual writing of the code documentation in the rst file.

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

This step is done by using the sphinx-autodoc extension.

you can use the ``lumache.test_doc()`` function:

.. autofunction:: lumache.test_doc

.. autofunction:: math_operations.test_doc

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError