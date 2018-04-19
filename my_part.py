import re
import os

def crearArchivoProductos():
    arch = open('productos.txt', 'w')
    #arch.close()

def descriptions():
    arch = open('productos.txt','a')
    description = input("Ingrese Nombre de productos:")
    arch.write(description)
    arch.write("\n")

def codes():
    arch = open('productos.txt','a')
    code = input("Ingrese codigo del producto:")
    arch.write(code)
    arch.write("\n")
    if (validateCode(value) == True)
      text = (input("Este codigo ya existe"))
"""a+=1
    if a > 1:
        arch = open('productos.txt','r')
        lines = arch.readlines()
        for line in lines:
            if word in line:
                print (line)"""

def prices():
    arch = open('productos.txt','a')
    price = input("Ingrese precio del producto: ")
    arch.write(price)
    arch.write("\n")

def itbms():
    arch = open('productos.txt','a')
    itbm = input("Ingrese impuesto del producto: ")
    arch.write(itbm)
    arch.write("\n")

def units():
    arch = open('productos.txt','a')
    unit = input("Ingrese unidad del producto L o G: ")
    arch.write(unit)
    arch.write("\n")
    
def validateCode(self, validateCodes):
    try:
        f = open('productos.txt','r')
    except FileNotFoundError:
        print ("--> ERROR!! No Existe Archivo de Usuarios")  
        return (False) 

    for linea in f.readlines():

        linea = linea.split(',')
        code = linea[1]

        if (validateCodes == code):
            return (True)
    return (False)
 
if __name__ == "__main__":
    print ("Ingrese cantidad de productos ")
    resp = int(input())
    crearArchivoProductos()
    i = 0
    os.system("cls")
    while i != resp:
        descriptions()
        codes()
        prices()
        itbms()
        units()
        i += 1
        os.system("cls")
