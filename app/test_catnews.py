import unittest
from models import catnews
Catnews = catnews.Catnews
 
class CatnewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Topnews class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_catnews = Catnews('engadget','Engadget','NY times under fire','www.foxnews.com')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_catnews,Catnews))
        if __name__ == '__main__':
           unittest.main() 