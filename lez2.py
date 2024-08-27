my_file = open('shampoo_sales.csv', 'r') 
for line in my_file:
    print(line) 
my_file.close()

mia_stringa = 'Ciao, come va?' 
lista_elementi = mia_stringa.split(',')

mia_stringa = '5.5'
mio_numero = float(mia_stringa)

mia_lista = [1,2,3] 
mia_lista.append(4)

# Inizializzo una lista vuota per salvare i valori
values = []
# Apro e leggo il file, linea per linea
my_file = open('shampoo_sales.csv', 'r') 
for line in my_file:
    # Faccio lo split di ogni riga sulla virgola
    elements = line.split(',')
    # Se NON sto processando l’intestazione...
    if elements[0] != 'Date':
        # Setto la data e il valore
        date  = elements[0]
        value = float(elements[1])
        
        # Aggiungo alla lista dei valori questo valore
        values.append(value)
print(values)