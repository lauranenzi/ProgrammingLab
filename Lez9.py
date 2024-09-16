class Model():
    def fit(self, data):
        # Fit non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato') 
    def predict(self, data):
        # Predict non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato')
    
class TrendModel(Model):
    def predict(self, data): 
        if len(data) < 2:
            raise Exception('Errore: devo avere almeno due valori')
        prev_value = 0
        prec_value = data[0]
        var = 0
        for item in data:
            var = var + item - prec_value
            prec_value = item    
        
        prediction = data[-1] + var/(len(data)-1)
        return prediction
    
