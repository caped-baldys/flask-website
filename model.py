from joblib import Parallel, delayed
import joblib
import pandas as pd

# reading trained model

logistic_reg_autism = joblib.load('logistic_regression_autism.pkl')
random_forest_autism = joblib.load('random_forest_autism.pkl')
print("Model loaded")


def pred_randomforest(data,age,sex):
    age = int(age)
    sex = 1 if sex == 'M' else 0
    dim = [[data[0],	data[1], data[2],	data[3], data[4],	data[5], data[6],	data[7],
            data[8], data[9], age,	sex,	1,	0,	False,	False,	False,	False,	False,	False,
            False,	False,	True,	False,	False,	False,	False,	False,	False,	True]]
    return (True if random_forest_autism.predict(dim) == [1] else False)


def logistic_reg(data,age,sex):
    age = int(age)
    sex = 1 if sex == 'M' else 0
    dim = [[data[0],	data[1], data[2],	data[3], data[4],	data[5], data[6],	data[7],
            data[8], data[9], age,	sex,	1,	0,	False,	False,	False,	False,	False,	False,
            False,	False,	True,	False,	False,	False,	False,	False,	False,	True]]
    return (True if logistic_reg_autism.predict(dim) == [1] else False)


# data = [1, 1, 1, 1, 1, 0, 1, 0, 1, 1]
# print(logistic_reg(data))
