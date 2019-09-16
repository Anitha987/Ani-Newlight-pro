import unittest
from app.models import News

class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_News = News()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_News,News))