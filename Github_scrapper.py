import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class ChromeDriverManager:
    def install(self):
        pass

# Crea el servicio y el controlador de Chrome
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

# URL de la página principal de GitHub
main_url = "https://github.com/RodxGutierrez17"
driver.get(main_url)

# Encuentra los elementos con la clase "repo"
res = driver.find_elements(By.CLASS_NAME, "repo")


# Listas para almacenar los enlaces
link = []
flink = []

# Función para realizar acciones en cada página
def loop(next_page):
    driver.get(next_page)
    # Encuentra los elementos con la clase "js-navigation-open"
    res2 = driver.find_elements(By.CLASS_NAME, "js-navigation-open")
    time.sleep(2)
    # for a in res2:
    #     pass
    #     time.sleep(2)
    #     print(a.text)
    # if "py" in a.text:
    #     print("it is an password in the text")










# Recorre los elementos encontrados y agrega los textos a la lista 'link'
for i in res:
    link.append(i.text)

# Crea enlaces completos y realiza acciones en cada página
for l in link:
    next_page = f"{main_url}/{l}"
    flink.append(next_page)
    # print(flink)
    loop(next_page)

# Cierra el navegador
driver.quit()
s = Service(ChromeDriverManager().install())
driver2 = webdriver.Chrome(service=s)
main_url2 = "https://github.com/RodxGutierrez17/RodxGutierrez17/blob/main/main.py"
driver2.get(main_url2)

# Encuentra los elementos con la clase "repo"
res3 = driver2.find_elements(By.CLASS_NAME, "repo")

def loop2(next_page2):
    driver.get(next_page2)
    # Encuentra los elementos con la clase "js-navigation-open"
    res3 = driver.find_elements(By.CLASS_NAME, "js-navigation-open")
    time.sleep(2)
    for u in res3:
        if "password" in u.text:
            print("you got it!")
        # time.sleep(2)
        # print(u.text)






link2 = []
flink2 = []

for u in res:
    link.append(u.text)

# Crea enlaces completos y realiza acciones en cada página
for w in link2:
    next_page2 = f"{main_url2}/{w}"
    flink2.append(next_page2)
    loop2(next_page2)
    print(flink)

