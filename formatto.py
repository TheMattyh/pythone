# inizializzare una lista con i reciproci dei primi 10 interi naturali.
# stampare i float risultanti in modo da visualizzare 8 decimali

lista1 = list (range(1,11))
lista2 = [1 / x for x in lista1]
for x in lista2:
    print(f"valore: {x:10.8f}")
