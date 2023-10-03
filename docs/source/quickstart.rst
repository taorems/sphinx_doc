Quickstart
==========

This is a quickstart guide to get the application up and running.

Dev Run
-------

To run an instance of the app with a database included, run the powershell script run.dev.ps1.

To access the swagger interface go to http://localhost:8080/docs

Below the procedure to create an asset are described.

A utility script is provided to create an asset and add operations to it. This script is located in the /app/utils/ folder and is called add_asset.py. The fastapi server needs to be running for it to work. The script can be run with the following command:

```bash
docker exec CONTAINER_ID python ./app/utils/add_asset.py
```

Where CONTAINER_ID is the ID of the container running the fastapi server, you can find this with `docker ps`.

The script will create an asset, add operations to it, do equivalent damage and total damage calculations. The asset ID is printed to the console. This ID can be used to access the asset in the other endpoints.

### Creating an asset
To create asset for testing:
1. Access the swagger ui
2. Go to the `/api/v1/assets/upload_files` endpoint.

After execution you should see a succesfull response and the asset should be created in the database.

It is given an id, which is used to access the asset in the other endpoints.

### Adding operations to an asset
To add operations to an asset for testing:
1. Access the swagger ui
2. Go to the `/api/v1/operations/operations_from_json_file` endpoint.

After execution you should see a succesfull response with the created operations and the operations should be created in the database.

### Perform the calculations
To perform the calculations for testing:
1. Access the swagger ui
2. Go to the `/api/v1/logic/operations/update/{asset_id}` endpoint.

### To display the results for a dashboard call
1. Access the swagger ui
2. Go to the `/api/v1/logic/dashboard/update/{asset_id}` endpoint.


Comment operations
-------------------

To keep track of comments, a separate database is created.

The comment database is a list of comments, where each comment is a dictionary with the following keys:

- `comment`: The comment itself
- `operation_id`: The id of the operation that the comment is associated with
- `id`: The id of the comment

There is also a `delete_comment`  endpoint, which deletes a comment from the comment database.

Comments can be read in two ways:
- Using the `read_comments` GET endpoint, which returns all comments in the comment database for a given operation id.
- Using the `read_operation` GET endpoint, which returns the operation with the given id, including all comments.