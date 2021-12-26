from selenium import webdriver
my_driver = webdriver.Chrome(executable_path="/Users/ynorman/Dropbox (Personal)/DevOps Experts/HTML/chromedriver")
#ff_drv_options = webdriver.FirefoxOptions()
#ff_drv_options.log.level = "trace"
#firefox_drv = webdriver.Firefox(executable_path=firefox_driver_path, options=ff_drv_options)
f#irefox_drv.get("https://www.ynet.co.il")


# my_driver.get("https://github.com")
path = "file:///Users/ynorman/Dropbox (Personal)/DevOps Experts/HTML/tip_calc/index.html"
my_driver.get(path)
bill = my_driver.find_element_by_id("billamt")
bill.send_keys("100")
my_driver.find_element_by_xpath('//*[@id="serviceQual"]/option[4]').click() #selecting a dropdown element
my_driver.find_element_by_id('peopleamt').send_keys("4")
my_driver.find_element_by_id('calculate').click()

expected = "3.75"
actual = my_driver.find_element_by_id('tip').text
assert(expected == actual)

