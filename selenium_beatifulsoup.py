import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = input("Enter the URL you want to scrape: ")
keyword = input("Enter the keyword of the URL: ")
enlaces = int(input("Cuantos enlaces quieres acceder: "))

# Step 1: Obtener enlaces con BeautifulSoup
try:
    response = requests.get(url)
    response.raise_for_status()  # Esto lanzará una excepción si el status no es 200
except requests.RequestException as e:
    print(f"Failed to retrieve {url}: {e}")
    exit()

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    a_tag = soup.find_all('a')
    url_list = [urljoin(url, tag.get('href')) for tag in a_tag if tag.get('href')]

print(f"fEnlaces obtenidos: {url_list}")


# Step 2: Inicializar Selenium
class ChromeDriverManager:
    def install(self):
        pass


s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)


# Step 3: Función para procesar el contenido de cada página
def process_page(page_url):
    driver.get(page_url)
    time.sleep(3)  # Esperar a que cargue el contenido dinámico

    paragraphs = driver.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)


# Step 4: Recorrer y procesar cada enlace

for link in url_list:
    try:
        print(f"Accediendo a {link}")
        process_page(link)
    except Exception as e:
        print(f"Error al acceder a {link}: {e}")

driver.quit()
