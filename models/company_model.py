from pydantic import BaseModel


class Company(BaseModel):
    comp_id:str
    comp_name:str
    comp_address: str