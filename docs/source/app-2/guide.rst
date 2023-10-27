Usage guide
===========

Installation
------------

Installation guide.

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


Codebase Description
----------------------------

Description on the codebase.

Comment operations
^^^^^^^^^^^^^^^^^^

To keep track of comments, a separate database is created.

The comment database is a list of comments, where each comment is a dictionary with the following keys:

- `comment`: The comment itself
- `operation_id`: The id of the operation that the comment is associated with
- `id`: The id of the comment


Frontend
--------

Dashboard
^^^^^^^^^

The dashboard is the landing page that displays the current status of the documentation. 

Description on the dashboard.

Operations
^^^^^^^^^^

Operations is the page that shows an overview of the operations that have been performed on the data.