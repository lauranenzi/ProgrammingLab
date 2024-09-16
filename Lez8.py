import matplotlib.pyplot as plt
from esParte6 import NumericalCSVFile
from EsParte8 import TrendModel
import statistics
         
shampoofile = NumericalCSVFile('shampoo_sales.csv')
lista_dati = shampoofile.get_data()
date= []
valori =[]
for dati in lista_dati:
    date.append(dati[0])
    valori.append(dati[1])


pred_class = TrendModel()
# print(predizione.predict([1,2,3]))   

valori_pred =[]
val_predclasse = []

n = 4 
for t in range(len(valori)):
        if t < n-1: 
            valori_pred.append(valori[t])
        else:            
            valori_pred.append(valori[t])
            data = valori_pred[t-n+1:t+1]
            val_predclasse.append(pred_class.predict(data))

pred = []
for t in range(2,len(valori)):
    pred.append((valori[t-2]+ valori[t-1]+ valori[t])/3)

def predizione(val, t):
            var1 = valori[t-1] - valori[t-2]
            var2 = valori[t] - valori[t-1]
            return (var1 + var2)/2
    
valori_pred =[]

for t in range(2,len(valori)):
       valori_pred.append(valori[t] + predizione(valori,t))



datapredsimple = date[3:]
datapredsimple.append('last')

# datapred = date[n:]
# datapred.append('last')
# # Creazione del grafico
# plt.plot(date,valori, label='valori')
# # plt.plot(datapredsimple,valori_pred, label='prediz_3')
# plt.plot(datapred,val_predclasse, label='prediz_n_classe')
# plt.title("Grafico a Linee")
# plt.legend()
# plt.xticks([])
# plt.xlabel("Date")
# plt.ylabel("Valori")
# plt.show()

print(statistics.mean(valori))