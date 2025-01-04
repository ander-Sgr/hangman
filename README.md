
### **Estructura del Proyecto**
Un proyecto bien organizado te ayudará a gestionar el código de manera más eficiente. Aquí tienes una sugerencia de estructura:

```
hangman/
├── main.py               # Punto de entrada del programa
├── hangman/
│   ├── __init__.py       # Indica que es un módulo Python
│   ├── game.py           # Lógica principal del juego
│   ├── words.py          # Gestión de palabras (elegir palabra aleatoria)
│   ├── display.py        # Dibujo del ahorcado en consola
├── tests/
│   ├── __init__.py
│   ├── test_game.py      # Pruebas para la lógica del juego
│   ├── test_words.py     # Pruebas para la gestión de palabras
├── README.md             # Descripción del proyecto
└── requirements.txt      # Dependencias del proyecto (opcional)
```

---

### **Clases Necesarias**
1. **`Game`** (en `game.py`):
   - Maneja la lógica principal del juego.
   - Atributos:
     - `word`: La palabra a adivinar.
     - `guesses`: Letras adivinadas hasta el momento.
     - `attempts`: Intentos restantes.
   - Métodos:
     - `start()`: Inicia el juego y administra el flujo.
     - `guess(letter)`: Procesa una letra adivinada.
     - `is_won()`: Verifica si el usuario ha ganado.
     - `is_lost()`: Verifica si el usuario ha perdido.
     - `current_progress()`: Devuelve la palabra con guiones bajos para las letras no adivinadas.

2. **`WordManager`** (en `words.py`):
   - Se encarga de gestionar la lista de palabras.
   - Métodos:
     - `get_random_word()`: Devuelve una palabra aleatoria de una lista predefinida.

3. **`HangmanDisplay`** (en `display.py`):
   - Dibuja el ahorcado en la consola según los intentos restantes.
   - Métodos:
     - `draw(attempts_left)`: Imprime la figura correspondiente a los intentos restantes.

---

### **Flujo del Juego**
1. **Inicio:**
   - Se selecciona una palabra aleatoria y se informa al jugador de la longitud.
   - Ejemplo de output:
     ```
     Bienvenido al Juego del Ahorcado.
     La palabra tiene 5 letras: _ _ _ _ _
     Tienes 6 intentos. ¡Buena suerte!
     ```

2. **Turno del Jugador:**
   - El jugador introduce una letra.
   - Si la letra está en la palabra:
     ```
     ¡Correcto! La letra 'a' está en la palabra.
     Progreso: a _ _ _ a
     ```
   - Si la letra no está en la palabra:
     ```
     Lo siento, la letra 'x' no está en la palabra.
     Te quedan 5 intentos.
     ```

3. **Dibujo del Ahorcado:**
   - Después de cada intento fallido, se actualiza el dibujo del ahorcado.
     ```
      -----
      |   |
      O   |
     /|\  |
     /    |
          |
     ------
     ```

4. **Fin del Juego:**
   - Si el jugador gana:
     ```
     ¡Felicidades! Has adivinado la palabra: 'amigo'.
     ```
   - Si el jugador pierde:
     ```
     Lo siento, te has quedado sin intentos. La palabra era 'python'.
     ```

---

### **Extras**
1. **Dibujo del Ahorcado (en `display.py`):**
   - Crea una lista de estados del dibujo, desde un ahorcado vacío hasta el completo.
   - Muestra el estado correspondiente según los intentos restantes.

   Ejemplo de estados:
   - 6 intentos restantes:
     ```
      -----
      |   |
          |
          |
          |
          |
     ------
     ```
   - 0 intentos restantes:
     ```
      -----
      |   |
      O   |
     /|\  |
     / \  |
          |
     ------
     ```

2. **Soporte para palabras más complejas:**
   - Agregar un archivo externo (`words.txt`) para incluir palabras más diversas y seleccionarlas al azar.

---

### **Ejemplo de Input y Output**
**Input:**
```
Introduce una letra: a
```

**Output:**
```
¡Correcto! La letra 'a' está en la palabra.
Progreso: a _ _ _ a
```

---

### **Pasos Siguientes**
1. **Define la lógica principal en `game.py`.** 
   - Empieza con los métodos esenciales como `start()` y `guess()`.

2. **Crea una lista de palabras en `words.py`.** 
   - Puedes usar una lista fija o cargar palabras desde un archivo.

3. **Diseña los dibujos en `display.py`.**
   - Prueba diferentes estados con un contador de intentos.

4. **Escribe pruebas unitarias en `tests/`.**
   - Asegúrate de que cada método funcione correctamente.
