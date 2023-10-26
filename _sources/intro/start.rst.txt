Getting Started
===============

To create such a project, first create a new repository on GitHub, then clone it locally:

.. code-block:: bash

   $ git clone repo_url

Then, create a new virtual environment and install the dependencies:

.. code-block:: bash

   $ python -m virtualenv venv
   $ source venv/bin/activate
   $ pip install -r requirements.txt


Repository Structure
--------------------
.. _Repo-structure:

.. The repo is structured as follows:

.. .. figure:: _static/repo_structure.jpg
..    :align: center
..    :width: 100%
   
..    Fig: Repository Structure


This is the structure of the repository which host multiple applications, for instance, app-1, app-2, etc. along with the documentation directory. 

.. code-block:: text
    
   project_root/
   ├── .github/
   |   ├── workflows/
   ├── app-1/
   │   ├── code/
   │       ├── python_files.py
   ├── app-2/
   │   ├── code/
   |       ├── python_files.py
   ├── docs/
   │   ├── build/
   |       ├── html/
   │   ├── source/
   │       ├── conf.py
   |       ├── index.rst
   |       ├── app-1
   |       |   ├── intro.rst
   |       |   ├── usage.rst
   |       |   ├── api.rst
   |       |   ├── frontend.rst
   |       |   ├── _static/
   |       |         ├── swaggerui/
   |       ├── app-2
   |           ├── intro.rst
   |           ├── usage.rst
   |           ├── api.rst
   |           ├── _static/

Configuring GitHub Pages
------------------------

In order to setup the github-pages for automatic generation of documentation, the following workflow is added:

.. tabs::

   .. tab:: Sphinx

      Since this project uses Sphinx,
      the following .yml workflow is added for git-actions.

      .. literalinclude:: ../../.github/workflows/doc.yml
         :language: yml
         :linenos:
         :caption: doc.yml

   .. tab:: Other

      Other documentation generator setup.

.. note::
   The `gh-pages` branch is not created by the user. It is created when the workflow is run via git-actions, which is activated when a push is made to the main branch as indicated in the doc.yml file. 
   After the `gh-pages` branch is created then set the GitHub pages deployment branch to `gh-pages` from the repository settings, as shown in the image below. 

.. figure:: _static/gh-pages.jpg
   :align: center
   :width: 100%
   
   GitHub-Pages Settings
