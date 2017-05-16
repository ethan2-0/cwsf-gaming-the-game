from selenium import webdriver
import time
words = []
with open("words.txt", "r") as f:
    words = [x.replace("\n", "") for x in f.readlines()]
driver = webdriver.Chrome(executable_path="C:/Users/advai/Downloads/chromedriver_win32/chromedriver.exe")
website = "https://eventmobi.com/cwsf-espc/game/209225/challenges"
driver.get(website)
time.sleep(30)
ebox = driver.find_element_by_css_selector(".gamify-form input[type=text]")
submit = driver.find_element_by_name("submit")
##ebox.click()

i = 3044
while True:
    for j in range(0, 100):
        ebox.send_keys(words[i] + str(j))
        submit.click()
        time.sleep(0.15)
    i += 1

