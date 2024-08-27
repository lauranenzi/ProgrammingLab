print('Hello world!')

#tipi di dati
my_var = 1  # Esempio di variabile tipo intero
my_var = 1.1  # Esempio di variabile tipo floating point
my_var = 'ciao'  # Esempio di variabile tipo stringa
my_var = True  # Esempio di variabile tipo booleano
my_var = None  # Il “niente” si rappresenta con il “None”
print('Valore 1: {}, valore 2: {}'.format(my_var, my_var))

mia_stringa = "cebrkriulfvewruyfqveiurgcqeliubcloeiuvroueivcruqyevruyvueyvcruoeyvcrueyvcruyevcryuvaerucvekurcveuyivrcueysvcreuyovliuqwveliuv  ehqwiluegcuioew ciuehcgua eciuegrciuegrciugqe"
mia_stringa[2]  # Terzo carattere della stringa
mia_stringa[-1]  # Penultimo carattere della stringa
mia_stringa[0:50]  # Dal primo al cinquantesimo carattere
mia_stringa[30:50]  # Dal trentunesimo al cinquantesimo carattere
mia_stringa[0:-1]  # Dal primo al penultimo carattere

my_list = [1, 2, 3]  # Lista di numeri
my_list = ['Marco', 'irene', 'paolo']  # Lista di stringhe

my_dict = {'Trieste': 34100, 'Padova': 35100}  # stringa -> numero
my_dict = {34100: 'Trieste', 35100: 'Padova'}  # numero -> stringa
my_dict = {'Trieste': 'TS', 'Padova': 'PD'}  # stringa -> stringa
print('CAP di Trieste: {}'.format(my_dict['Trieste']))

for item in my_list:
    print(item)

for i in range(10):
    print(i)

for i, item in enumerate(my_list):
    print("Posizione {}: {}".format(i, item))

def mia_funzione(argomento1, argomento2):
    print("Argomenti: {} e {}".format(argomento1, argomento2))

mia_funzione("Pippo","Pluto")

def eleva_al_quadrato(numero): 
    return numero*numero

eleva_al_quadrato(4)

risultato = eleva_al_quadrato(4) 
print('Risultato: {}'.format(risultato))