class Source:
  '''
  Source class to define Source Objects
  '''

  def __init__(self, id, name, description, url, category, language, country):

    self.id = id
    self.name = name
    self.description = description
    self.url = url
    self.category = category
    self.language = language
    self.country = country
class Article:
  '''
  Article class to define Article objects
  '''
  def __init__(self, id, name, author, title, description, url, urlToImage, publishedAt):
      self.id = id
      self.name = name
      self.author = author
      self.title = title
      self.description = description
      self.url = url
      self.urlToImage = urlToImage
      self.publishedAt = publishedAt
    # def save_review(self):
    #     Review.all_reviews.append(self)


    # @classmethod
    # def clear_reviews(cls):
    #     Review.all_reviews.clear()

    # @classmethod
    # def get_reviews(cls,id):

    #     response = []

    #     for review in cls.all_reviews:
    #         if review.article_id == id:
    #             response.append(review)

    #     return response          