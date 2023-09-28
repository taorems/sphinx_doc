Quickstart
==========

This is a quickstart guide to get the application up and running. For more detailed information, see the [documentation](

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
1. Go to the `/api/v1/assets/upload_files` endpoint.
1. Give asset name in asset_name parameter
1. For file_bin_settings_parameter use /config/bin_settings.json file
1. For the file_design_life bin use /config/design_life.json
1. Execute the endpoint with the files.

After execution you should see a succesfull response and the asset should be created in the database.

It is given an id, which is used to access the asset in the other endpoints.

### Adding operations to an asset
To add operations to an asset for testing:
1. Access the swagger ui
1. Go to the `/api/v1/operations/operations_from_json_file` endpoint.
1. Give asset ID in asset_id parameter
1. For the file_operations bin use /config/operations.json
1. Execute the endpoint with the files.

After execution you should see a succesfull response with the created operations and the operations should be created in the database.

### Perform the calculations
To perform the calculations for testing:
1. Access the swagger ui
1. Go to the `/api/v1/logic/calculate_equivalent_distance/asset/{asset_id}` endpoint.
1. Give asset ID in asset_id parameter and execeute the endpoint.
1. This will calculate the equivalent distance for the asset and return the result.
1. Go to the `/api/v1/logic/calculate_total_damage/asset/{asset_id}/asset/{asset_id}` endpoint.
1. Give asset ID in asset_id parameter and execeute the endpoint.
1. This will calculate the total damage for the asset and return the result.

### To display the results for a dashboard call
1. Access the swagger ui
1. Go to the `/api/v1/logic/dashboard/update/{asset_id}` endpoint.
1. Give asset ID in asset_id parameter and execeute the endpoint.
1. This display the results of the equivalent distance and the total damage for the asset.

Comment operations
-------------------

To keep track of comments, a separate database is created.
Operations can, but do not have to, include comments. 
When the operation is made, the comment in the create operation call, if any, is added to the comment database as the first comment.
The comment database is a list of comments, where each comment is a dictionary with the following keys:

- `comment`: The comment itself
- `operation_id`: The id of the operation that the comment is associated with
- `id`: The id of the comment

In the backend there are two ways of adding comments to an operation.
- During a create operation call, the comment is added to the comment database as the first comment.
- Using the `add_comment` POST endpoint, a comment can be added to an existing operation, using its id

There is also a `delete_comment`  endpoint, which deletes a comment from the comment database.

Comments can be read in two ways:
- Using the `read_comments` GET endpoint, which returns all comments in the comment database for a given operation id.
- Using the `read_operation` GET endpoint, which returns the operation with the given id, including all comments.