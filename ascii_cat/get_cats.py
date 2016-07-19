import json
import random
import requests
from StringIO import StringIO
from googleapiclient.discovery import build


def construct_query(opts):
    """
    Construct query with options passed from the command line

    :param list opts: options passed in from the CLI

    :returns: properly formatted query to pass to the Google
    custom search engine
    """
    query_args = ['cats']
    if opts.command == 'cats':
        if opts.breeds:
            for breed in opts.breeds:
                query_args.append(breed)
        if opts.other:
            for arg in opts.other:
                query_args.append(arg)
        if opts.fluffy:
            query_args.append('fluffy')
        if opts.funny:
            query_args.append('funny')
        if opts.kitten:
            query_args.append('kitten')

    if opts.command == 'meme':
        if opts.grumpy:
            query_args.append('gumpy cat')
        if opts.bubs:
            query_args.append('bubs')
        if opts.business_cat:
            query_args.append('business cat')
        if opts.lolcats:
            query_args.append('lolcat')
        if opts.nyan:
            query_args.append('nyan cat')
        if opts.hipster:
            query_args.append('hipster cat')
        if opts.longcat:
            query_args.append('longcat')

    if opts.command == 'random':
        query_args += ['cute', 'kitten', 'kitty']

    joined_args = ' '.join(query_args)

    return joined_args

def get_image_content(image_url):
    print image_url
    img_content = None

    response = requests.get(image_url)
    if response.status_code != 200:
        print('Whoops! Error getting image')
        return
    img_content = StringIO(response.content)

    return img_content


def select_results(query_resp, num_results=1):
    """
    Select the results to return.
    """
    result = []
    N = 0

    for item in query_resp:
        N += 1
        if len(result) < num_results:
            result.append(item)
        else:
            s = int(random.random() * N)
            if s < num_results:
                result[s] = item

    return result


def search(query=None):
    """
    Use Google Custom Search Engine (CSE) to query the web for kitty images.

    The google_search_api_key and google_search_engine are stored in a
    private file located in the ascii_cat directory named .credentials.json

    In order to use this you will need to create your own CSE through Google:
        https://developers.google.com/custom-search/
    """
    if not query:
        return "No search parameters passed in!"

    with open('ascii_cat/.credentials.json') as key_file:
        key = json.load(key_file)
        api_key = key.get("google_search_api_key")
        engine = key.get("google_search_engine")
    service = build('customsearch', 'v1', developerKey=api_key)

    response = service.cse().list(
        q=json.dumps(query),
        cx=engine,
        safe='high',
        searchType='image'
    ).execute()

    if response['searchInformation']['totalResults'] == 0:
        return 'No images found matching your search terms :('

    return response['items']
