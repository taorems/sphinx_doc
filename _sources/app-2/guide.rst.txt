Usage Guide
***********

Installation
============

Installation guide.

Quickstart
==========

This is a quickstart guide to get the application up and running. To get started with the application, you need to first request access to the application via the portal.

Dev Run
-------

To run an instance of the app with a database included, run the powershell script run.dev.ps1.

To access the swagger interface go to http://localhost:8080/docs

A utility script is provided to create an asset and add operations to it. This script is located in the /app/utils/ folder and is called add_asset.py. The fastapi server needs to be running for it to work. The script can be run with the following command:

```bash
docker exec CONTAINER_ID python ./app/utils/add_asset.py
```

Where CONTAINER_ID is the ID of the container running the fastapi server, you can find this with `docker ps`.


Codebase Description
====================

Description on the codebase.

Assets
------	

What are assets? How are they stored?

Operations
^^^^^^^^^^

Operations performed on assets are called Operations. What are operations? How are they stored? 

Logic
-----

The logic of the application is contained in the /app/logic/ folder. Here, decription on the logic used in the application is provided.

.. autoclass:: logic.LegHandelingOperation
    :members: apply_mapping


CRUD Operations
---------------

Description on the CRUD operations.


Frontend
========

Dashboard
---------

The dashboard is the landing page that displays the current status of the documentation. 

Description on the dashboard.

Operations
----------

Operations is the page that shows an overview of the operations that have been performed on the data.