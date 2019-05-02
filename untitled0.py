import numpy as np
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn import linear_model
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from gensim.models import doc2vec
from collections import namedtuple

def get_tag_and_training_data(filename):
    '''takes the input file and returns  tokenized sentences and document tags as separate lists'''
    tags=[]
    documents=[]
    line_counter=1
    with open(filename) as f:
        for line in f:
            #skip first line
            if line_counter==1:
                line_counter=line_counter+1
                continue
            #Initialize the token list for line
            tags.append(int(line[:1]))
            documents.append(line[2:])
    return tags,documents

Y,X=get_tag_and_training_data('Data/trainingdata.txt')

Y_train,Y_test=Y[:4120],Y[4120:]
count_vectorizer = CountVectorizer()
count_vectorizer.fit_transform(X)
freq_term_matrix = count_vectorizer.transform(X)
tfidf = TfidfTransformer(norm="l2")
tfidf.fit(freq_term_matrix)
tf_idf_matrix = tfidf.transform(freq_term_matrix)

X_train,X_test=tf_idf_matrix[:4120],tf_idf_matrix[4120:]
logreg = linear_model.LogisticRegression(C=1e5)
logreg.fit(X_train,Y_train)
pred=logreg.predict(X_test)
accuracy_score(Y_test, pred)

clf = MultinomialNB()
clf.fit(X_train,Y_train)
nb_pred=clf.predict(X_test)
accuracy_score(Y_test, nb_pred)

logreg.predict(tfidf.transform((count_vectorizer.transform([""]))))