import re
import os

class usuariosCodigo (object):
    def crearArchivoProductos(self):
        f = open('productos.txt', 'w')
        # arch.close()

    def validateCode(self, validateCodes):
        try:
            f = open('productos.txt', 'r')
        except FileNotFoundError:
            print("--> ERROR!! No Existe Archivo de Usuarios")
            return (False)

        for linea in f.readlines():

            linea = linea.split(',')
            description = linea [0]
            code = linea[1]
            price = linea [2]
            itbm = linea [3]
            unit = linea [4]

            if (validateCodes == code):
                return (True)
            return (False)

    def descriptions(self):
        f = open('productos.txt', 'a')
        description = input("Ingrese Nombre de productos:")
        f.write(description)
        f.write("\n")

    def codes(self):
        f = open('productos.txt', 'a')
        code = input("Ingrese codigo del producto:")
        f.write(code)
        f.write("\n")
        validate = usuariosCodigo()
        if (validate.validateCode(code) == True):
            print ("Este codigo ya existe <ENTER>")


    def prices(self):
        f = open('productos.txt', 'a')
        price = input("Ingrese precio del producto: ")
        f.write(price)
        f.write("\n")


    def itbms(self):
        f = open('productos.txt', 'a')
        itbm = input("Ingrese impuesto del producto: ")
        f.write(itbm)
        f.write("\n")


    def units(self):
        f = open('productos.txt', 'a')
        unit = input("Ingrese unidad del producto L o G: ")
        f.write(unit)
        f.write("\n")   

x = usuariosCodigo()
print("Ingrese cantidad de productos ")
resp = int(input())
x.crearArchivoProductos()
i = 0
os.system("cls")
while i != resp:
    x.descriptions()
    x.codes()
    x.prices()
    x.itbms()
    x.units
    i += 1
    os.system("cls")
