from google.cloud import storage
from google.auth.exceptions import *

from custom_package.version_info_factory import *


def check_version_list(request):
    """
    Lists all the blobs in the bucket with generation.
    1. https://cloud.google.com/storage/docs/using-versioned-objects?hl=ko#storage-list-object-versions-python
    2. https://cloud.google.com/storage/docs/metadata?hl=ko#generation-number
    3. https://docs.kakaoi.ai/kakao_work/webapireference/commonguide/
    """

    bucket_name = "fourmis_test"
    prefix = "test.json"
    content = list()
    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name, prefix=prefix, versions=True)
    
    try:
        storage_client = storage.Client()
        blobs = storage_client.list_blobs(bucket_name, prefix=prefix, versions=True)

        
        for blob in blobs:
            content.append(VersionInfoFactory.createVersion(blob.md5_hash, blob.size))
            print(f"{blob.name}, {blob.generation}, {blob.updated}")
            
        response = {
            "code"      : 200,
            "content"   : content
        }
    except GoogleAuthError as e:
        response = {
            "code"      : 403,
            "content"   : {
                "message"       : "Error in google.auth",
                "description"   : "Check authentication settings in Google Cloud Flatfom"
            }
        }
    except:
        response = {
            "code"      : 400,
            "content"   : {
                "message"       : "message is message",
                "description"   : "description is description"
            }
        }
        
    return response
    


def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return f'Hello World!'
