
# Creati o functie care primeste doua argumente de tip int (a, b, c) si returneaza o functie capabile sa
# calculeze ax^2-2bx+c (a^2 = a la puterea 2). Pentru setul de valorile a = 1, b = 3, c = 5 dati valori functiei
# returnate in intervalul -10, 10. Printati valoarea lui x pentru care functiia returneaza un minim

rezultate= []

def ecuatie(a,b,c):
    minim = 9999
    for x in range(-10, 11):
        rezolvare = a*x**2 - 2*b*x + c
        rezultate.append(rezolvare)
        if minim > rezolvare:
            minim = rezolvare
            val_x = x

    return val_x

def returnare(a,b,c):
    return ecuatie(a,b,c)

print('valoarea lui x este:', returnare(1,3,5))