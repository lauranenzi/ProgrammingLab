from model import TrendModel
from model import FitTrendModel

test_dataset = [1,2,3,4,5,6,7,8,9,10.5,11.5,11.2]
fit_dataset = [1,2,3,4,5,6,7]
evaluation_data_set = [9,10.5,11.5,11.2]
evaluation_data_set1 = [9,10.5]
evaluation_data_set2 = [10.5,11.5]
prediction_true = [11.5,11.2]

# fit_dataset = [8,19,31,41,50,52,60]
# evaluation_data_set = [67,72,72, 67, 72]
# evaluation_data_set1 = [67,72,72]
# evaluation_data_set2 = [72,72,67]
# prediction_true = [65,76]

# Istanzio il modello
trend_model_no_fit = TrendModel( window = 2)


prediction_no_fit1 = trend_model_no_fit.predict(evaluation_data_set1)
prediction_no_fit2 = trend_model_no_fit.predict(evaluation_data_set2)
test_value = [prediction_no_fit1, prediction_no_fit2]

def evaluation(test_value, prediction_true):
    mae = 0
    for i, prediction in enumerate(prediction_true):
        var = abs(prediction - test_value[i])
        mae = mae  + var
    mae = mae/len(prediction_true)
    return mae

print(evaluation(test_value, prediction_true))


trend_model_no_fit.evaluate(test_dataset)

    




