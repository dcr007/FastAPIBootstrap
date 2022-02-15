##
 # @author Chandu D
 # @email chanduram.dowlathram@sap.com
 # @create date 2022-02-15 11:47:51
 # @modify date 2022-02-15 11:47:52
 # @desc [description]
##

from fastapi import APIRouter, Depends, HTTPException, status
from api.dependencies.database import get_repository

from models.user_model import User
from repositories.user_repository import UserRepository


router = APIRouter()


@router.get("/getUsers", name="get list of users ")
async def get_User() -> str:
    return 'all user list'

@router.post("/registerUser", name="Saves a New users into DB",status_code=status.HTTP_201_CREATED,response_model=User)
async def post_user(user_payload:User,user_repo=Depends(get_repository(UserRepository))) -> dict:
    try:
        return user_repo.create_and_register_user(user_payload)
    except Exception:
        raise Exception('Exception while registering user')


@router.get("/getAllUsers", name="Fetches all Registered users",status_code=status.HTTP_200_OK,response_model=list[User])
async def get_all_users(user_repo=Depends(get_repository(UserRepository))) -> list[User]:
    
    users = user_repo.getAllUsers()
    return users


@router.get("/getUser/{user_id}", name="Fetches all Registered users",status_code=status.HTTP_200_OK,response_model=list[User])
async def get_user(user_id:str,user_repo=Depends(get_repository(UserRepository))) -> list[User]:
    return user_repo.getUser(user_id)
    
@router.put("/modifyUser/{user_id}", name="Updates user info",status_code=status.HTTP_200_OK,response_model=User)
async def modify_user(update_user:User,user_id:str,user_repo=Depends(get_repository(UserRepository))) -> User:
    return user_repo.update_user_info(update_user,user_id)


@router.delete("/delUser/{user_id}", name="Deletes a user",status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id:str,user_repo=Depends(get_repository(UserRepository))) -> None:
    user_repo.del_user(user_id)
    return