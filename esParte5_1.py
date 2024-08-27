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
                    date = elements[0]
                    value = elements[1].strip()
                    my_list.append([date, value])
            my_file.close()
            return my_list

        except FileNotFoundError:
            print('Errore: il file non esiste')


shampoofile = CSVFile('shampoo_saless.csv')
lista_dati = shampoofile.get_data()
print(lista_dati)
