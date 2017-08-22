from sklearn.linear_model import RidgeCV
from sklearn.linear_model import LinearRegression
import numpy as np


class PositiveRidgeCV(RidgeCV):
    def predict(self, X):
        y = super(PositiveRidgeCV, self).predict(X)
        y = np.maximum([0] * len(y), y)
        return y


class PositiveLinearRegression(LinearRegression):
    def predict(self, X):
        y = super(LinearRegression, self).predict(X)
        y = np.maximum([0] * len(y), y)
        return y
