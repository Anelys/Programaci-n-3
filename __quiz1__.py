class figura(object):
    base = 0
    altura = 0
    def __init__(self, fgeometrica):
            self.fgeometrica = fgeometrica
    def formula(self):
        if self.fgeometrica == 'triangulo':
            print("El valor del area del Triangulo Rectangulo es:")
            return self.base * self.altura / 2
        print("El valor del area del Rectangulo es:")
        return self.base * self.altura

class TrianguloRectangulo(figura):
    base = 4
    altura = 2
    def tipo_figura(self):
        return 'triangulo'   
    
class Rectangulos(figura):
    base = 5
    altura = 3
    def tipo_figura(self):
        return 'rectangulo'

if __name__ == "__main__":
    imp = TrianguloRectangulo("triangulo")
    print(imp.formula())
    impr = Rectangulos("cuadrado")
    print(impr.formula())
    
