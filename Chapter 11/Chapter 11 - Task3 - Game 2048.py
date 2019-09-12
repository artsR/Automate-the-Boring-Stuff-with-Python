#! python3
#

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
time.sleep(5)
game_elem = browser.find_element_by_tag_name('html')

while True:
    game_elem.send_keys(Keys.UP)
    game_elem.send_keys(Keys.RIGHT)
    game_elem.send_keys(Keys.DOWN)
    game_elem.send_keys(Keys.LEFT)
    try:
        browser.find_element_by_css_selector("div.game-message.game-over p")
        break
    except:
        pass
time.sleep(10)
browser.close()
