from msilib.schema import Feature
from sklearn import svm
from sklearn.inspection import DecisionBoundaryDisplay
import matplotlib.pyplot as plt
import numpy as np


"""
This is a different Version of svm_classifier_singlespan_beam_2D.py
as a class.


FeatureVector and InputVector from the DataPreparaton need to be saved in some way.

"""


class EstimateCS():

    def __new__(
        self,
        d1 = int,
        d2 = int
    ):
        '''
            Dataset with which algorithm is trained

            x = np.array with data about the problem (In 2D case: length & magnitude of line load)

            y = corresponding section

        '''

        """

        Here should the result from dataPrepOptimization.py go

        x = InputVector
        y = FeatureVector

        """

        x = np.array([[15, 7], [14, 13], [5, 5], [23, 3], [2, 2]])
        y = ['IPE 300', 'IPE 200', 'IPE 700', 'IPE 500', 'IPE 120']

        #machine learning model
        C = 1.0
        clf = svm.SVC(kernel = "poly", degree = 3, gamma = "auto", C=C)
        clf.fit(x,y)


        """
        #user input for their system
        d1 = input("Please type length: ")
        d2 = input("Please type loading: ")

        """

        #predicted section
        PredictedCS = clf.predict([[d1, d2]])

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


        return PredictedCS[0]

