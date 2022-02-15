##
 # @author Chandu D
 # @email chanduram.dowlathram@sap.com
 # @create date 2022-02-15 11:47:20
 # @modify date 2022-02-15 11:47:24
 # @desc [description]
##

from pydantic import BaseModel
from typing import Optional,List
from uuid import UUID,uuid4
from models.enums import Gender,Role

class User(BaseModel):
    id: Optional[str] = str(uuid4())
    first_name: str 
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]