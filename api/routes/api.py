##
 # @author Chandu D
 # @email chanduram.dowlathram@sap.com
 # @create date 2022-02-15 11:44:40
 # @modify date 2022-02-15 11:46:32
 # @desc [main router api to configure and add other routes]
##

from fastapi import APIRouter
from resources import config
from api.routes.users import user_route

router = APIRouter()

root_router = APIRouter()
core_router = APIRouter(prefix=config.API_PREFIX)


@root_router.get("/")
def root():
    return {"message": "welcome to Fast API homepage !"}

@root_router.get("/health")
def health():
    return {"message": "I'm up and running!"}

router.include_router(root_router, tags=['App'])

core_router.include_router(user_route.router,tags=["Users"])
router.include_router(core_router)

