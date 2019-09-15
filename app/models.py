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



class Review:

    all_reviews = []

    def __init__(self,movie_id,title,imageurl,review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review


    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)

        return response          