##
 # @author Chandu D
 # @email chanduram.dowlathram@sap.com
 # @create date 2022-02-15 11:47:42
 # @modify date 2022-02-15 11:47:43
 # @desc [description]
##
import os
from starlette.config import Config

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
