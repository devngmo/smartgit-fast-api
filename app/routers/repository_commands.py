from fastapi import APIRouter, HTTPException
from shared import global_variables

from core.repositories.project_repository import ProjectRepository
from infrastructure.mongo.services.dss_mongo import DocumentStorageServiceMongo
from core.services.minkey_service import MinkeyService

router = APIRouter(
    prefix='/api/v1/repository',
    tags=['Repository Commands'],
    responses={404: {"description": "Not found"}}
)

minkeyService = MinkeyService(global_variables.getServiceConfig('MinKey'))
storage = DocumentStorageServiceMongo(global_variables.getServiceConfig('DocumentStorageServiceMongo'), databaseName='smartgit', collectionName='projects')
projectRepo = ProjectRepository(storage)

@router.get("/{project_id}/pull", description="Pull source to project folder")
async def pull_source_to_project_folder(project_id:str):
    projectInfo = projectRepo.getProjectByID(project_id)
    if projectInfo == None:
        return HTTPException(status_code=404, detail=f'Project not found: {project_id}')
    
    sourceFolder = minkeyService.autoGet(projectInfo.folder_path)
    

    