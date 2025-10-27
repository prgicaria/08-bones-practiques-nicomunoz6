#!/usr/bin/env python
'''Nom del programa. Descripció curta del programa
Institut Icària
Programació - 1r Batxillerat - Curs 2023-24
Descripció llarga del programa. Indicar que fa el
programa i el resultat esperat.
'''
__author__ = "One solo developer"
__authors__ = ["One developer", "And another one", "etc"]
__email__ = "mail@example.com"
__date__ = "YYYY/MM/DD"
Dividend = int(input("ingresar dividend"))
Divisor = int(input("ingresar divisor"))
Quocient = (Dividend)//(Divisor)
Residu = (Dividend) % (Divisor)
print(f"Divisió: {Dividend}/{Divisor}")
print(f"Quocient: {Quocient}")
print(f"Residu: {Residu}")
