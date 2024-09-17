class Model():

    def __init__(self, window=3): 
        self.window = window

    def fit(self, data):
        # Fit non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')
    def predict(self, data):
        # Predict non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')
    
    def evaluate(self, data):
        fit_data_cutoff =int (0.7 * len(data))
        fit_data = data[:fit_data_cutoff]
        test_data = data[fit_data_cutoff:]
        try:
            self.fit(fit_data)
        except Exception as e:
            if isinstance(e, NotImplementedError):
                pass
            else:
                raise Exception('Metodo implementato ma ha sollevato una eccezione {}'.format(e))
        evaluation_mae = []
        for i in range(len(test_data)):
            if i + self.window < len(test_data):
                prediction_no_fit1 = self.predict(test_data[i:i + self.window])
                evaluation_mae.append(abs(test_data[i + self.window]-prediction_no_fit1))

        evaluation_mae = sum(evaluation_mae)/len(evaluation_mae)

        return evaluation_mae


class TrendModel(Model):

    def __init__(self, window=3): 
        self.window = window
    
    def validate_data(self,data):
        if len(data) != self.window:
            raise ValueError('Passati {} mesi ma il modello richiede di averne {}'.format(len(data), self.window))
    
    def compute_avg_variation(self, data):
        prev_value = 0
        prec_value = data[0]
        var = 0
        for item in data:
            var = var + item - prec_value
            prec_value = item    
        avg_variation = var/(len(data)-1)
        # variations = [] 
        # item_prev = None 
        # for item in data:
        #     if item_prev is not None: 
        #          variations.append(item-item_prev)
        #     item_prev = item
        # avg_variation = sum(variations)/len(variations)
        return avg_variation
   
    def predict(self, data): 
        self.validate_data(data)
        prediction = data[-1] + self.compute_avg_variation(data)
        return prediction


class FitTrendModel(TrendModel):

    def fit(self, data):
          self.historical_avg_variation = self.compute_avg_variation(data)

    def predict(self, data):
        try:
            self.historical_avg_variation 
        except AttributeError:
            raise Exception('Il modello non è fittato!')

        self.validate_data(data)
        
        prediction = data[-1] + (self.historical_avg_variation + self.compute_avg_variation(data))/2
        return prediction
