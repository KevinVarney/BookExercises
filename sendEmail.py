#! python3
# sendEmail.py
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Firefox()
browser.get('https://www.googlemail.com')
emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys('kevin.e.varney@googlemail.com')
nextElem = browser.find_element_by_id('identifierNext')
nextElem.send_keys(Keys.ENTER)
#browser.switch_to().frame(browser.findElement(By.xpath("//iframe[@name='a1']")))
#browser.switch_to().frame("f1");
#browser.switch_to_active_element()
#passwordElem = browser.find_element_by_id('password')
browser.implicitly_wait(5)
passwordElem = browser.find_element_by_css_selector('#password > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
passwordElem.send_keys(sys.argv[1])
passwordNextElem = browser.find_element_by_id('passwordNext')
passwordNextElem.send_keys(Keys.ENTER)
composeElem = browser.find_element_by_id(':io')
composeElem.send_keys(Keys.ENTER)
#message = sys.argv[1]
