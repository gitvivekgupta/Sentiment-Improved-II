import csv
import time
import pandas as pd
from matplotlib import cm
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier

# icon = pd.read_csv('same_score_data.csv')
icon = pd.read_csv('diff_score_data.csv')

# norm = pd.read_csv('norm_same_score_data.csv')
# norm = pd.read_csv('norm_diff_score_data.csv')

X = icon[['pos_score', 'neu_score', 'neg_score']]
# X = norm[['score']]
y = icon['value']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

myList = list(range(1,800))
neighbors = myList

n = []
k_val = []
cv_scores = []

for k in neighbors:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    score = knn.score(X_test, y_test)
    k_val.append(k)
    n.append(score)

plt.plot(n)
plt.xlabel('Value of k')
plt.ylabel('Accuracy Score')
plt.show()

n, k_val = zip(*sorted(zip(n, k_val)))

print(n[-1], "||", k_val[-1])


for kk in neighbors:
    knn = KNeighborsClassifier(n_neighbors=kk)
    scores = cross_val_score(knn, X_train, y_train, cv=10, scoring='accuracy')
    cv_scores.append(scores.mean())


MSE = [1 - x for x in cv_scores]

optimal_k = neighbors[MSE.index(min(MSE))]
print("The optimal number of neighbors is %d" % optimal_k)

plt.plot(neighbors, MSE)
plt.xlabel('Number of Neighbors K')
plt.ylabel('Misclassification Error')
plt.show()
