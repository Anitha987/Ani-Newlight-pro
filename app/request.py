from app import app    
import urllib.request,json
from .models import source

Source = source.Source
# Getting api key
api_key = app.config['SOURCE_API_KEY']

# Getting the source base url
base_url = app.config["SOURCE_API_BASE_URL"]
def get_source(category):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['results']:
            source_results_list = get_source_response['results']
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
      if poster:
        source_object=Source(id,name,description,url,category,language,country)
        source_results.append(source_object)
    return source_results  
  def get_article(id):
    get_article_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_article_details_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(_details_data)

        article_object = None
        if article_details_response:
            id = article_details_response.get('id')
            title = article_details_response.get('original_title')
            overview = article_details_response.get('overview')
            poster = article_details_response.get('poster_path')
            vote_average = article_details_response.get('vote_average')
            vote_count = article_details_response.get('vote_count')
            article_object = Article(id,title,overview,poster,vote_average,vote_count)

    return article_object 
def search_article(article_name):
    # search_article_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,article_name)
    with urllib.request.urlopen(search_article_url) as url:
        search_article_data = url.read()
        search_article_response = json.loads(search_article_data)

        search_article_results = None

        if search_article_response['results']:
            search_article_list = search_article_response['results']
            search_article_results = process_results(search_article_list)


    return search_article_results    



