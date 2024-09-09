# Definizione della classe CSVFile
class CSVFile():
    
    # Metodo costruttore della classe, inizializza l'attributo 'name' con il nome del file
    def __init__(self, name):
        self.name = name
        if not isinstance(self.name, str):
            raise Exception('Errore: il nome del file non è una stringa')

    # Metodo per ottenere i dati dal file CSV
    def get_data(self, start=None, end=None):
        if start is not None or end is not None:
            if not isinstance(start, int):
                raise Exception(
                    'Errore: il parametro start non è un intero')
            elif not isinstance(end, int):
                raise Exception('Errore: il parametro end non è un intero')
            elif start <= 0:
                raise Exception(
                    'Errore: il parametro start non è un intero positivo')
            elif end < start:
                raise Exception(
                    'Errore: il parametro start è maggiore di end')      
        try:
            # Apertura del file in modalità lettura
            my_file = open(self.name, 'r')
            my_list = []
            # Scorrimento di ogni riga del file
            for i, line in enumerate(my_file):
                if (start==None and end==None) or (start <= i <= end):
                    # Divido la riga in elementi separati da virgola
                    elements = line.split(',')
                    # Rimuovo eventuali spazi vuoti o caratteri di nuova linea alla fine
                    elements[-1] = elements[-1].strip()
                    # Salto l'intestazione se la prima colonna contiene 'Date'
                    if elements[0] != 'Date':
                        my_list.append(elements)
            # Chiudo il file
            my_file.close()
            if isinstance(end, int) and len(my_list)+1 < end:
                raise Exception(
                    'Errore: il parametro end {} è maggiore del numero di righe {}'.format(end,len(my_list))) 
             
            # Ritorno la lista dei dati letti dal file
            return my_list

        # Gestione dell'eccezione nel caso il file non venga trovato
        except FileNotFoundError:
            print('Errore: il file non esiste')
            


# Definizione della classe NumericalCSVFile, che eredita dalla classe CSVFile
class NumericalCSVFile(CSVFile):

    # Sovrascrittura del metodo get_data
    def get_data(self, *args, **kwargs):
        # Chiamo il metodo get_data della classe base (CSVFile) per ottenere i dati grezzi
        lista_dati = super().get_data(*args, **kwargs)

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
    

shampoofile = CSVFile('shampoo_sales.csv')
lista_dati = shampoofile.get_data(3.3, 3.5)
print(lista_dati)
