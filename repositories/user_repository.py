##
 # @author Chandu D
 # @email chanduram.dowlathram@sap.com
 # @create date 2022-02-15 11:49:38
 # @modify date 2022-02-15 11:49:39
 # @desc [description]
##
from ast import List
from asyncio.log import logger
from typing import Container
from azure.cosmos import CosmosClient,PartitionKey,ContainerProxy
from fastapi import HTTPException
from pydantic import BaseModel, parse_obj_as
from db.errors import UnableToAccessDatabase
from db.events import DATABASE_ID,CONTAINER_ID
from models.user_model import User
from repositories.base_repository import BaseRepository

PARTITION_KEY = PartitionKey(path="/userid")

class UserRepository(BaseRepository):
   
    def __init__(self,client:CosmosClient):
       super().__init__(client,CONTAINER_ID)
    
    
    def create_and_register_user(self,user_template:User)->dict:
        template = parse_obj_as(User,user_template)
        self.save_item(template)
        return template

    
    def getAllUsers(self)->list[User]:
        query = 'SELECT * FROM c'
    
        users_list = self.query(query=query)
        print(users_list)
        return [parse_obj_as(User,user)for user in users_list]

    def getUser(self,usr_id:str)->list[User]:
        print(f'Querying user Id : {usr_id}')
        query = f'SELECT * FROM c WHERE c.id=\"{usr_id}\"'
        print(query)
        users = self.query(query=query)
        print(users)
        return [parse_obj_as(User,user)for user in users]
    
    def update_user_info(self,user:User,usr_id:str)->dict:
        user_to_update:User = self.getUser(usr_id)[0]
        user_to_update.last_name = user.last_name
        user_to_update.first_name = user.first_name
        user_to_update.roles = user.roles
        self.update_item(user_to_update)
        return parse_obj_as(User,user_to_update)
    
    def del_user(self,usr_id:str)->dict:
        
        user_to_delete:User = self.getUser(usr_id)[0]
        
        if user_to_delete:
            self.delete_item(usr_id)
            return {"message": f"deleted user id {usr_id}"}
        
        raise HTTPException(
                status_code=404,
                detail=  f"User-id : {usr_id} does not exists"
            )