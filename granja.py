import pygame
import random

class Animal:
    def __init__(self, nombre, raza, edad, peso, salud, estado_animo, energia, hambre):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.salud = salud
        self.estado_animo = estado_animo
        self.energia = energia
        self.hambre = hambre

    def reproducir_sonido(self, sonido):
        pygame.mixer.music.load(sonido)
        pygame.mixer.music.play()

    def comer(self):
        self.hambre -= 10
        self.peso += 2
        self.energia += 10
        if self.hambre < 0:
            self.hambre = 0
        self.hacer_sonido()  
        print(f"{self.nombre} está comiendo.")

    def beber(self):
        self.energia += 5
        self.hacer_sonido()  
        print(f"{self.nombre} está bebiendo.")

    def dormir(self):
        self.energia += 20
        print(f"{self.nombre} está durmiendo.")

    def reproducir(self, otro_animal):
        if type(self) == type(otro_animal):
            if self.energia > 50 and otro_animal.energia > 50:
                self.hacer_sonido()  
                print(f"{self.nombre} y {otro_animal.nombre} se han reproducido.")
            else:
                print(f"{self.nombre} o {otro_animal.nombre} no tienen suficiente energía para reproducirse.")
        else:
            print("No pueden reproducirse, son de diferentes especies.")

    def enfermar(self):
        if random.random() > 0.8:  # 20% de probabilidad de enfermar
            self.salud = "mala"
            print(f"{self.nombre} ha enfermado.")

    def tratar(self):
        if self.salud != "excelente":
            self.salud = "buena"
            self.hacer_sonido()  
            print(f"{self.nombre} ha sido tratado y su salud ha mejorado.")

    def hacer_sonido(self):
        pass

    def recolectar_producto(self):
        pass

class Vaca(Animal):
    def hacer_sonido(self):
        self.reproducir_sonido('vaca.mp3')  
        print(f"{self.nombre} está mugiendo.")

    def recolectar_producto(self):
        return random.randint(1, 5)  # Litros de leche

class Gallina(Animal):
    def hacer_sonido(self):
        self.reproducir_sonido('gallina.mp3')  
        print(f"{self.nombre} está cacareando.")

    def recolectar_producto(self):
        return random.randint(1, 3)  # Huevos

class Oveja(Animal):
    def hacer_sonido(self):
        self.reproducir_sonido('oveja.mp3')  
        print(f"{self.nombre} está balando.")

    def recolectar_producto(self):
        return random.randint(1, 2)  # Unidades de lana

class Caballo(Animal):
    def hacer_sonido(self):
        self.reproducir_sonido('caballo.mp3')  
        print(f"{self.nombre} está relinchando.")

class Cerdo(Animal):
    def hacer_sonido(self):
        self.reproducir_sonido('cerdo.mp3') 
        print(f"{self.nombre} está gruñendo.")

class Granja:
    def __init__(self):
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def mostrar_informacion(self):
        for animal in self.animales:
            print(f"Nombre: {animal.nombre}, Salud: {animal.salud}, Energía: {animal.energia}, Hambre: {animal.hambre}")

def mostrar_menu():
    print("\n--- Menú de la Granja ---")
    print("1. Alimentar un animal")
    print("2. Beber agua")
    print("3. Dormir")
    print("4. Recolectar productos")
    print("5. Reproducir animales")
    print("6. Tratar enfermedades")
    print("7. Mostrar información de los animales")
    print("8. Salir")

def seleccionar_animal(granja):
    print("Selecciona un animal:")
    for idx, animal in enumerate(granja.animales):
        print(f"{idx + 1}. {animal.nombre} ({type(animal).__name__})")
    seleccion = int(input("Número del animal: ")) - 1
    if 0 <= seleccion < len(granja.animales):
        return granja.animales[seleccion]
    else:
        print("Selección inválida.")
        return None

def ejecutar_granja():
    pygame.mixer.init()
    granja = Granja()
    
    # Inicializa algunos animales
    vaca = Vaca("Lola", "Jersey", 4, 500, "buena", "feliz", 52, 10)
    gallina = Gallina("Clara", "Leghorn", 2, 1.5, "excelente", "feliz", 32, 0)
    oveja = Oveja("Dolly", "Merino", 3, 70, "regular", "nerviosa", 42, 15)
    caballo = Caballo("Spirit", "Mustang", 5, 600, "excelente", "feliz", 50, 10)
    cerdo = Cerdo("Porky", "Yorkshire", 3, 120, "buena", "feliz", 35, 20)
    
    granja.agregar_animal(vaca)
    granja.agregar_animal(gallina)
    granja.agregar_animal(oveja)
    granja.agregar_animal(caballo)
    granja.agregar_animal(cerdo)
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            animal = seleccionar_animal(granja)
            if animal:
                animal.comer()
        elif opcion == "2":
            animal = seleccionar_animal(granja)
            if animal:
                animal.beber()
        elif opcion == "3":
            animal = seleccionar_animal(granja)
            if animal:
                animal.dormir()
        elif opcion == "4":
            animal = seleccionar_animal(granja)
            if animal:
                print(f"Producto recolectado: {animal.recolectar_producto()}")
        elif opcion == "5":
            animal1 = seleccionar_animal(granja)
            animal2 = seleccionar_animal(granja)
            if animal1 and animal2:
                animal1.reproducir(animal2)
        elif opcion == "6":
            animal = seleccionar_animal(granja)
            if animal:
                animal.tratar()
        elif opcion == "7":
            granja.mostrar_informacion()
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    ejecutar_granja()
