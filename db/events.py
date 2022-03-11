##
 # @author Chandu D
 # @email chanduram.dowlathram@sap.com
 # @create date 2022-02-15 11:49:14
 # @modify date 2022-02-22 23:01:29
 # @desc [description]
##

import logging
import azure.cosmos.documents as documents
from azure.cosmos.cosmos_client import CosmosClient
from fastapi import FastAPI
from api.dependencies.database import get_db_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey
import datetime
import resources.config as config
from resources.config import logger

HOST = config.settings['host']
MASTER_KEY = config.settings['master_key']
DATABASE_ID = config.settings['database_id']
CONTAINER_ID = config.settings['container_id']


async def bootstrap_database(app:FastAPI) -> None:
    try:
        client: CosmosClient = get_db_client(app)
        
        # if client:
        client.create_database_if_not_exists(id=DATABASE_ID)
        logger.info(f"Initialized DB-id: {DATABASE_ID}: sucessfully !")
    except Exception as e:
        logging.debug(e)