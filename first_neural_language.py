"""
@author: Yossi Shor
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
from nltk import download
from nltk.corpus import stopwords
download('stopwords')
from nltk.stem.porter import PorterStemmer 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score



t = re.sub('[^a-zA-Z1-9]','')
dataset = pd.read_csv(r'C:\src\P14-Natural-Language-Processing\Natural_Language_Processing\Restaurant_Reviews.tsv', delimiter = '\t')
review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][0]).lower().split()
ps = PorterStemmer()
review = ' '.join([ps.stem(word) for word in review if not word in set(stopwords.words('english'))])
#e = stopwords.words('english')

new = []
for i in range(len(dataset)):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i]).lower().split()
    ps = PorterStemmer()
    review = ' '.join([ps.stem(word) for word in review if not word in set(stopwords.words('english'))])
    new.append(review)
    


cv = CountVectorizer(max_features = 1500)    
X = cv.fit_transform(new).toarray()
X.shape
Y = dataset.iloc[:,1].values
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)
x = X


random_Classifier = RandomForestClassifier(criterion = 'entropy', n_estimators = 10, random_state = 0)
random_Classifier.fit(x_train, y_train)
ran_pre = random_Classifier.predict(x_test)
print(ran_pre)
print(accuracy_score(y_test, ran_pre))


dtclassifier = DecisionTreeClassifier(criterion = 'gini')
dtclassifier.fit(x_train, y_train)
y_pre = dtclassifier.predict(x_test)
print(y_pre)
print(accuracy_score(y_test, y_pre))
print(confusion_matrix(y_test, y_pre))

dtclassifier = DecisionTreeClassifier(criterion = 'entropy')
dtclassifier.fit(x_train, y_train)
y_pre = dtclassifier.predict(x_test)
print(y_pre)
print(accuracy_score(y_test, y_pre))


classifier = GaussianNB()
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)

confu = confusion_matrix(y_test, y_pred)
print((confu[0][0] + confu[1][1]) / 250)

accu = accuracy_score(y_test, y_pred)
print(accu)



