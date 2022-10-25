from urllib.parse import quote
from pymongo import MongoClient
from core.services.minkey_service import MinkeyService
from shared import global_variables, utils

def createConnectionString(mongoCredential:dict):
    if 'connection_string' in mongoCredential:
        conStr = mongoCredential['connection_string']
        if conStr.startswith('minkey@'):
            minkeyService = MinkeyService(global_variables.getServiceConfig('MinKey'))
            key = conStr[7:]
            conStr = minkeyService.getString(key)
            utils.i(f"mongo_helper load connection string from MinKey [{key}]: {conStr}")
        return conStr

    host = mongoCredential['host']
    port = int(f"{mongoCredential['port']}")
    username = mongoCredential['username']
    password = mongoCredential['password']

    connectionStr = 'mongodb://{host}:{port}'
    if username != '' and password != '':
        pwdEncoded = quote(password)
        return 'mongodb://{user}:{pwd}@{host}:{port}/?authMechanism=DEFAULT'.format(user=username, pwd=pwdEncoded, host=host, port=port)
    return connectionStr

def createClient(mongoCredential:dict):    
    connectionStr = createConnectionString(mongoCredential)
    return MongoClient(connectionStr)
    