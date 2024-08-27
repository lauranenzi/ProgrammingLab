class CSVFile():

    def __init__(self, name):
        self.name = name
        if not isinstance(self.name, str):
            raise Exception('Errore: il nome del file non è una stringa')

    def get_data(self, start=None, end=None):
        try:
            my_file = open(self.name, 'r')
            my_list = []

            i = 1

            for line in my_file:
                elements = line.split(',')
                if elements[0] != 'Date':
                    try:
                        elements[-1] = elements[-1].strip()
                        my_list.append(elements)
                    except IndexError:
                        print(
                            'Errore: la riga "{line}" non ha abbastanza elementi'
                            .format(line=line))
                i += 1
            my_file.close()

            if start is not None and end is not None:
                if not isinstance(start, int):
                    raise Exception(
                        'Errore: il parametro start non è un intero')
                elif start <= 0:
                    raise Exception(
                        'Errore: il parametro start non è un intero positivo')
                elif not isinstance(end, int):
                    raise Exception('Errore: il parametro end non è un intero')
                elif len(my_list) < start:
                    raise Exception(
                        'Errore: il parametro start è maggiore del numero di righe'
                    )
                elif end < start:
                    raise Exception(
                        'Errore: il parametro end è maggiore di start')
                else:
                    my_list = my_list[int(start):int(end)]
            return my_list

        except FileNotFoundError:
            print('Errore: il file non esiste')


class NumericalCSVFile(CSVFile):

    def __init__(self, name):
        self.name = name

    def get_data(self, *args, **kwargs):
        lista_dati = super().get_data(*args, **kwargs)
        for elemento in lista_dati:
            try:
                elemento[1] = float(elemento[1])
            except ValueError:
                print('Errore: il valore "{}" non è un numero'.format(
                    elemento[1]))
        return lista_dati


shampoofile = NumericalCSVFile('shampoo_sales.csv')
lista_dati = shampoofile.get_data(3, 5)
print(lista_dati)
