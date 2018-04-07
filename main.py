from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC

RE_URL = "https://voting.re-fd.de/voting/mein-versorger-mein-verein-2018/ein-sporthausanbau-fuer-den-fsv-thalau/support/"
#email_adresse = "jonas-licht@gmx.de"
email_adresse = "wuuzzaa.jl@gmail.com"

browser = webdriver.Firefox()
#browser = webdriver.Edge(executable_path='MicrosoftWebDriver.exe')
browser.fullscreen_window()
#print(browser.context)


#browser.implicitly_wait(10) # seconds
browser.get(RE_URL)

try:
    # E-Mail eintragen
    email_input = WebDriverWait(browser, 11).until(EC.element_to_be_clickable((By.NAME, "email")))  # Wartet 11 Sekunden
    browser.execute_script("arguments[0].click();", email_input)
    email_input.send_keys(email_adresse)

    # Submit Button drücken
    submit_button = WebDriverWait(browser, 11).until(EC.element_to_be_clickable((By.ID, "vote-btn-ein-sporthausanbau-fuer-den-fsv-thalau")))  # Wartet 11 Sekunden
    browser.execute_script("arguments[0].click();", submit_button)


except:
    browser.save_screenshot('screenie.png')
    raise





"""
from robobrowser import RoboBrowser

RE_URL = "https://voting.re-fd.de/voting/mein-versorger-mein-verein-2018/ein-sporthausanbau-fuer-den-fsv-thalau/support/"
email_adresse = "jonas-licht@gmx.de"

browser = RoboBrowser(history=True)
browser.open(RE_URL)

form = browser.get_form(action="#")

#form["id_email"].text = email_adresse
form["email"].value = email_adresse
form["fp_id"].value = "95eeaf90baeed6eedbe2d0e0e8b9a7a2aca1999de7eee4eeaec7cceed6eeded0dfd8d0dddedddfdbdcd7dbdeeee4eea19dad909beed6eeb9a7a2aca1999de0c2bce0dfd0e2d0d5e0b9a7a2dadcd5e098dadceee4eea398bc90eed6d0e4ee9bafeed6eec3a196a7a4a4afe1dbe2d0e0e8b9a7a2aca1999de0c2bce0dfd0e2d0d5e0b9a7a2dadcd5e098dadcd5e09e9ad6dbd7e2d0e7e0c9abada5a1e1ded0dfd0d0dfd0dfe0caa79eabaaa198e1dbd7e2d0eee4eea8ad9eeed6dce4ee99ac9ceed6dfd7ded0e4eea8a99ceed6dfd0d8d0e4eeafad9ca79aab98eed6aaafa49dabe4ee9da49ba9eed6eeaba7a2e39d90a19e9ca8af9b9dafa2aeaf9be3aa9bab9ee3acaba2e3aa9d9ae39ca8afa4af9beee4ee90989eeed6dfe4ee9b9dab9eb1afa9aba29ceed6eec3a196a7a4a4afe1dbe2d0e0e8b9a7a2aca1999de0c2bce0dfd0e2d0d5e0b9a7a2dadcd5e098dadcd5e09e9ad6dbd7e2d0e7e0c9abada5a1e1ded0dfd0d0dfd0dfe0caa79eabaaa198e1dbd7e2d0eee4eeae9eb1a4a7abaceed6aaafa49dabe4eea19db1a4a7abaceed6aaafa49dabe4ee9aaba2aca19eeed6eeeee4ee90a4af9caaa19ea3eed6eeb9a7a2dadceee4eea9b19eaba2acab9eab9eeed6eeb9abaec9c4e0c9c4bdc4e0cbbde0dfe2d0eee4eea9b19aaba2aca19eeed6eeb9abaec9c4e0dfe2d0eee4eea9b19ba2a3b19aaba2aca19eeed6eec9a1a1a9a4abe0c7a2ade2eee4eea9b19ba2a3b19eaba2acab9eab9eeed6eecfc2c9c4cbe0e8beafacaba1a2e0e8bcc3e7e0beb8e0dcd8d0e0c99eaf90a8a7ad9de0cca79eabad9cddccdfdfe09a9db1dbb1d0e0909db1dbb1d0e7eee4ee9db19d9ca19eafa9abeed69c9e9babe4eea4b19d9ca19eafa9abeed69c9e9babe4eea7b1acaeeed69c9e9babe4ee9dad9eb1ada49eb1acab909ca8eed6dedce4eea4afa2a99bafa9ab9deed6eeb595b4eea4afa2a9b4eed6b4eeacabb4ee93e495b4eea4afa2a9b4eed6b4eeaba2e3bbbdb4ee93e495b4eea4afa2a9b4eed6b4eeaba2b4ee93b3eee4eeaca29ceed6eedfeee4eeaea4a1ada5eed6aaafa49dabe4ee90a49ba9a7a29deed6eeb5b3eee4eeada1a1a5a7abeed69c9e9babe4eea3a7a3abb19c9790ab9deed6eeb5b3eee4eeafad9cbacceed69c9e9babe4ee909ece9eeed69c9e9bab93"
form["direct_action"].value = ""
#form["g-recaptcha-response"].value = ""

print(form)
browser.submit_form(form)

print(browser.response)
#print(browser.state)
#print(browser.parsed)

"""




