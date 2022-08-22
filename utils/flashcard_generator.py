from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json as jsonify

from os import mkdir
from os.path import isdir

outdir = "../assets"

if not isdir(outdir):
    mkdir(outdir)

options = Options()
options.headless = True
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://quizlet.com/470235219/vince-gre-flash-cards/")
driver.find_element(By.CLASS_NAME,"siycb3m").click()
blocks = driver.find_elements(By.CLASS_NAME,"SetPageTerm-contentWrapper")

cards = {}

for block in blocks:
    word = block.find_element(By.CLASS_NAME,"SetPageTerm-wordText").text
    definition = block.find_element(By.CLASS_NAME,"SetPageTerm-definitionText").text
    image = block.find_element(By.CLASS_NAME,"SetPageTerm-image")
    if word:
        cards[word]={"definition": definition, 
                    "image":image.get_attribute("src")[image.get_attribute("src").rfind("https://"):]}

json_object = jsonify.dumps(cards, indent=4)

with open("../assets/GRE_flashcard.json", "w") as outfile:
    outfile.write(json_object)

driver.quit()

