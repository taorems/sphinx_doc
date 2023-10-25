.. Test documentation master file, created by
   sphinx-quickstart on Tue Sep 26 12:42:49 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Test-app documentation!
======================================================

**Test** is a web application for testing the documentation of application. It is developed by the *A-team*.

The key focus points for this documentation are the followings:

1. Layout a stucture for the documentation of multiple web applications 
2. Implement automating code documentation from the source code

Scroll through the table of contents on the left to see what is available.

.. toctree::
   :maxdepth: 2
   :caption: app-1 Documentation
   :hidden:

   /app-1/intro
   /app-1/usage
   /app-1/api
      /app-1/backend 
   /app-1/frontend

.. toctree::
   :maxdepth: 2
   :caption: App-2 Documentation
   :hidden:

   /app-2/intro
   /app-2/api


.. warning::
   This documentation is still under development and is not intended to be used as a reference for any application.

.. note::

   This documentation is built using `Sphinx <http://sphinx-doc.org/>`_ and `Read the Docs <https://readthedocs.org/>`_. The source code is hosted on GitHub.
   Sphinx supports documenting code objects in several languages, namely Python, C, C++, JavaScript, and reStructuredText. Each of them can be documented using a series of directives and roles grouped by domain. 
