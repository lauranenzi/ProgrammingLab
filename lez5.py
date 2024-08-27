my_var = 'ciao'

try:
    my_var = float(my_var)
    
except TypeError:
    print('Non posso convertire "my_vart" a valore numerico')
    print('Ho avuto un errore di TIPO. "m_var" vale "{}"'.format(my_var))

except ValueError:
    print('Non posso convertire "my_vart" a valore numerico')
    print('Ho avuto un errore di VALORE. "m_var" vale "{}"'.format(my_var))

except Exception as e:
    print('Non posso convertire "my_vart" a valore numerico')
    print('Ho avuto questo errore generico: "{}"'.format(e))



