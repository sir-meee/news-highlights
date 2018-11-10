from app import app
import urllib.request,json
from .models import topnews

Topnews = topnews.Topnews
 
 # Getting api key
api_key = app.config['NEWS_API_KEY']

 # Getting top news base url
base_url = app.config["TOPNEWS_API_BASE_URL"] 