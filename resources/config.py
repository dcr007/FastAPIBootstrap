##
 # @author Chandu D
 # @email chanduram.dowlathram@sap.com
 # @create date 2022-02-15 11:47:42
 # @modify date 2022-02-22 23:03:33
 # @desc [description]
##
import logging
import os
from starlette.config import Config
from pydantic import BaseModel

config = Config(".env")
#Cosmos DB settings
settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://visionone-datapool.documents.azure.com:443/'),
    'master_key': os.environ.get('ACCOUNT_KEY', 'G506A5TDmVt0nIpzA0r7NLXtGVCvw1hDLWVyv2x747L57YRcqUp6fZYLGrunVUhjQKlWdfW35W44Sg8Afm9mXg=='),
    'database_id': os.environ.get('COSMOS_USERS_DATABASE', 'UsersDb'),
    'container_id': os.environ.get('COSMOS_USERS_CONTAINER', 'UsersContainer')
}
#API Setttings
PROJECT_NAME: str = config("PROJECT_NAME", default="Fast API")
API_DESCRIPTION = "Sample Fast API project backed by Cosmos DB"
API_PREFIX = "/api/v1"
DEBUG: bool = config("DEBUG", cast=bool, default=False)

from pydantic import BaseModel


class LogConfig(BaseModel):
    """Logging configuration to be set for the server"""

    LOGGER_NAME: str = PROJECT_NAME
    LOG_FORMAT: str = "%(levelprefix)s  %(asctime)s | %(message)s"
    LOG_LEVEL: str = "DEBUG"

    # Logging config
    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers = {
        PROJECT_NAME: {"handlers": ["default"], "level": LOG_LEVEL},
    }
# export logger
logger = logging.getLogger(PROJECT_NAME)