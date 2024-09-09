# Definizione della classe CSVFile
class CSVFile():
    
    # Metodo costruttore della classe, inizializza l'attributo 'name' con il nome del file
    def __init__(self, name):
        self.name = name

    # Metodo per ottenere i dati dal file CSV
    def get_data(self):
        try:
            # Apertura del file in modalità lettura
            my_file = open(self.name, 'r')
            my_list = []
            # Scorrimento di ogni riga del file
            for line in my_file:
                # Divido la riga in elementi separati da virgola
                elements = line.split(',')
                # Rimuovo eventuali spazi vuoti o caratteri di nuova linea alla fine
                elements[-1] = elements[-1].strip()
                # Salto l'intestazione se la prima colonna contiene 'Date'
                if elements[0] != 'Date':
                    my_list.append(elements)
            # Chiudo il file
            my_file.close()
            # Ritorno la lista dei dati letti dal file
            return my_list

        # Gestione dell'eccezione nel caso il file non venga trovato
        except FileNotFoundError:
            print('Errore: il file non esiste')


# Definizione della classe NumericalCSVFile, che eredita dalla classe CSVFile
class NumericalCSVFile(CSVFile):

    # Sovrascrittura del metodo get_data
    def get_data(self):
        # Chiamo il metodo get_data della classe base (CSVFile) per ottenere i dati grezzi
        lista_dati = super().get_data()

        # Lista per contenere i dati convertiti in numeri
        numerical_data = []

        # Scorro ogni riga nella lista dei dati
        for riga in lista_dati:
            # Lista per la riga convertita (se possibile) in numeri
            numerical_row = []

            # Scorro ogni elemento della riga
            for i, elemento in enumerate(riga):
                # Il primo elemento (indice 0) è mantenuto come stringa (es. la data)
                if i == 0:
                    numerical_row.append(elemento)
                else:
                    try:
                        # Provo a convertire l'elemento in float
                        numerical_row.append(float(elemento))
                    # Se c'è un errore di conversione, lo segnalo e interrompo la lettura della riga
                    except ValueError as e:
                        print('Il valore "{}" non è un numero. Errore: "{}" '.format(elemento, e))
                        break

            # Se la riga originale ha lo stesso numero di elementi convertiti, la aggiungo alla lista finale
            if len(riga) == len(numerical_row):
                numerical_data.append(numerical_row)

        # Ritorno la lista dei dati numerici
        return numerical_data


# Creo un'istanza della classe NumericalCSVFile con il nome del file 'shampoo_sales.csv'
shampoofile = NumericalCSVFile('shampoo_sales.csv')

# Chiamo il metodo get_data per ottenere i dati numerici
lista_dati = shampoofile.get_data()

# Stampo i dati ottenuti
print(lista_dati)
