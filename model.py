class Model():
    def fit(self, data):
        # Fit non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')
    def predict(self, data):
        # Predict non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')


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

    def prediction(self, data):
        try:
            self.historical_avg_variation 
        except AttributeError:
            raise Exception('Il modello non è fittato!')

        self.validate_data(data)
        
        prediction = data[-1] + (self.historical_avg_variation + self.compute_avg_variation(data))/2
        return prediction
