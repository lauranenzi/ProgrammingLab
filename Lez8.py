import matplotlib.pyplot as plt
from esParte6 import CSVFile 

# Dati di esempio
csv_file = CSVFile('test_file.csv')
data = csv_file.get_data(start=1, end=2)

# # Creazione del grafico
# plt.plot(x, y)
# plt.title("Grafico a Linee")
# plt.xlabel("Asse X")
# plt.ylabel("Asse Y")
# plt.show()