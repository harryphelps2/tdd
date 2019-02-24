from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to add a to do right away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types 'buy peacock feathers' in the text box
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter is adds the to do item to the todo list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # She adds another to do item

        self.fail('Finish the test!')
        # The page updates again and shows both items 

        # She wonders whether the site will remember her list and
        # sees it has generated a unique url for her

        # She visits the url and sees the todo items are still there.

if __name__ == '__main__':
    unittest.main(warnings='ignore')

