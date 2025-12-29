# PokerGame

PokerGame es un proyecto en Python que implementa la lógica básica de un juego de póker, centrado en la representación de cartas, la evaluación de manos y la comparación entre jugadores siguiendo las reglas del Texas Hold’em.

El proyecto se enfoca en cómo funciona el póker a nivel interno, dejando de lado la interfaz o la interacción directa con el usuario.

---

## ¿Cómo funciona el proyecto?

1. Cada jugador dispone de cartas privadas.
2. Existen cartas comunes compartidas por todos los jugadores.
3. A partir de todas las cartas disponibles, se generan combinaciones posibles de 5 cartas.
4. Cada combinación se evalúa para determinar el tipo de mano que representa.
5. Se selecciona la mejor mano posible para cada jugador.
6. Las manos se comparan y se decide el ganador o un empate.

Toda la lógica de evaluación y comparación se realiza automáticamente.

---

## Estructura del proyecto

PokerGame/  
│  
├── src/  
│   ├── cards.py  
│   ├── game.py  
│   ├── helpers.py  
│   └── roles.py  
│  
├── tests/  
│  
└── README.md  

---

## Descripción de los archivos

### cards.py

Contiene la lógica principal del juego. Define la clase Card para representar una carta individual y la clase Hand para evaluar y comparar manos de póker según las reglas del juego.

### helpers.py

Incluye funciones auxiliares como el barajado de cartas, la generación de números aleatorios y la creación de combinaciones de cartas.

### game.py

Se encarga de la lógica principal de la partida. Calcula la mejor mano posible para cada jugador usando las cartas comunes y privadas, y determina el ganador.

### roles.py

Define la clase Player, que representa a un jugador y almacena sus cartas privadas.

---

## Tecnologías utilizadas

- Python 3
- Programación orientada a objetos
