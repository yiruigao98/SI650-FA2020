from rank_bm25 import BM25Okapi, BM25L, BM25Plus
from preprocessing import *
from os import listdir
from sklearn.metrics import ndcg_score, dcg_score
import numpy as np
import pandas as pd



# For sampling use: get the sampling documents
doc_filenames = sorted(listdir('../data/sample_docs'))
sample_docs = []
city_country_names = []
for i in range(len(doc_filenames)):
    line = doc_filenames[i].split('_')
    city_country_names.append((line[0], line[1]))
    with open('../data/sample_docs/' + doc_filenames[i], 'r', encoding='utf-8') as df:
        doc = df.read()
        sample_docs.append(doc)

tokenized_corpus = []

for ind1, doc in enumerate(sample_docs):
    doc = str(doc)
    name = city_country_names[ind1][0].lower()
    # print(name)
    tokens = preprocess(doc, name)
    tokenized_corpus.append(tokens)


top_10_test_queries = [["waterfall"], ["silk"], ["desert"],["volcano"],["beer"],["coconut"],["seafood"]]
top_100_test_queries = [["football"], ["castle"], ["shopping"], ['monument'], ["forest"]]

bm25 = BM25L(tokenized_corpus, b = 0.5)

for q in top_100_test_queries:
    print("------------------{}------------------".format(q[0]))
    
    tokenized_query = q
    doc_scores = bm25.get_scores(tokenized_query)
    top_n = bm25.get_top_n(tokenized_query, city_country_names, n = 100)

    print([(pair[0].encode('utf-8'), pair[1].encode('utf-8'))for pair in top_n])

    # NDCG evaluations:
    relevance_score = [1 for i in range(100)]

    annotate_result = pd.read_csv('../data/annotate_result.csv', encoding='utf-8', header=0)

    true_relevence = []
    for top_city in top_n:
        true_relevence.append(annotate_result[annotate_result['city'] == str((top_city[0], top_city[1]))].squeeze()[q[0]])

    # Releveance scores in Ideal order 
    true_relevance = np.asarray([true_relevence]) 
    
    # Releveance scores in output order 
    relevance_score = np.asarray([relevance_score]) 
    

    print(ndcg_score( true_relevance, relevance_score))

