import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


class ChromeDriverManager:
    def install(self):
        pass


s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
main_url = "https://github.com/RodxGutierrez17"
driver.get(main_url)
res = driver.find_elements(By.CLASS_NAME, "repo")
flink = []
link = []

def loop(next_page):
    global a
    driver.get(next_page)
    res = driver.find_elements(By.CLASS_NAME, "js-navigation-open")
    time.sleep(3)

    for a in res:
        pass
        print(a.text)










for i in res:
    link.append(i.text)



for u in link:
    next_page = f"{main_url}/{u}"
    flink.append(next_page)
    print(flink)
    loop(next_page)



driver.quit()


















