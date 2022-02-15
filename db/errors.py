##
 # @author Chandu D
 # @email chanduram.dowlathram@sap.com
 # @create date 2022-02-15 11:50:03
 # @modify date 2022-02-15 11:50:04
 # @desc [description]
##

from azure.cosmos.exceptions import ResourceNotFoundError

class UnableToAccessDatabase(ResourceNotFoundError):
     """Raised when we can't access the database"""