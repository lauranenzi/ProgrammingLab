from model import TrendModel
from model import FitTrendModel


# Definisco dei dati di test
test_data = [50,52,60]


# Istanzio il modello
trend_model = TrendModel()

# Testo che la lungezza della finestra di default venga settata a 3
if trend_model.window != 3:
    raise Exception('Il modello non ha una finestra di default pari a 3,' +
' ma di {}'.format(trend_model.window))

 # Applico il modello
prediction = trend_model.predict(test_data)


# Testo che il risultato sia corretto
if prediction != 65:
    raise Exception('Il modello sbaglia la prediction: ha ' +
    'dato {} invece di 65'.format(prediction))


# su dei dati con un numero di mesi diverso da 3: 
wrong_test_data = [50,52,60,70]
try:
    trend_model.predict(wrong_test_data) 
except ValueError:
    pass 
else:
    raise Exception('Il modello non alza alcuna eccezione ' + 'se applicato su un numero di mesi ' +
                      'diverso da 3')



# Infine tetso il modello con una finstra di lunghezza # diversa da quella di default di 3 mesi
trend_model = TrendModel(window=4)


# Testo che la lungezza della finestra sia stata settata a 4
if trend_model.window != 4:
    raise Exception('Il modello non ha settata una finestra pari a 4,' +
' ma di {}'.format(trend_model.window))


# Applico il modello con finestra di 4 mesi
test_data_new = [50,52,60,65]
prediction = trend_model.predict(test_data_new)


# Testo che il risultato sia corretto
if prediction != 70:
    raise Exception('Il modello sbaglia la previsione: ha ' +
    'dato {} invece di 70'.format(prediction))


# Infine tetso il modello con una finstra di lunghezza # diversa da quella di default di 3 mesi
trend_model = FitTrendModel(window=3)

# Testo che la lungezza della finestra sia stata settata a 3
if trend_model.window != 3:
    raise Exception('Il modello non ha settata una finestra pari a 3,' +
' ma di {}'.format(trend_model.window))

all_data = [8,19,31,41,50,52,60]
historical_data = [8,19,31,41]
test_data = [50,52,60]
prediction_true = 68

trend_model.fit(historical_data)
prediction = trend_model.prediction(test_data)

# Testo che il risultato sia corretto
if prediction != 68:
    raise Exception('Il modello sbaglia la previsione: ha ' +
    'dato {} invece di 68'.format(prediction))

print('ALL TESTS PASS')