# GCloud IAM custom roles management
This will help you to manage the custom roles in your project/organization.
Here is the [link](https://cloud.google.com/iam/docs/reference/rest/v1/projects.roles) to the doc.

## Steps
- Enable IAM api and check quota for your project [here](https://console.developers.google.com/apis/api/iam)
- Install the gcloud CLI from this [link](https://cloud.google.com/sdk/docs/install)
- After above step is completed, run the command `gcloud beta auth application-default login`
  - Make sure the account you log in with has the following permissions:
    - iam.roles.get, iam.roles.create, iam.roles.update
- Make sure **python** is installed in your system/environment.
- Install other requirements using this command: 
  - For python 2 `pip install -r requirements.txt` 
  - For python 3 `pip3 install -r requirements.txt`
- Create a `.env` file in the current working directory, and add all the required variables (Example can be found below).
  - **Note:** You can ask the admin or your manager to give you the already existing `.env` file over a secure mode of transfer, for you to directly use it.
  - Don't worry about downloading the packages as it has been taken care of in the above step.
  - You can learn more about creating .env file from this [link](https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1).
- **Run** the `main.py` file using the command:
  - For python 2 `python .\main.py`
  - For python 3 `python3 .\main.py`

## Example .env file format
```
PROJECT_ID=""
ORG_ID=""
ROLE_ID=""
ROLE_TITLE=""
ROLE_DESCRIPTION=""
ROLE_PERMISSIONS='["my.role.1", "my.role.2", "my.role.3"]'
```

### Description of each variable
- **PROJECT_ID** - <type: _str_>
- **ORG_ID** - <type: _str_>
- **ROLE_ID** - <type: _str_>
- **ROLE_TITLE** - <type: _str_>
- **ROLE_DESCRIPTION** - <type: _str_>
- **ROLE_PERMISSIONS** - <type: _list_>
  - _Note_: ROLE_PERMISSIONS should be list enclosed within single inverted commas, with every value enclosed within double
inverted commas. Example: ROLE_PERMISSIONS='["Foo", "bar"]'