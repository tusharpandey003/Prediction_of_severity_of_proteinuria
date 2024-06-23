import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("proteinuria_patient_dataset")
df = df.drop(df.columns[0], axis=1)

X = df[df.columns[:-1]].values
y = df[df.columns[-1]].values


X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.2, random_state=0)
X_valid, X_test, y_valid, y_test = train_test_split(
    X_temp, y_temp, test_size=0.4, random_state=0)


classify = RandomForestClassifier()
classify.fit(X_train, y_train)


def patient_prediction(info):
    prediction = classify.predict(info)
    if prediction == 0:
        return ('Yours reports are satisfactory and we have noted that you have mild symptoms.')
    elif prediction == 1:
        return ('Your reports are now available. We have reviewed the information and noted that you are experiencing moderate symptoms. We strongly recommend that you take the necessary steps to care for your wellbeing , as failure to do so could lead to a worsening of your condition.')
    else:
        return ('Your reports are now available. We have reviewed the information and noted that you are experiencing "Severe" symptoms. We strongly recommend that you take the necessary steps to care for your wellbeing , as failure to do so could lead to a worsening of your condition.')
