import pandas as pd
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

df = pd.read_csv("glass.csv")
x_train = df.drop("Type",axis=1)
y_train = df["Type"]

x_train, x_test, y_train, y_test= train_test_split(x_train, y_train, test_size=0.4, random_state=0)

naive = GaussianNB()
naive.fit(x_train,y_train)
y_pred = naive.predict(x_test)
acc_naive = round(naive.score(x_test,y_test) * 100,2)

print("NB Accuracy Score:",acc_naive)
print("NB Classification Report:\n",classification_report(y_test,y_pred))