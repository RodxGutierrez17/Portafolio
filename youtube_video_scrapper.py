from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class ChromeDriverManager:
    def install(self):
        pass

# Crea el servicio y el controlador de Chrome
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

main_url = "https://www.youtube.com/@RodrigoGutierrez1/videos"
driver.get(main_url)
url2 = "https://youtu.be/VLyB60kNdek?si=3jTz1i0mj3YoYTvp"
last = "watch?v=e0Bot2WxwBM&t=3s"
cls = driver.find_elements(By.CLASS_NAME, "style-scope ytd-rich-grid-row")
def going_for_video(click_video):
    driver.get(url2)
    click = driver.find_elements(By.CLASS_NAME, "style-scope ytd-app")
    pagina = driver.page_source
    pagina = f"{pagina}"
    print(pagina)
    time.sleep(3)
    if "Mi Sistema de Aprendizaje: Cómo Dominar Cualquier Habilidad" in pagina:
        print("funciona")
    else:
        pass







for a in cls:
    print(a.text)
    time.sleep(3)
    if "6" in a.text:
        clik_video =f"{url2}"
        going_for_video(clik_video)
    else:
        pass



# https://www.youtube.com/watch?v=e0Bot2WxwBM&t=3s
