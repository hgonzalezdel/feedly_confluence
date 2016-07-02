import json
import requests
import base64
import getpass
import config

#Add your confluence rest ednpoint
confluence_endpoint = config.confluence_endpoint

def get_auth_b64():
    username = config.confluence_user
    password = getpass.getpass('Confluence password: ')
    usrPass = username+":"+password
    b64Val = base64.b64encode(usrPass)
    return b64Val

def create_page(title, content,space):
    headers = {'content-type': 'application/json',
        'Authorization':  "Basic " + get_auth_b64()
    }
    quest_url = confluence_endpoint + "content"
    params = dict(
        type="page",
        title=title,
        space=dict(
            key=space
        ),
        body = dict(
            storage=dict(
                value=content,
                representation="storage"
            )
        )
    )
    res = requests.post(url=quest_url, data=json.dumps(params), headers=headers)
    return res

def update_page(page_id, content):
    headers = {'content-type': 'application/json',
        'Authorization':  "Basic " + get_auth_b64()
    }
    quest_url = confluence_endpoint + "content"
    params = dict(
        id=page_id,
        body = dict(
            storage=dict(
                value=content
            )
        )
    )
    res = requests.post(url=quest_url, data=json.dumps(params), headers=headers)
    return res