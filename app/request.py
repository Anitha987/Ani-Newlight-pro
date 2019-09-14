from app import app
import urllib.request,json
from .models import news

News = news.News
# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]
def get_newss(category):
    '''
    Function that gets the json response to our url request
    '''
    get_newss_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_newss_url) as url:
        get_newss_data = url.read()
        get_newss_response = json.loads(get_newss_data)

        news_results = None

        if get_newss_response['results']:
            news_results_list = get_newss_response['results']
            news_results = process_results(news_results_list)


    return news_results
def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
      id = source_item.get('id')
      name = source_item.get('name')
      description = source_item.get('description')
      url = source_item.get('url')
      category = source_item.get('category')
      language = source_item.get('language')
      country = source_item.get('country')
      if poster:
        news_object=News(id,name,description,url,category,language,country)
        news_results.append(news_object)
    return news_results  


