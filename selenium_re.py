from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

RE_URL = "https://voting.re-fd.de/voting/mein-versorger-mein-verein-2018/ein-sporthausanbau-fuer-den-fsv-thalau/support/"
email_adresse = "jonas-licht@gmx.de"

browser = webdriver.Firefox()
browser.fullscreen_window()
browser.get(RE_URL)

print(browser.current_window_handle.title())

email_input = browser.find_element_by_name("email")

#browser.execute_script("arguments[0].scrollIntoView();", email_input)

#actions = ActionChains(browser)
#actions.move_to_element(email_input).perform()


email_input.click().send_keys("jonas-licht@gmx.de")

form = browser.find_element_by_class_name("api-form")
form.submit()

