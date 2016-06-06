import json
import requests
from googleapiclient.discovery import build


def get_image_content(image):
    img_content = None

    # use StringIO for python 2
    if sys.version_info[0] == 2:
        from StringIO import StringIO
        img_content = StringIO(response.content)
    # use BytesIO for python 3
    if sys.version_info[0] == 3:
        from io import BytesIO
        img_content = BytesIO(response.content)

    return img_content


def search(query=None):
    if not query:
        return "No search parameters passed in!"

    with open('.credentials.json') as key:
        api_key = key.get("google_search_api_key")
        engine = key.get("google_search_engine")
    service = build('customsearch', 'v1', developerKey=api_key)

    response = service.cse().list(
        q=query,
        cx=engine,
        safe='high',
        searchType='image',
        num=50
    ).execute()
