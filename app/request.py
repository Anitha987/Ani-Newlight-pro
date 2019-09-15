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
  def get_source(id):
    get_source_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_source_details_url) as url:
        source_details_data = url.read()
        source_details_response = json.loads(_details_data)

        source_object = None
        if source_details_response:
            id = source_details_response.get('id')
            title = source_details_response.get('original_title')
            overview = source_details_response.get('overview')
            poster = source_details_response.get('poster_path')
            vote_average = source_details_response.get('vote_average')
            vote_count = source_details_response.get('vote_count')
            source_object = Source(id,title,overview,poster,vote_average,vote_count)

    return source_object  


