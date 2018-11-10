from app import app
import urllib.request,json
from .models import topnews

Topnews = topnews.Topnews
 
 # Getting api key
api_key = app.config['NEWS_API_KEY']

 # Getting top news base url
base_url = app.config["TOPNEWS_API_BASE_URL"] 
def get_topnews(source):
    """
    Function that gets the json response to our url request
    """
    get_topnews_url = base_url.format(source,api_key)
    with urllib.request.urlopen(get_topnews_url) as url:
        get_topnews_data = url.read()
        get_topnews_response = json.loads(get_topnews_data)
        topnews_results = None
        if get_topnews_response['results']:
            topnews_results_list = get_topnews_response['results']
            topnews_results = process_results(topnews_results_list)
    return topnews_results