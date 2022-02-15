

from asyncio.log import logger
from typing import Callable,Type
from azure.cosmos import CosmosClient
from fastapi import FastAPI,Depends,HTTPException, Request
from starlette.status import HTTP_503_SERVICE_UNAVAILABLE
from repositories.base_repository import BaseRepository
from db.errors import UnableToAccessDatabase
from resources import config
import azure.cosmos.exceptions as exceptions

HOST = config.settings['host']
MASTER_KEY = config.settings['master_key']
DATABASE_ID = config.settings['database_id']
CONTAINER_ID = config.settings['container_id']

def get_repository(repo_type: Type[BaseRepository]) -> Callable[[CosmosClient], BaseRepository]:
    def _get_repo(client: CosmosClient = Depends(get_db_client_from_request)) -> BaseRepository:
        try:
            print('<-------------------------------------->')
            print('repository type resolved to : ',format(repo_type))
            print('<-------------------------------------->')
            return repo_type(client)
        except UnableToAccessDatabase:
            raise HTTPException(status_code=HTTP_503_SERVICE_UNAVAILABLE, detail="Api endpoint not responding")

    return _get_repo

def get_db_client(app: FastAPI) -> CosmosClient:
    # if not app.state.cosmos_client:
    app.state.cosmos_client = connect_to_db()
    return app.state.cosmos_client


def get_db_client_from_request(request: Request) -> CosmosClient:
    return get_db_client(request.app)


def connect_to_db() -> CosmosClient:
    logger.info(f"Connecting to {DATABASE_ID}")
    try:
        cosmos_client = CosmosClient(HOST, {'masterKey': MASTER_KEY}, user_agent="CosmosDBPythonQuickstart", user_agent_overwrite=True)
        return cosmos_client
    except exceptions.CosmosHttpResponseError as e:
        logger.debug(f"Connection to state store could not be established: {e}")
