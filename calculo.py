class Calculo:
    def __init__(self, num1:int, num2:int):
       self.num1 = num1
       self.num2 = num2

    def sumador(self):
        self.suma = self.num1 + self.num2

    def restador(self):
        self.resta = self.num1 - self.num2

    def multiplicador(self):
        self.multiplicacion = self.num1 * self.num2
    
    def divisor(self):
        self.division = self.num1 / self.num2


