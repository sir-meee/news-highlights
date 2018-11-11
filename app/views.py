from flask import render_template
from app import app
from .request import get_topnews
 #Views
@app.route('/') 
def index():
     '''
    View root page function that returns the index page and its data
    '''
     #Getting top news from cnn
     top_articles = get_topnews('google-news')
     print(top_articles)
     title = 'Home -Get breaking news headlines, and search for articles from over 30,000 news sources and blogs'
     return render_template('index.html', title = title, google_news = top_articles)