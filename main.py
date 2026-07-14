class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")


def main():
    persona = Persona("Héctor", 20)
    persona.mostrar_datos()


if __name__ == "__main__":
    main()