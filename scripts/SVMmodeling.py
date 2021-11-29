from sklearn import svm
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from transfer_data import *

def SVM(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
    cols = X_train.columns
    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)

    X_test = scaler.transform(X_test)
    X_train = pd.DataFrame(X_train, columns=[cols])
    X_test = pd.DataFrame(X_test, columns=[cols])

    ##### Blueprint for this code is from https://www.kaggle.com/prashant111/svm-classifier-tutorial

    # Instantiate classifier with linear kernel and C=100.0
    lin_svc=svm.SVC(kernel = 'linear', C = 100.0, probability = True, random_state = 0) 
    lin_svc.fit(X_train, y_train)
    y_pred=lin_svc.predict(X_test)

    # Compute and print accuracy score
    print('Model accuracy score with linear kernel and C=100.0 : {0:0.4f}'. format(accuracy_score(y_test, y_pred)))

    # Difference in model accuracy between C = 100 and C = 1000 was minimal. Slight improvement from 1 to 100.


    # # Print the scores on training and test set
    # print('Training set score: {:.4f}'.format(linear_svc.score(X_train, y_train)))
    # print('Test set score: {:.4f}'.format(linear_svc.score(X_test, y_test)))

    # null_accuracy = y_test.value_counts()[0] / (y_test.value_counts()[0] + y_test.value_counts()[1])
    # print('Null accuracy score: {0:0.4f}'. format(null_accuracy))
    
    fileName = pick_file()

    X_2022 = get_2022stats(fileName)
    y_2022 = lin_svc.predict(X_2022)

    print(X_2022)
    print(y_2022)

    # classifier = lin_svc.fit(X_2022, y_2022)
    predictions = lin_svc.predict_proba(X_2022)

    addandsave_to_CSV(fileName, 'allLeague', y_2022, 'allLeague_prob', predictions[:,1], "SVM")



def main():
    X, y = get_allplayerstats()
    SVM(X, y)

if __name__ == "__main__":
    main()