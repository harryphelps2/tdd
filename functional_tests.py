from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Lou needs a to do app to go with her new job. She goes to check out
        # its homepage
        self.browser.get('http://localhost:8000')

        # She sees to do lists in the title
        assert 'To-Do' in self.browser.title

        # She is invited to add a to do right away
        self.fail('Finish the test!')

        # She types 'buy peacock feathers' in the text box

        # When she hits enter is adds the to do item to the todo list

        # She adds another to do item

        # The page updates again and shows both items 

        # She wonders whether the site will remember her list and
        # sees it has generated a unique url for her

        # She visits the url and sees the todo items are still there.

if __name__ == '__main__':
    unittest.main(warnings='ignore')

