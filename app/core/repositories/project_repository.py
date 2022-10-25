from core.services.document_storage_service import DocumentStorageService

class ProjectRepository:
    def __init__(self, storage: DocumentStorageService):
        self.dbID = 'projects'
        self.storage = storage

    def getProjectByID(self, id):
        return self.storage.getDocumentByID(id)

    def getAllProjects(self):
        return self.storage.getAllDocuments()

    def updateProject(self, id, changes):
        return self.storage.updateDocument(id, changes)
