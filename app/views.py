from flask import render_template
from app import app
 #Views
def index():
     '''
    View root page function that returns the index page and its data
    '''
     title = 'Home -Get breaking news headlines, and search for articles from over 30,000 news sources and blogs'
    return render_template('index.html', title = title)