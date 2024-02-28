class Persona:
    def __init__(self, nombre, anios):
        self.anios = anios
        self.nombre = nombre

    def imprimir(self):
        print(self.nombre, "tiene", self.anios, "anios")

    def cumpleanios(self):
        self.anios += 1
        self.imprimir()

if __name__ == "__main__":
    obama = Persona("Obama", 62)
    obama.imprimir()
    obama.cumpleanios()

    