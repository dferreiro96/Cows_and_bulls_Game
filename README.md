# Cows and Bulls / Vacas y Toros

A Python CLI game where the computer generates a random 4-digit number and the player tries to guess it.

Un juego de línea de comandos en Python donde la computadora genera un número aleatorio de 4 dígitos y el jugador intenta adivinarlo.

## How to Play / Cómo Jugar

- The program generates a random 4-digit number (no repeated digits) / El programa genera un número aleatorio de 4 dígitos (sin dígitos repetidos)
- The player tries to guess it / El jugador intenta adivinarlo
- **Cow (vaca)**: a digit that is in the number but in the wrong position / **Vaca**: un dígito que está en el número pero en la posición incorrecta
- **Bull (toro)**: a digit that is in the number and in the correct position / **Toro**: un dígito que está en el número y en la posición correcta
- The player wins when they get 4 bulls / El jugador gana cuando obtiene 4 toros

## Features / Funcionalidades

- Random 4-digit number generation with `random.sample()` / Generación de número aleatorio de 4 dígitos con `random.sample()`
- No repeated digits in the secret number / Sin dígitos repetidos en el número secreto
- Input validation with `try/except` / Validación de entrada con `try/except`
- Validation that the guess is a 4-digit number without repeated digits / Validación de que el intento sea de 4 dígitos sin repetidos
- Attempt counter / Contador de intentos
- Option to play again / Opción de jugar de nuevo
- Displays cows and bulls for each guess / Muestra vacas y toros en cada intento

## Requirements / Requisitos

- Python 3

## What I Learned / Lo que Aprendí

- Generating unique digits with random.sample() / Generar dígitos únicos con random.sample()

- Extracting digits from a number with // and % / Extraer dígitos de un número con // y %

- Comparing digits by position (bulls) and presence (cows) / Comparar dígitos por posición (toros) y presencia (vacas)

- Validating user input with try/except / Validar entradas del usuario con try/except

- Using nested while loops for game logic / Usar bucles while anidados para la lógica del juego

- Using flags to control the game loop / Usar banderas para controlar el bucle del juego

## Author / Autor

[dferreiro96]

## How to Run / Cómo Ejecutar

```bash
python cows_and_bulls.py