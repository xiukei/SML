from sklearn.svm import LinearSVC
import pandas as pd
import csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler, MinMaxScaler, Normalizer
from sklearn.linear_model import LogisticRegression
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import SGDClassifier
train = pd.read_csv('dataframe.csv')
test = pd.read_csv('test_data.csv')
# train = train[:100000]
y = train.author
X = train.drop('author', axis=1)


# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)

# print(X_train)
# print(y_train)

# Naive Bayes
# nb = MultinomialNB()
# nb.fit(X_train, y_train)
# y_pred = nb.predict(X_test)

ssCoder = StandardScaler()
mmCoder = MinMaxScaler()
nCoder = Normalizer()

X_ss = ssCoder.fit_transform(X)
# X_mm = mmCoder.fit_transform(X_ss)
# print(X_mm)
# X_n = nCoder.fit_transform(X_mm)
# print(X_n)
X = pd.DataFrame(X_ss)
test = ssCoder.transform(test)
print(test)

#
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print(X_train, y_train)


# Support Vector Machine
# svc = LinearSVC()
# svc.fit(X_train, y_train)
# print('hello')
# y_pred = svc.predict(X_test)

clf = SGDClassifier(loss='log')
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# svm_clf = Pipeline([
#     ("scaler", StandardScaler()),
#     ("svm_clf", LinearSVC(C=1, loss="hinge"))
# ])
# svm_clf.fit(X_train, y_train)
# print('hello')
# y_pred = svm_clf.predict(X_test)
# LogisticRegression()

# clf = LogisticRegression()
# clf.fit(X_train, y_train)
# y_pred = clf.predict(X_test)

# RandomForestClassifier()
# rfc = RandomForestClassifier(n_estimators=10)
# rfc.fit(X_train, y_train)
# y_pred = rfc.predict(X_test)

# DecisionTreeClassifier
# clf = tree.DecisionTreeClassifier(criterion='entropy')
# clf.fit(X_train, y_train)
# y_pred = clf.predict(X_test)

# KNeighborsClassifier
# knn_clf = KNeighborsClassifier(n_neighbors=5)
# knn_clf.fit(X, y)
# y_pred = knn_clf.predict(test)
# print(y_pred)

# Output results into csv file
# prediction_columns = ['Id', 'Predicted']
# output = pd.DataFrame({'Id': range(1, y_pred.shape[0] + 1),
#                        'Predicted': y_pred})
# output.to_csv('./prediction.csv', index=False)
print('accuracy %s' % accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
