# Definizione della classe CSVFile
class CSVFile():
    
    # Metodo costruttore della classe, inizializza l'attributo 'name' con il nome del file
    def __init__(self, name):
        self.name = name
        if not isinstance(self.name, str):
            raise Exception('Errore: il nome del file non è una stringa')
        
        # Provo ad aprirlo e leggere una riga
        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
            my_file.close()
        except Exception as e:
            self.can_read = False
            print('Errore in apertura del file: "{}"'.format(e))
        
        

    # Metodo per ottenere i dati dal file CSV
    def get_data(self, start=None, end=None):
        if start is not None:
            if not isinstance(start, int):
                raise Exception(
                    'Errore: il parametro start non è un intero')
            elif start <= 0:
                raise Exception(
                'Errore: il parametro start non è un intero positivo')
        if end is not None:
                if not isinstance(end, int):
                    raise Exception('Errore: il parametro end non è un intero')
        if isinstance(start, int) and isinstance(end, int):
            if end < start:
                raise Exception('Errore: il parametro start è maggiore di end')  
        intestazione = False
        try:               
            # Apertura del file in modalità lettura
            my_file = open(self.name, 'r')
            my_list = []
            # Scorrimento di ogni riga del file
            for i, line in enumerate(my_file):
                    # Divido la riga in elementi separati da virgola
                    elements = line.split(',')
                    # Rimuovo eventuali spazi vuoti o caratteri di nuova linea alla fine
                    elements[-1] = elements[-1].strip()
                    # Salto l'intestazione se la prima colonna contiene 'Date'
                    if elements[0] != 'Date':
                        my_list.append(elements)
                    else:
                        intestazione = True
            # Chiudo il file
            my_file.close()
            if intestazione == True:
                lenlist = len(my_list) +1    
                if isinstance(end, int):
                    end = end - 1
                if isinstance(start, int):
                    start = start-1
            else:
                lenlist = len(my_list)
            if isinstance(start, int):
                if lenlist < start:
                    raise Exception(
                    'Errore: il parametro start {} è maggiore del numero di righe {}'.format(start,lenlist)) 
                if isinstance(end, int):
                    if lenlist < end :
                        raise Exception(
                            'Errore: il parametro end {} è maggiore del numero di righe {}'.format(end,lenlist))             
                    my_list = my_list[start-1 : end] 
                else:
                    print(my_list)
                    my_list = my_list[start-1:] 
                    print(my_list)
            else:
                if isinstance(end, int):
                    if lenlist < end:
                        raise Exception(
                            'Errore: il parametro end {} è maggiore del numero di righe {}'.format(end,lenlist))                  
                    my_list = my_list[:end] 

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
    

shampoofile = CSVFile('test_file.csv')
lista_dati = shampoofile.get_data(start=1, end=39)
print(lista_dati)
