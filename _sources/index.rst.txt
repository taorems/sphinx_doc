.. Test documentation master file, created by
   sphinx-quickstart on Tue Sep 26 12:42:49 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to App Documentation
=================================

This is a documentation page to test on application documentation for a generic app called **app-1**. It is developed by the *team-name*.

The key focus points for this documentation are the followings:

#. How to setup a documentation for a web application using GitHub pages.
#. Lay out a structure for the documentation of multiple web applications within a single repository.
#. Implement automatic code documentation from the source code.


.. toctree::
   :maxdepth: 2
   :hidden:

   intro/gettingstarted

.. toctree::
   :maxdepth: 2
   :caption: app-1 Documentation
   :hidden:

   app-1/intro
   app-1/guide
   app-1/api
   app-1/frontend

.. toctree::
   :maxdepth: 2
   :caption: app-2 Documentation
   :hidden:

   app-2/intro
   app-2/guide
   app-2/api

Use Case
--------

The use case of such a documentation are as follows:

#. To provide a single source of documentation for multiple web applications. 
#. The documentation is generated automatically from the source code and is hosted on GitHub pages. This way, the documentation is always up-to-date with the source code and the developers do not have to spend time on writing documentation. 
#. It is easily readable and accessible for the users of the application to validate the logic used in the application, rather then reading the source code. 

Scroll through the table of contents on the left to see what is available.

.. warning::
   This documentation is still under development and is not intended to be used as a reference for any application.

.. note::

   This documentation is built using `Sphinx <http://sphinx-doc.org/>`_. The source code is hosted on GitHub.
   Sphinx supports documenting code objects in several languages, namely Python, C, C++, JavaScript, and reStructuredText. Each of them can be documented using a series of directives and roles grouped by domain. More on this can be found `here <https://www.sphinx-doc.org/en/master/index.html>`_.
