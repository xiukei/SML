from sklearn.svm import SVC
import numpy as np
import pandas as pd
import csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler
train = pd.read_csv('dataframe.csv')
test = pd.read_csv('test_data.csv')
# train = train[:10000]
y_train = train.author
X_train = train.drop('author', axis=1)
X_test = test
# print (X)
# print (y)

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print (X_train)
print (y_train)
# nb = MultinomialNB()
# nb.fit(X_train, y_train)
# y_pred = nb.predict(X_test)
# for data in y_pred:
#     print(data)
# svc = SVC(kernel='poly', gamma='scale', max_iter=1000)
# svc.fit(X_train, y_train)
# print('hello')
# y_pred = svc.predict(X_test)

rfc = RandomForestClassifier(n_estimators=50, random_state=120)
rfc.fit(X_train, y_train)
y_pred = rfc.predict(X_test)
print(y_pred)
prediction_columns = ['Id', 'Predicted']
# try:
#     with open('prediction.csv', 'wb') as f:
#         writer = csv.DictWriter(f, fieldnames=prediction_columns)
#         writer.writeheader()
#         for row in y_pred:
#             writer.writerow(row)
# except IOError as (errno, strerror):
#     print('I/O error({0}): {1}'.format(errno, strerror))
output = pd.DataFrame({'Id': range(1, y_pred.shape[0] + 1),
                       'Predicted': y_pred})
output.to_csv('./prediction.csv', index=False)
# print('accuracy %s' % accuracy_score(y_pred, y_test))
# print(confusion_matrix(y_test, y_pred))
# print(classification_report(y_test, y_pred))
