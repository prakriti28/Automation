from selenium import webdriver
import time
# import getpass
path=r"C:\Users\Prakriti\Downloads\chromedriver_win32\chromedriver.exe"
browser=webdriver.Chrome(path)
str=input()
browser.get('http://www.google.com')
searchBox=browser.find_element_by_name('q')
searchBox.send_keys(str)
time.sleep(3)
searchButton=browser.find_element_by_name('btnK')
searchButton.click()
time.sleep(5)
wiki=browser.find_elements_by_partial_link_text('Wikipedia')

wiki[0].click()
# getpass.getpass()