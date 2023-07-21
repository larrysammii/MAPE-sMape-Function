# MAPE & sMAPE functions

from sklearn.linear_model import LinearRegression
import numpy as np

# For self-learning purposes only. 
# If necessary (usually the case I guess for actual datasets),
# change the instance type of y_true & y_pred to array instead of int.

# Mean Average Percentage Error
def mape(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred)/y_true)) * 100

# symmetric Mean Average Percentage Error
def smape(y_true, y_pred):
    return np.mean(np.abs(np.sum(2 * np.abs(y_pred - y_true) / (np.abs(y_true) + np.abs(y_pred))))) * 100

# To demonstrate the MAPE formula (or a flaw of this formula)
# It favours the predicted values lowered than the actual values
# The above case is vice versa for the sMAPE formula
# Lowered the MAPE / sMAPE the better

y_true = 90 
y_pred = 70

print(mape(y_true, y_pred))

y_true = 70
y_pred = 90

print(mape(y_true, y_pred))

#######################################################################

"""

Bonus:
To find a point on the predicted linear regression model,
use sklearn's .predict method, and an reshaped array.

"""

X = np.array([4, 6, 8, 10, 12, 14, 16]).reshape(-1, 1)
y = np.array([2, 2, 3, 5, 5, 6, 6]).reshape(-1, 1)

linreg = LinearRegression().fit(X, y)

# To find the 23th point on the predicted linear regression
# I'm still figuring out why .reshape is (1, 1) not (-1, 1), I'm still learning.

predictions = linreg.predict(np.array([23]).reshape(1,1))

print(predictions)