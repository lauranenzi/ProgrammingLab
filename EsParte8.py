class TrendModel():
    def predict(self, data): 
        # if len(data) < 2:
        #     rraise ValueError('Errore: devo avere almeno due valori')
        if len(data) != 3:
            raise ValueError('Passati {} mesi ma il modello richiede di averne almeno 3'.format(len(data)))
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
        
        prediction = data[-1] + avg_variation
        return prediction
    