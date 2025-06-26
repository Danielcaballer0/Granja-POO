# 🐄 Simulador de Granja POO

Un simulador de granja desarrollado en Python que implementa los principios de la Programación Orientada a Objetos (POO). Este proyecto permite gestionar una granja virtual con diferentes tipos de animales, cada uno con sus características y comportamientos únicos.

## Descripción

El simulador modela una granja completa donde puedes:
- Gestionar diferentes tipos de animales
- Alimentar y cuidar a los animales
- Recolectar productos (leche, huevos, lana)
- Reproducir animales
- Tratar enfermedades
- Escuchar los sonidos característicos de cada animal

## 🐾 Animales Disponibles

| Animal | Producto | Sonido | Características |
|--------|----------|---------|-----------------|
| 🐄 **Vaca** | Leche (1-5 litros) | Mugido | Animales grandes productores de leche |
| 🐔 **Gallina** | Huevos (1-3 unidades) | Cacareo | Aves ponedoras |
| 🐑 **Oveja** | Lana (1-2 unidades) | Balido | Productoras de lana |
| 🐎 **Caballo** | Transporte | Relincho | Animales de monta |
| 🐷 **Cerdo** | Carne | Gruñido | Animales de engorde |

## Características POO Implementadas

### Abstracción
- Clase base `Animal` que define la estructura común
- Métodos abstractos implementados por cada especie

### Herencia
- Todas las especies heredan de la clase `Animal`
- Cada animal implementa sus comportamientos específicos

###  Polimorfismo
- Método `hacer_sonido()` implementado de forma diferente en cada animal
- Método `recolectar_producto()` específico para cada especie

###  Encapsulamiento
- Atributos privados protegidos dentro de las clases
- Métodos públicos para interactuar con los objetos

##  Funcionalidades

### Acciones Básicas
- **Alimentar**: Reduce el hambre, aumenta peso y energía
- **Beber**: Incrementa la energía del animal
- **Dormir**: Restaura significativamente la energía
- **Reproducir**: Permite la reproducción entre animales de la misma especie

### Gestión de Salud
- **Sistema de enfermedades**: Los animales pueden enfermar aleatoriamente
- **Tratamiento médico**: Posibilidad de curar y mejorar la salud
- **Estados de salud**: Excelente, Buena, Regular, Mala

### Recolección
- **Productos específicos**: Cada animal produce diferentes recursos
- **Cantidad variable**: La producción varía aleatoriamente

## 🎵 Características de Audio

El simulador incluye efectos de sonido para cada animal. Asegúrate de tener los siguientes archivos de audio en el directorio del proyecto:

- `vaca.mp3`
- `gallina.mp3`
- `oveja.mp3`
- `caballo.mp3`
- `cerdo.mp3`

## 🛠️ Requisitos del Sistema

### Dependencias
```bash
pip install pygame
```

### Requisitos
- Python 3.6 o superior
- pygame (para efectos de sonido)
- Archivos de audio (.mp3) para cada animal

## 🚀 Instalación y Uso

1. **Clona el repositorio**
```bash
git clone https://github.com/Danielcaballer0/Granja-POO.git
cd Granja-POO
```

2. **Instala las dependencias**
```bash
pip install pygame
```

3. **Agrega los archivos de audio**
Coloca los archivos de sonido (.mp3) en el directorio principal del proyecto.

4. **Ejecuta el simulador**
```bash
python granja.py
```

## 🎮 Cómo Jugar

1. **Inicia el programa** y verás el menú principal
2. **Selecciona una opción** del 1 al 8
3. **Elige un animal** de la lista cuando sea necesario
4. **Observa los cambios** en los atributos del animal
5. **Escucha los sonidos** característicos de cada especie

### Menú de Opciones
```
1. Alimentar un animal
2. Beber agua
3. Dormir
4. Recolectar productos
5. Reproducir animales
6. Tratar enfermedades
7. Mostrar información de los animales
8. Salir
```

##  Estructura del Código

```
granja.py
├── Clase Animal (Base)
│   ├── Atributos comunes
│   ├── Métodos básicos
│   └── Métodos abstractos
├── Clases Específicas
│   ├── Vaca
│   ├── Gallina
│   ├── Oveja
│   ├── Caballo
│   └── Cerdo
├── Clase Granja
│   ├── Gestión de animales
│   └── Operaciones de la granja
└── Interfaz de Usuario
    ├── Menú interactivo
    └── Selección de animales
```

##  Atributos de los Animales

Cada animal tiene los siguientes atributos:

- **Nombre**: Identificador único
- **Raza**: Tipo específico del animal
- **Edad**: Años del animal
- **Peso**: Peso en kilogramos
- **Salud**: Estado de salud (excelente/buena/regular/mala)
- **Estado de ánimo**: Emocional (feliz/triste/nervioso)
- **Energía**: Nivel de energía (0-100)
- **Hambre**: Nivel de hambre (0-100)

## 🔮 Futuras Mejoras

- [ ] Interfaz gráfica con pygame
- [ ] Sistema de clima que afecte a los animales
- [ ] Economía de la granja (compra/venta)
- [ ] Más tipos de animales
- [ ] Sistema de experiencia y niveles
- [ ] Guardado y carga de partidas
- [ ] Interacciones entre diferentes especies
- [ ] Ciclos de vida más complejos

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request


## 👥 Autores

- Daniel Caballero - [@Mi usuario](https://github.com/Danielcaballer0)
