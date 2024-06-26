##
 # @author Chandu D
 # @email chanduram.dowlathram@sap.com
 # @create date 2022-02-15 11:48:10
 # @modify date 2022-02-22 19:58:46
 # @desc [description]
##

from typing import Callable

from fastapi import FastAPI

from db.events import bootstrap_database

def create_start_app_handler(app: FastAPI) -> Callable:
    async def start_app() -> None:
        # app.state.cosmos_client = None
        await bootstrap_database(app)

    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:
    async def stop_app() -> None:
        pass
    return stop_app