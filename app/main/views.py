from flask import render_template
from app import app
from .request import get_newss
# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    anitha_newss=get_newss()
    title = 'You are most  welcome to the best News Website Online'
    return render_template('index.html',title=title,news=anitha_newss)
@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)    