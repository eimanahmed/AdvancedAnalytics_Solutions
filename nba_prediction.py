from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import pandas as pd
import math

nba_data = pd.read_csv("nba_logreg.csv")
nba_data = nba_data.dropna()

y = nba_data['TARGET_5Yrs']
X = nba_data.drop('TARGET_5Yrs', axis=1)
X = X.drop('Name', axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

model = LogisticRegression(solver='liblinear')
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

#confusion_matrix = metrics.confusion_matrix(y_test, y_pred)
#print(confusion_matrix)

accuracy = metrics.accuracy_score(y_test, y_pred)
print("Accuracy: ", accuracy)
