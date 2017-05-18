from selenium import webdriver
import time
words = []
with open("words2.txt", "r") as f:
    words = [x.replace("\n", "") for x in f.readlines()]
driver = webdriver.Chrome(executable_path="C:/Users/advai/Downloads/chromedriver_win32/chromedriver.exe")
website = "https://eventmobi.com/cwsf-espc/game/209225/challenges"
driver.get(website)
time.sleep(30)
ebox = driver.find_element_by_css_selector(".gamify-form input[type=text]")
submit = driver.find_element_by_name("submit")
##ebox.click()

i = 1
while True:
    ebox.send_keys(words[i])
    submit.click()
    time.sleep(0.15)
    i += 4

