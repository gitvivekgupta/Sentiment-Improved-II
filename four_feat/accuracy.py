import csv
import json
import pandas as pd
from matplotlib import cm
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# icon = pd.read_csv('var_compute.csv.csv')
# icon = pd.read_csv('level_compute.csv.csv')

X = icon[['pos_score', 'neu_score', 'neg_score', 'sub_score']]
y = icon['value']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

myList = list(range(1,800))
neighbors = myList

scores = []
k_value = []

for k in neighbors:
    k_value.append(k)
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    score = knn.score(X_test, y_test)
    scores.append(score)

plt.plot(scores)

plt.ylabel('Accuracy Score')

plt.show()

scores.sort()
print(scores[-1])

k_value.sort()
print(scores[-1])
