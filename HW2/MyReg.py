# arif akkan
# a simple linear regressor for x and y values, for multiple values we can exploit for loops and get multiple coeffs

import numpy as np
import pandas


def myreg(x, y):
# we calculate the #B^ coefficient by x,y and transpose of x
    xtrp = np.transpose(x)
    ytrp = np.transpose(y)

    bhat = np.linalg.inv(xtrp @ x) @ xtrp @ y

# x must be nx2 1 column of 1's, which gives b0 at the end. any number coeff should work

#we can calculate error term by subtracting the predictions from original"
    e = np.subtract(y, (x @ bhat))


#"finding the variance"
    etrp= np.transpose(e)
    numrow, numcol = np.shape(x)
    varsq= (etrp @ e) / (numrow - numcol - 1)

# finding variance of coeff
    varb= np.diag(np.multiply(varsq, np.linalg.inv(x.T @ x)))
    sterr= np.sqrt(varb).reshape(2,1)


# I will use %95 conf interval
    z=1.96
    confint=[bhat - z*sterr, bhat + z*sterr]

    #print("Regression coefficient b0,B-hat= ", bhat, "\nStandard Error: ", sterr, "\nConfidence interval of Regressor: ", confint)
    return bhat, sterr, confint
