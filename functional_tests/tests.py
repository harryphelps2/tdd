from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
    
    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Lou needs a to do app to go with her new job. She goes to check out
        # its homepage
        self.browser.get(self.live_server_url)

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

        # She adds another to do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make fly')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again and shows both items 
        self.wait_for_row_in_list_table('2: Use peacock feathers to make fly')
        self.wait_for_row_in_list_table('1: Buy peacock feathers')


        # She wonders whether the site will remember her list and
        # sees it has generated a unique url for her

        # She visits the url and sees the todo items are still there.
        self.fail('Finish the test!')
