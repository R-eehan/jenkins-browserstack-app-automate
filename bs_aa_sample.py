from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os

userName = os.getenv("BROWSERSTACK_USERNAME")
accessKey = os.getenv("BROWSERSTACK_ACCESS_KEY")

desired_caps = {
    "device": "Samsung Galaxy S8 Plus",
    "app": os.getenv("BROWSERSTACK_APP_ID"),
    "name": "Jenkins 1",
    "build": os.getenv("BROWSERSTACK_BUILD_NAME"),
    "browserstack.debug": True
}

driver = webdriver.Remote("https://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub", desired_caps)

search_element = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Search Wikipedia"))
)
search_element.click()

search_input = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ID, "org.wikipedia.alpha:id/search_src_text"))
)
search_input.send_keys("BrowserStack")
time.sleep(5)

search_results = driver.find_elements_by_class_name("android.widget.TextView")
assert(len(search_results) > 0)

driver.quit()
