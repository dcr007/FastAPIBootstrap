##
 # @author Chandu D
 # @email chanduram.dowlathram@sap.com
 # @create date 2022-02-15 11:42:36
 # @modify date 2022-02-22 23:00:36
 # @desc  [This the main file to bootstrap the applicaiton.Create a virtual envirronment and install all dependencies.]
##
 
import logging
from logging.config import dictConfig
from resources import config
# from resources.log_config import LogConfig
from resources.config import logger
from resources.config import LogConfig
from fastapi import FastAPI
import uvicorn


from resources.events import create_start_app_handler
from api.routes.api import router as api_router


# Initailizes logging
dictConfig(LogConfig().dict())


def get_application() -> FastAPI():
    application = FastAPI(
        title= config.PROJECT_NAME,
        description = config.API_DESCRIPTION,
    )
    # application.logger = logger
    application.add_event_handler("startup",create_start_app_handler(application))
    application.include_router(api_router)
    
    return application

app = get_application()

if __name__ == "__main__":
    
    logger.info("This is  Info")
    logger.error("It's a  Error")
    logger.debug("For Debug")
    logger.warning("Its a  Warning")
    logger.info("************Starting app**************")
    uvicorn.run("__main__:app", host="127.0.0.1", port=8009, reload=True)
