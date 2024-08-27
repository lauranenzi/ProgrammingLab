class CSVFile():

    def __init__(self, name):
        self.name = name

    def get_data(self):
        try:
            my_file = open(self.name, 'r')
            my_list = []
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
            my_file.close()
            return my_list

        except FileNotFoundError:
            print('Errore: il file non esiste')


class NumericalCSVFile(CSVFile):

    def __init__(self, name):
        self.name = name

    def get_data(self):
        lista_dati = super().get_data()
        for elemento in lista_dati:
            try:
                elemento[1] = float(elemento[1])
            except ValueError:
                print('Errore: il valore "{}" non è un numero'.format(
                    elemento[1]))
        return lista_dati


shampoofile = NumericalCSVFile('shampoo_sales.csv')
lista_dati = shampoofile.get_data()
print(lista_dati)
