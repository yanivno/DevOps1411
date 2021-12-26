from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import threading
import time

chrome_driver_path = "/Users/ynorman/Dropbox (Personal)/DevOps Experts/selenium/chromedriver"
firefox_driver_path = "/Users/ynorman/Dropbox (Personal)/DevOps Experts/selenium/geckodriver"
edge_driver_path = "/Users/ynorman/Dropbox (Personal)/DevOps Experts/selenium/msedgedriver"

# Q1
def do_chrome(website):
    chrome_drv = webdriver.Chrome(executable_path=chrome_driver_path)
    chrome_drv.get(website)
    print("completed loading chrome")
    chrome_drv.close()
    return chrome_drv


# Q1 + Q2
def do_firefox(website):
    firefox_drv = webdriver.Firefox(executable_path=firefox_driver_path)
    firefox_drv.get(website)
    print("completed loading firefox")
    # Q2
    ynet_title_before_refresh = firefox_drv.title
    print(f"website title before refresh={ynet_title_before_refresh}")
    firefox_drv.refresh()
    ynet_title_after_refresh = firefox_drv.title
    print(f"website title after refresh={ynet_title_after_refresh}")
    assert(ynet_title_before_refresh == ynet_title_after_refresh)
    # END Q2
    firefox_drv.close()
    return firefox_drv


t_chrome = threading.Thread(target=do_chrome, args=("https://www.walla.co.il",))
t_ff = threading.Thread(target=do_firefox, args=("https://www.ynet.co.il",))

t_chrome.start()
t_ff.start()


# Q3
# Locatores - ID, XPath are same path no matter which browser - it is depended on page structure.

# chrome_drv = webdriver.Chrome(executable_path=chrome_driver_path)

# Q4

chrome_drv = webdriver.Chrome(executable_path=chrome_driver_path)
chrome_drv.get("https://translate.google.com")
full_xpath="/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea"
source_textarea = chrome_drv.find_element(by=By.XPATH, value=full_xpath)
source_textarea.clear()
source_textarea.send_keys("קצת עברית")
chrome_drv.close()


# Q5
chrome_drv = webdriver.Chrome(executable_path=chrome_driver_path)
chrome_drv.get("https://youtube.com")

chrome_drv.find_element(by=By.XPATH, value='//input[@id="search"]').send_keys("hurt johnny cash")
chrome_drv.implicitly_wait(5) # button may have not load up
chrome_drv.find_element(by=By.XPATH, value='//button[@id="search-icon-legacy"]').click()
time.sleep(20)
chrome_drv.close()

#Q6

chrome_drv = webdriver.Chrome(executable_path=chrome_driver_path)
chrome_drv.get("https://translate.google.com")
full_xpath="/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea"
source_textarea = chrome_drv.find_element(by=By.XPATH, value=full_xpath)
source_textarea.clear()
source_textarea.send_keys("קצת עברית")
time.sleep(10)
source_textarea = chrome_drv.find_element(by=By.CLASS_NAME, value='er8xn')
source_textarea.clear()
source_textarea.send_keys("קצת עברית 2")
time.sleep(10)
source_textarea = chrome_drv.find_element(by=By.TAG_NAME, value='TEXTAREA')
source_textarea.clear()
source_textarea.send_keys("קצת עברית 3")
time.sleep(10)
chrome_drv.close()


#Q7
chrome_drv = webdriver.Chrome(executable_path=chrome_driver_path)
chrome_drv.get("https://www.facebook.com/")
chrome_drv.find_element(by=By.ID, value='email').send_keys("some_email@gmail.com");
chrome_drv.find_element(by=By.ID, value='pass').send_keys("some_P@ssw0rd");
chrome_drv.find_element(by=By.NAME, value='login').click()
chrome_drv.close()


#Q8

def print_cookies(cookies_list):
    print(f"number of elements={len(cookies_list)}")
    for cookie in cookies_list:
        print(f"cookie for {cookie.get('domain')}={cookie.get('name')}")


chrome_drv = webdriver.Chrome(executable_path=chrome_driver_path)
chrome_drv.get("https://www.facebook.com/")
print("before deleting all cookies")
print_cookies(chrome_drv.get_cookies())
chrome_drv.delete_all_cookies()
print("after deleting all coockies")
print_cookies(chrome_drv.get_cookies())
chrome_drv.close()

# Q9
chrome_drv = webdriver.Chrome(executable_path=chrome_driver_path)
chrome_drv.get("https://github.com/")
search = chrome_drv.find_element(by=By.CSS_SELECTOR, value='.js-site-search-form').\
    find_element(by=By.XPATH,value='//input')
search.send_keys("selenium")
search.send_keys(Keys.ENTER)
chrome_drv.close()


# Q10
# source https://chromium.googlesource.com/chromium/src/+/refs/heads/main/chrome/common/chrome_switches.cc#212
options = webdriver.ChromeOptions()
options.add_argument("disable-extensions")
chrome_drv_no_extensions = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

# safe mode disables the addons
ff_options = webdriver.FirefoxOptions()
ff_options.add_argument("--safe-mode")
firefox_drv = webdriver.Firefox(executable_path=firefox_driver_path, options=ff_options)

# no internet explorer - mac :/ edge (same as Chrome since based on Chromium project)
edge_options = webdriver.EdgeOptions()
edge_options.add_argument("disable-extensions")
edge_drv = webdriver.Edge(executable_path=edge_driver_path,options=edge_options)
