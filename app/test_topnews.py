import unittest
from models import topnews
Topnews = topnews.Topnews 
class TopnewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Topnews class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_topnews = Topnews('Google News','Justin','NY times under fire','Pretty good','https://image.tmdb.org/t/p/w500/khsjha27hbs','www.foxnews.com')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_topnews,Topnews))
if __name__ == '__main__':
    unittest.main()