import json
import pandas as pd
import numpy as np

with open('assets/flashcard_new.json') as f:
    flashcard = json.load(f)

word = input('Enter the word: ')

while word != '':
    meaning = input('Enter the meaning: ')
    flashcard[word]['meaning'] =  meaning
    vocab_output = 'assets/flashcard_new.json'
    json_file = open(vocab_output, 'w+')
    json.dump(flashcard, json_file, indent = 4)
    word = input('Enter the word: ')
