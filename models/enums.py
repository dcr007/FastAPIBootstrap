##
 # @author Chandu D
 # @email chanduram.dowlathram@sap.com
 # @create date 2022-02-15 11:50:23
 # @modify date 2022-02-15 11:50:26
 # @desc [description]
##

from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"