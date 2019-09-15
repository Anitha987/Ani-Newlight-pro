import unittest   
from models import source 
SOURCE = source.Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
    '''
    Set up method that will run before every Test
    '''
    # self.source_sources = Source()

    def test_instance(self):
        self.assertTrue(isinstance(self.source_sources,Source))


if __name__ == '__main__':
    unittest.main()