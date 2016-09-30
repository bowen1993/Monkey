from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.PhantomJS()
driver.get('http://www.python.org')
driver.get_screenshot_as_file('1.png')
ele = driver.find_element_by_css_selector("input#id-search-field.search-field.placeholder")
ele.send_keys('pycon')
driver.get_screenshot_as_file('2.png')
ele = driver.find_element_by_css_selector("button#submit")
ele.click()
driver.get_screenshot_as_file('3.png')
ele = driver.find_element_by_xpath("/html/body/div/div[3]/div/section/h2")
assert 'Search' in ele.text
driver.get_screenshot_as_file('4.png')
driver.close()