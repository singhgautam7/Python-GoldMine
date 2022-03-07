import json

from googleapiclient import discovery, errors
from oauth2client.client import GoogleCredentials

import config

credentials = GoogleCredentials.get_application_default()
service = discovery.build('iam', 'v1', credentials=credentials)
parent = f'projects/{config.PROJECT_ID}' if config.flag_is_a_project else f'organizations/{config.ORG_ID}'


class HelperGCloud:
    """
    Helper class which will interact with gcloud.
    Doc: https://cloud.google.com/iam/docs/reference/rest/v1/projects.roles
    The role object is of form
    {
        'description': '',
        'etag': '',
        'includedPermissions': [],
        'name': 'projects/<project-name>/roles/<role-name>',
        'stage': 'GA',
        'title': ''
    }
    """

    @staticmethod
    def get_roles_list():
        """
        Returns: List of custom roles
        """
        # Parent will be an organization if the id exists else project
        request = service.projects().roles().list(parent=parent)

        # Initializing roles list with empty list
        roles_list = []

        # Run the loop to collect all custom roles list
        while True:
            response = request.execute()
            roles_list.append(response.get('roles', []))

            # Get next roles list
            request = service.projects().roles().list_next(previous_request=request, previous_response=response)

            # If no more roles left to find, then break
            if request is None:
                return roles_list

    @staticmethod
    def get_role_info():
        """
        Returns: Dictionary of roles details
        """
        try:
            request = service.projects().roles().get(name=config.absolute_role_name)
            response = request.execute()
            return response
        except errors.HttpError:
            return {}

    @staticmethod
    def create_role():
        """
        Create a role
        Returns: Dictionary of roles details
        """
        role_request_body = {
            'roleId': config.ROLE_ID,
            'role': {
                'title': config.ROLE_TITLE,
                'description': config.ROLE_DESCRIPTION,
                'includedPermissions': config.ROLE_PERMISSIONS,
                'etag': '',
                'stage': 'GA',
            }
        }

        request = service.projects().roles().create(parent=parent, body=role_request_body)
        response = request.execute()

        return response

    @staticmethod
    def update_role():
        """
        Update a role
        Returns: Dictionary of roles details
        """
        role_body = {
            'title': config.ROLE_TITLE,
            'description': config.ROLE_DESCRIPTION,
            'includedPermissions': config.ROLE_PERMISSIONS,
            'etag': '',
            'stage': 'GA',
        }

        request = service.projects().roles().patch(name=config.absolute_role_name, body=role_body)
        response = request.execute()

        return response


if __name__ == '__main__':

    print("Please wait. Getting Role Info")

    # Get the role info
    init_role_info = HelperGCloud.get_role_info()

    # If the role info is empty, then create a role
    if not bool(init_role_info):
        print(f'\nNo role found with ID {config.ROLE_ID}.\nCREATING ROLE')
        role_info = HelperGCloud.create_role()

    # Else, update the role
    else:
        print(f'\nRole found with ID {config.ROLE_ID}.\nUPDATING ROLE')
        role_info = HelperGCloud.update_role()

    print(f'\n\nThe {"NEW" if not bool(init_role_info) else "UPDATED"} role is - ')
    print(json.dumps(role_info, indent=4))
