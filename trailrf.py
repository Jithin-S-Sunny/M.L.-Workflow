
import pandas as pd
import csv
dataframe1 = pd.read_csv("example2.txt", header=None)
dataframe1.to_csv('example2.csv', index = None)

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data=pd.read_csv("4glm.csv")
#print(data.sample(5))
#print(data.columns)
X = data.drop("target", axis=1)
y = data["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.10, random_state=42)
classifier = RandomForestClassifier(n_estimators=100)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
with open('example2.csv', newline='') as f:
  reader = csv.reader(f)
  row2 = next(reader)
y=classifier.predict([row2])
print(y)