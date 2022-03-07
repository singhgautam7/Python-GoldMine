"""
A file to import all the variables from env file.
Keys required in .env files are
"""
import json
import os
from os.path import join, dirname
from dotenv import load_dotenv

# Initializing dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Get variables from env
PROJECT_ID = os.getenv('PROJECT_ID') or ''
ORG_ID = os.getenv('ORG_ID') or ''
ROLE_ID = os.getenv('ROLE_ID').split('/')[-1]
ROLE_TITLE = os.getenv('ROLE_TITLE')
ROLE_DESCRIPTION = os.getenv('ROLE_DESCRIPTION')
ROLE_PERMISSIONS = json.loads(os.getenv('ROLE_PERMISSIONS'))

# Calculated variables
flag_is_a_project = ORG_ID == ''
absolute_role_name = f'projects/{PROJECT_ID}/roles/{ROLE_ID}' if flag_is_a_project \
    else f'organizations/{ORG_ID}/roles/{ROLE_ID}'
