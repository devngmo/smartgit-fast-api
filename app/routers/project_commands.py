from fastapi import APIRouter, HTTPException
from shared import global_variables, utils

from core.repositories.project_repository import ProjectRepository
from infrastructure.mongo.services.dss_mongo import DocumentStorageServiceMongo

router = APIRouter(
    prefix='/api/v1',
    tags=['Project Commands'],
    responses={404: {"description": "Not found"}}
)

storage = DocumentStorageServiceMongo(global_variables.getServiceConfig('DocumentStorageServiceMongo'), databaseName='smartgit', collectionName='projects')
projectRepo = ProjectRepository(storage)

@router.get("/projects", description="Get all projects")
async def get_all_project():
    utils.hl("get all projects:")
    ls = projectRepo.getAllProjects()
    utils.i(ls)
    return ls
    

    