import json
import requests
from os import mkdir
from os.path import isdir

outdir = "../assets/images/"

if not isdir(outdir):
    mkdir(outdir)

with open("../assets/GRE_flashcard.json", "r") as file:
    cards = file.read()
cards = json.loads(cards)
for word, value in cards.items():
    print(word, value["image"])

    out =  outdir + word + ".png"
    url = value["image"]

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)

    with open(out, 'wb') as handler:
        handler.write(response.content)
