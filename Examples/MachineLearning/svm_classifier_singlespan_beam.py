from sklearn import svm
from sklearn.inspection import DecisionBoundaryDisplay
import matplotlib.pyplot as plt
import numpy as np

'''
    Dataset with which algorithm is trained

    x = np.array with data about the problem
        ([[length, magnitude of load, max. displacement,
            loading_type]]

    y = corresponding section

'''
x = np.array([[12, 10, 83, 1], [14, 123, 23, 2], [5, 5, 53, 3], [23, 3, 21, 4], [11, 123, 89, 5]])
y = ['IPE 300', 'IPE 200', 'IPE700', 'IPE500', 'IPE120']

#machine learning model
C = 1.0
clf = svm.SVC(kernel = "poly", degree = 3, gamma = "auto", C=C)
clf.fit(x,y)

#user input for their system
d1 = input("Please type length: ")
d2 = input("Please type loading: ")
d3 = input("Please type max. displacement: ")
d4 = input("Please type loading_type: ")

print(clf.predict([[d1, d2, d3, d4]]))
