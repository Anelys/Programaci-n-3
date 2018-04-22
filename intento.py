import os
import re 

class usuariosAdministrar (object):
    
    def validarPatron (self,campo):
        patron = '[a-z0-9][a-z0-9]'
        if re.match(patron,campo):
            return True
        else:
            msn = (input("Valor Invalido!"))
            return False
    
    def validarLogin (self, loginValidar):
        try:
                f = open('productos.txt','r')
        except FileNotFoundError:
            print ("--> ERROR!! No Existe Archivo de Usuarios")  
            return (False) 

        for linea in f.readlines():

            linea = linea.split(',')
            code = linea[0]
            description = linea [1]
            price = linea [2]
            itbm = linea [3]
            unit = linea [4]

            if (loginValidar == code):
                return (True)
        return (False)
        
    def ingresar (self):
        while True: 
            os.system('cls')
            print ("----------------------------------")
            print ("    Sistema de Ingreso de Codigo   ")
            print ("----------------------------------")
            print ( " ")

            code = ""
            description = ""
            price = ""
            itbm = 0
            unit = ""

            while True: 
                code = (input("Ingrese codigo de producto: "))
                i = code
                v = usuariosAdministrar()
                if (v.validarPatron(code) == True): 
                    if (v.validarLogin(code) == True):
                        x = (input("Este Codigo ya Existe <ENTER>"))
                    else: 
                        break
            f = open('productos.txt', 'a')
            f.write(i)
            description = (input("Descripcion del producto: " ))
            f.write(description)
            price = (input("Ingrese precio del producto: "))
            f.write(price)
            itbm = (input("Ingrese itbm del producto: "))
            f.write(itbm)
            unit = (input("Ingrese unidades del producto: "))
            f.write(unit)


            print (" ")
            opcion = (input("Datos Correctos ?"))
            if (opcion.lower() == "s"):
                    f = open ('productos.txt','a')
                    f.write(code + "," + description + "," + price + "," + itbm + "," + unit + "\n")
                    f.close()
                    opcion = (input("Datos Guardados Correctamente <ENTER>"))
        else: 
            x = input("Valor Invalido")

x = usuariosAdministrar()
print("Ingrese cantidad de productos ")
resp = int(input())
i = 0
os.system("cls")
while i != resp:
    x.ingresar()
    i += 1
    os.system("cls")