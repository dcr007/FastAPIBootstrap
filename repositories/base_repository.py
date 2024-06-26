##
 # @author Chandu D
 # @email chanduram.dowlathram@sap.com
 # @create date 2022-02-15 11:50:57
 # @modify date 2022-03-11 15:18:35
 # @desc [description]
##

from asyncio.log import logger
from typing import Container
from azure.cosmos import CosmosClient,PartitionKey,ContainerProxy
from pydantic import BaseModel
from models.user_model import User
from db.errors import UnableToAccessDatabase
from xmlrpc.client import boolean
from azure.cosmos.database import DatabaseProxy,ContainerProxy
import resources.config as config
import azure.cosmos.exceptions as exceptions

PARTITION_KEY = PartitionKey(path="/id")
DATABASE_ID = config.settings['database_id']

class BaseRepository():
   def __init__(self,client:CosmosClient,container_name:str = None,partition_key:PartitionKey=None)-> None:
        self._client: CosmosClient = client
        self._container: ContainerProxy = self._get_container(container_name,partition_key)
        self._partition_key:PartitionKey = partition_key
    
   @property
   def container(self) -> ContainerProxy:
        return self._container

   def _get_container(self, container_name,partition_key) -> ContainerProxy:
        try:
            database = self._client.get_database_client(DATABASE_ID)
            container = database.create_container_if_not_exists(id=container_name, partition_key=partition_key)
            properties = container.read()
            print(properties['partitionKey'])
            return container
        except UnableToAccessDatabase:
            logger.error('Database with id \'{0}\' was not found'.format(DATABASE_ID))

   def query(self, query: str):
        return list(self.container.query_items(query=query, enable_cross_partition_query=True))

   def read_item_by_id(self, item_id: str) -> dict:
      return self.container.read_item(item=item_id, partition_key=item_id)

   def save_item(self, item: User):
      self.container.create_item(body=item.dict())

   def update_item(self, item: User):
      self.container.upsert_item(body=item.dict())

   def delete_item(self, item_id: str):
        self.container.delete_item(item=item_id, partition_key=item_id)

   def drop_container(db:DatabaseProxy, id:ContainerProxy)->boolean:
    print("\n Executing Delete Container")

    try:
        db.delete_container(id)
        print('Container with id \'{0}\' was deleted'.format(id))
        return True

    except exceptions.CosmosResourceNotFoundError:
        print('A container with id \'{0}\' does not exist'.format(id))
        return False
   
   def drop_database(db:DatabaseProxy, client:CosmosClient)->boolean:
    print("\n Executing Delete Database")

    try:
        client.delete_database(db)
        print('Database with id \'{0}\' was deleted'.format(db))
        return True

    except exceptions.CosmosResourceNotFoundError:
        print('A Database with id \'{0}\' does not exist'.format(id))
        return False