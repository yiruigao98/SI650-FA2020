import nltk
from os import listdir
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import numpy as np
from numpy import savetxt
import pandas as pd


stop_words = set(stopwords.words('english'))
stemmer= PorterStemmer()
lemmatizer=WordNetLemmatizer()


def text_lower(text):
    return text.lower()

def remove_empty_lines(text):
    return text.replace('\\n', ' ')

def remove_ending_blocks(text):
    # target_block = ['== See also ==','== References ==','== External links ==','=== Notable people ===']
    target_block = ['== See also ==','== References ==','== External links ==']
    for target in target_block:
        start_i = text.find(target)
        if start_i != -1:
            text = text[:start_i]
        
    return text

def remove_block_title(text):
    return re.sub(r'[=]+\s[a-z\s]+\s[=]+', '', text)

def remove_extra_blanks(text):
    return re.sub(' {2,}', ' ', text)

def remove_punc(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def remove_spec_char(text):
    return re.sub(r'[^A-Za-z0-9\s]+', '', text)

def tokenize(text):
    tokens = word_tokenize(text)
    return [i for i in tokens if not i in stop_words]

def stemming(word_list):
    return [stemmer.stem(word) for word in word_list]

def lemmatize(word_list):
    return [lemmatizer.lemmatize(word) for word in word_list]

def remove_city_name(word_list, name):
    return [word for word in word_list if word != name]

# Preprocess the sample documents:
def preprocess(doc, city_name):
    # Remove several ending blocks
    doc = remove_ending_blocks(doc)
    # Lower the letters
    doc = text_lower(doc)
    # Remove empty lines
    doc = remove_empty_lines(doc)

    # Remove block titles:
    doc = remove_block_title(doc)
    # Remove extra blank spaces:
    doc = remove_extra_blanks(doc)
    # Remove punctuations:
    doc = remove_punc(doc)
    # Remove speacial characters:
    doc = remove_spec_char(doc)

    # Tokenization:
    tokens = tokenize(doc)
    # Stemming:
    # tokens = stemming(tokens)
    # Lemmatizing:
    tokens = lemmatize(tokens)
    # Remove city names:
    tokens = remove_city_name(tokens, city_name)

    return tokens




