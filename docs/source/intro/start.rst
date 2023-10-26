Getting Started
===============

To get started with the documentation, first create a new repository on GitHub or use an existing project repo, then clone it locally:

.. code-block:: bash

   $ git clone repo_url

In the local directory where the repo has been cloned, create a new virtual environment and install sphinx:

.. code-block:: bash

   $ python -m venv .venv
   $ .\.venv\Scripts\Activate.ps1
   (.venv) $ pip install sphinx

.. note::
   Make sure to installed other dependencies as well in the virtual environment, if any.

If everything is installed correctly, you should be able to run the following command to create a new sphinx project:

.. code-block:: bash

   (.venv) $ sphinx-quickstart docs

Few prompts may pop-up, requesting user inputs for setting up the directory. Follow along and this will create a new directory called `docs` with the following structure:

.. code-block:: text

   docs/
   ├── make.bat
   ├── Makefile
   ├── build/
   ├── source/
   │   ├── conf.py
   │   ├── index.rst
   │   ├── _static/
   │   └── _templates/
   └── _build/

The purpose of these files are:

- `make.bat` and `Makefile` are used to build the documentation.
- `build` is the directory where the rendered documentation is stored.
- `source/config.py` is the configuration file for the Sphinx project. It contains the project metadata, the list of extensions used, and the configuration settings for each extension.
- `source/index.rst` is the root document for the documentation, which serves as the welcome page for the documentation and contains the table of contents tree (toctree).
- `source/_static` is the directory where static files such as images, CSS, and JavaScript files are stored.
- `source/_templates` is the directory where custom templates are stored.

Now, to build the documentation site locally, run the following command:

.. code-block:: bash

   (.venv) $ cd docs
   (.venv) $ make html

.. note::
   The `make html` command will generate the documentation in the `build/html` directory. To view the documentation, open the `index.html` file in a web browser. 

When writing documentation for multiple applications, it is recommended to create a separate directory for each application and organise the repository. This is explained in the next section.

Repository Structure
--------------------
.. _Repo-structure:

.. The repo is structured as follows:

.. .. figure:: _static/repo_structure.jpg
..    :align: center
..    :width: 100%
   
..    Fig: Repository Structure

If the project has two applications, app-1 and app-2, then create two directories, app-1 and app-2, alongside the documentation directory 'docs'. Create the same app-1 and app-2 directory under the `docs/source` directory as well. The directory structure should look like this:

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
   |   ├── make.bat
   |   ├── Makefile
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
      the following .yml workflow is added for GitHub Actions.

      .. literalinclude:: ../../../.github/workflows/doc.yml
         :language: yml
         :linenos:
         :caption: doc.yml

   .. tab:: Other

      Other documentation generator setup.

.. note::
   The `gh-pages` branch is not created by the user. It is created when the workflow is run via GitHub Actions, which is initiated when a push is made to the main branch as indicated in the doc.yml file. 
   After the `gh-pages` branch is created, set the GitHub pages deployment branch to `gh-pages` from the repository settings, as shown in the image below. 

.. figure:: ../_static/gh-pages.jpg
   :align: center
   :width: 100%
   
   GitHub-Pages Settings
