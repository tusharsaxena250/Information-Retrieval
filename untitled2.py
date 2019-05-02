import sklearn as sk
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

document = pd.read_fwf("f-t2.txt")

vect = TfidfVectorizer()
tfidf_matrix = vect.fit_transform(document)
df = pd.DataFrame(tfidf_matrix.toarray(), columns = vect.get_feature_names())
print(df)



#x = np.array([[1,2,3,4]])
#y = np.array([[1,2,0,0]])
#
#z = sk.metrics.pairwise.cosine_similarity(x,y)
#
#
#from sklearn.metrics.pairwise import cosine_similarity 
#print(cosine_similarity(x,y))