# from app import app
import urllib.request,json
from .models import Source,Article

# Source = source.Source
# Getting api key
api_key = None

# Getting the source base url
base_url = None
base_article_url = None
def configure_request(app):
    global api_key, base_article_url, base_source_url
    api_key = app.config['NEWS_API_KEY']
    base_source_url = app.config['NEWS_SOURCE_API_BASE_URL']
    base_article_url = app.config['NEWS_ARTICLES_API_BASE_URL']

def get_source():
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_source_url.format(api_key)
    print(api_key) 
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)


    return source_results
def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
      id = source_item.get('id')
      name = source_item.get('name')
      description = source_item.get('description')
      url = source_item.get('url')
      category = source_item.get('category')
      language = source_item.get('language')
      country = source_item.get('country')
      if name:
        source_object=Source(id,name,description,url,category,language,country)
        source_results.append(source_object)
    return source_results  
def get_article(id):
    get_article_details_url = base_article_url.format(id,api_key)

    with urllib.request.urlopen(get_article_details_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)

        articles_results = None
        if article_details_response['articles']:
            source_results_list = article_details_response['articles']
            articles_results = process_article(source_results_list)
            # id = article_details_response.get('id')
            # title = article_details_response.get('original_title')
            # overview = article_details_response.get('overview')
            # poster = article_details_response.get('poster_path')
            # vote_average = article_details_response.get('vote_average')
            # vote_count = article_details_response.get('vote_count')
            # article_result = Article(id,title,overview,vote_average,vote_count)

        return articles_results  
def process_article(article_list):
    '''
    Function  that processes the articles results and transform them to a list of Objects
    Args:
        articles_list: A list of dictionaries that contain articles details
    Returns :
        articles_results: A list of articles objects
    '''
    article_results = []
    for article_item in article_list:
        id = article_item.get('id')
        name = article_item.get('name')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')

        article_results.append(Article(id, name, author, title, description, url, urlToImage, publishedAt))

    return article_results    


