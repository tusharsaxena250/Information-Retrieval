from sklearn.feature_extraction.text import CountVectorizer

train_set = ("The sky is blue.", "The sun is bright.")
test_set = ("The sun in the sky is bright.",
"We can see the shining sun, the bright sun.")

count_vectorizer = CountVectorizer()
count_vectorizer.fit_transform(train_set)
print ("Vocabulary:", count_vectorizer.vocabulary)

# Vocabulary: {'blue': 0, 'sun': 1, 'bright': 2, 'sky': 3}

freq_term_matrix = count_vectorizer.transform(test_set)
print (freq_term_matrix.todense())

#[[0 1 1 1]
#[0 2 1 0]]

from sklearn.feature_extraction.text import TfidfTransformer

tfidf = TfidfTransformer(norm="l2")
tfidf.fit(freq_term_matrix)

print ("IDF:", tfidf.idf_)

# IDF: [ 0.69314718 -0.40546511 -0.40546511  0.        ]


tf_idf_matrix = tfidf.transform(freq_term_matrix)
print (tf_idf_matrix.todense())

# [[ 0.         -0.70710678 -0.70710678  0.        ]
# [ 0.         -0.89442719 -0.4472136   0.        ]]