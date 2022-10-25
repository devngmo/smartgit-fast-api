import os, sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

APP_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(APP_DIR)
sys.path.append(os.path.dirname(APP_DIR))

from shared import utils, global_variables
from routers import repository_commands, project_commands
import apidefs
ALLOW_CREDENTIALS = utils.getEnvBool('ALLOW_CREDENTIALS', False)
ALLOW_ORIGINS = utils.getEnvValue('ALLOW_ORIGINS', '*').split(',')
ALLOW_METHODS = utils.getEnvValue('ALLOW_METHODS', '*').split(',')
ALLOW_HEADERS = utils.getEnvValue('ALLOW_HEADERS', '*').split(',') 

app = FastAPI(openapi_tags=apidefs.tags_metadata, title=apidefs.API_TITLE, version=global_variables.getVersionName())
app.add_middleware(
    CORSMiddleware,
    allow_origins = ALLOW_ORIGINS,
    allow_credentials=ALLOW_CREDENTIALS,
    allow_methods = ALLOW_METHODS,
    allow_headers = ALLOW_HEADERS
)

app.include_router(repository_commands.router)
app.include_router(project_commands.router)

@app.get("/")
def welcome():
    return f'welcome to SmartGit API ver. {global_variables.getVersionName()}'
