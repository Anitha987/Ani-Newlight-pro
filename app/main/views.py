from flask import render_template
from app import app
from .request import get_source
# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    anitha_source=get_source()
    title = 'You are most  welcome to the best News Highlight'
    return render_template('index.html',title=title,sources=anitha_source)
@app.route('/source/<int:source_id>')
def source(source_id):

    '''
    View source page function that returns the source details page and its data
    '''
    return render_template('source.html',id = source_id)    