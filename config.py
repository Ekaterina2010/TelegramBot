from enum import Enum

token = '1292639481:AAFlpOQCr3yCwBXjOeZRDBzrr6ChAFfSXk8'

db_file = 'database.vdb'


class States(Enum):
    S_START = "0"
    S_ENTER_DAY = "1"
    S_COUNTRY_OR_REGION = "2"
    S_ENTER_COUNTRY_OR_REGION = "3"
    S_ENTER_FIELD_LIST = "4"
