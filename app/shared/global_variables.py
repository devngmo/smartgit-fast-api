from datetime import datetime, timezone
import os, yaml
from shared import utils

STARTUP_TIME = datetime.now(timezone.utc)

LOG_LV_ALL = 0
LOG_LV_INFO = 1
LOG_LV_DEBUG = 2
LOG_LV_WARN = 3
LOG_LV_ERROR = 4
LOG_LV_FATAL_ERROR = 5

CODE_RELEASE_DATE = '2022-10-25 8:00'

config = {}
CONFIG_FILE = utils.getEnvValue('CONFIG_FILE', 'smartgit')
CONFIG_FOLDER = utils.getEnvValue('CONFIG_FOLDER', os.path.join(os.getcwd(), 'configs'))
if CONFIG_FILE == None:
    utils.e('----------------------------------------')
    utils.e(' CONFIG_FILE was not set!!!')
    utils.e('----------------------------------------')
else:
    fp = os.path.join(CONFIG_FOLDER, CONFIG_FILE + '.yml')
    utils.hl(f'Load config file: {fp}')
    config = utils.loadYaml(fp)


DATA_FOLDER=os.path.join(os.getcwd(), 'data')
if not os.path.exists(DATA_FOLDER):
    print('ERROR: Data Folder not found: ', DATA_FOLDER)

def getVersionName():
    return config['version_name']

def getVersionCode():
    return config['version_code']

def getBuildDate():
    return config['build_date']

def getBuildNumber():
    return config['build_number']

def showBigModelOnConsole():
    return config['debug']['logging']['console']['print_big_model']

def getServiceConfig(serviceID):
    return config['service_configuration'][serviceID]