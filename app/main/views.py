from flask import render_template,request,redirect,url_for      
from app import app
from .request import get_source,get_article,search_article
from app import views
from app import error
# Views
@app.route('/')
def index():  

    '''
    View root page function that returns the index page and its data
    '''
    anitha_source=get_source()
    title = 'You are most  welcome to the best News Highlight'
    
    search_article = request.args.get('article_query')

    if search_article:
        return redirect(url_for('search',article_name=search_article))
    else:
        return render_template('index.html',title=title,sources=anitha_source)
@app.route('/source/<int:source_id>')
def source(source_id):

    '''
    View source page function that returns the source details page and its data
    '''
    return render_template('source.html',id = source_id)    
@app.route('/article/<int:id>')
def article(id):

    '''
    View article page function that returns the article details page and its data
    '''
    article = get_article(id)
    title = f'{article.title}'
    reviews = Review.get_reviews(article.id)
    return render_template('article.html',title = title,article = article,reviews = reviews) 
@app.route('/search/<article_name>')
def search(article_name):
    '''
    View function to display the search results
    '''
    article_name_list = article_name.split(" ")
    article_name_format = "+".join(article_name_list)
    searched_article = search_article(article_name_format)
    title = f'search results for {article_name}'
    return render_template('search.html',articles = searched_articles)       