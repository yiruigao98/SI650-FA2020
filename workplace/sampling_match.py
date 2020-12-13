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
from preprocessing import *



# For sampling use: get the sampling query words
with open('../data/sample_queries.txt', 'r', encoding='utf-8') as f:
    sample_queries = f.read().splitlines()

# For sampling use: get the sampling documents
doc_filenames = listdir('../data/sample_docs2')
sample_docs = []
city_country_names = []
for i in range(len(doc_filenames)):
    line = doc_filenames[i].split('_')
    city_country_names.append((line[0], line[1]))
    with open('../data/sample_docs2/' + doc_filenames[i], 'r', encoding='utf-8') as df:
        doc = df.read()
        sample_docs.append(doc)

# Create a numpy array to store a matrix of documents and queries:
D = len(sample_docs)
Q = len(sample_queries)
output_arr = np.zeros((D, Q), dtype = 'int64')

for ind1, doc in enumerate(sample_docs):
    doc = str(doc)
    name = city_country_names[ind1][0].lower()
    # print(name, ind1)
    tokens = preprocess(doc, name)
    for ind2, query in enumerate(sample_queries):
        if query.lower() in tokens:
            if tokens.count(query.lower()) > 1:
                output_arr[ind1, ind2] = 1

# print(output_arr)
df = pd.DataFrame(output_arr, index = city_country_names, columns = sample_queries)
df.to_csv('sample_result2.csv')

sums = df.sum(axis = 0, skipna = True)
print(list(zip(sample_queries, sums)))
