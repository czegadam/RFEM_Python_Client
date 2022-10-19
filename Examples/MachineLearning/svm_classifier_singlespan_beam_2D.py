from sklearn import svm
from sklearn.inspection import DecisionBoundaryDisplay
import matplotlib.pyplot as plt
import numpy as np

'''
    Dataset with which algorithm is trained

    x = np.array with data about the problem (In 2D case: length & magnitude of line load)

    y = corresponding section

'''
x = np.array([[15, 7], [14, 13], [5, 5], [23, 3], [11, 12]])
y = ['IPE 300', 'IPE 200', 'IPE700', 'IPE500', 'IPE120']

#machine learning model
C = 1.0
clf = svm.SVC(kernel = "poly", degree = 3, gamma = "auto", C=C)
clf.fit(x,y)

#user input for their system
d1 = input("Please type length: ")
d2 = input("Please type loading: ")

#predicted section
print(clf.predict([[d1, d2]]))

X0, X1 = x[:, 0], x[:, 1]

#Plotting areas of different sections
disp = DecisionBoundaryDisplay.from_estimator(clf,
    x,
    response_method = "predict",
    cmap = "Pastel1",
    alpha = 1,
    ax = None ,
    xlabel = None,
    ylabel = None)

#It would be nice to show the user input point on the colored map
plt.scatter(X0, X1, c="red", s=20, edgecolors="k")
plt.show()
