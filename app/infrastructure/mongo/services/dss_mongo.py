from pymongo import MongoClient
from infrastructure.mongo import mongo_helper
from core.services.document_storage_service import DocumentStorageService
from shared import utils

class DocumentStorageServiceMongo(DocumentStorageService):
    def __init__(self, mongoCredential:dict, databaseName: str, collectionName: str):
        self.mongoCredential = mongoCredential
        self.mongoClient : MongoClient = mongo_helper.createClient(self.mongoCredential)
        self.databaseName = databaseName
        self.db = self.mongoClient[databaseName]
        self.collection = self.db[collectionName]
        utils.hl(f'DocumentStorageServiceMongo: created for DB: [{databaseName}] collection [{collectionName}]')
    
    def getDocumentByID(self, id):
        mQuery = { '_id': id }
        return self.collection.find_one(mQuery)

    def getAllDocuments(self):
        mQuery = { 'deleted': False }
        cursor = self.collection.find(mQuery)
        ls = []
        for doc in cursor:
            ls += [doc]
        return ls

    def updateDocument(self, id, changes):
        mQuery = { '_id': id }
        return self.collection.update_one(mQuery, {'$set': changes})

    