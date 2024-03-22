import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo", "inteligencia"]

# Función para obtener la palabra parcialmente adivinada según el nivel de dificultad
def get_partial_word(secret_word, level, guessed_letters):
    if level == "facil":
        # Mostrar todas las vocales por defecto
        return "".join([letter if letter in guessed_letters or letter in "aeiou" else "_" for letter in secret_word])
    elif level == "medio":
        # Mostrar la primera y la última letra de la palabra
        revealed_letters = set([secret_word[0], secret_word[-1]]) & set(guessed_letters)
        #return "".join([letter if letter in guessed_letters or letter in revealed_letters else "_" for letter in secret_word])
        return "".join([letter if letter in guessed_letters or letter in revealed_letters or index == 0 or index == len(secret_word)-1 else "_" for index, letter in enumerate(secret_word)])
    else:
        # Mostrar todas las letras adivinadas hasta el momento
        return "".join([letter if letter in guessed_letters else "_" for letter in secret_word])

# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de fallos permitidos
max_failures = 5
# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")
print("Selecciona el nivel de dificultad: fácil, medio o difícil")
level = input("Nivel: ").lower()

# Verificar si el nivel seleccionado es válido
if level not in ["facil", "medio", "dificil"]:
    print("Nivel de dificultad no válido. Seleccionando nivel fácil por defecto.")
    level = "facil"

print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
# Mostrar la palabra parcialmente adivinada según el nivel seleccionado
word_displayed = get_partial_word(secret_word, level, guessed_letters)
print(f"Palabra: {word_displayed}")

failures = 0  # Contador de fallos

while failures < max_failures:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()

    if not letter:
        print("No has ingresado ninguna letra. Por favor, intenta nuevamente.")
        continue

    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue

    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)
    
    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
       print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        failures += 1  # Incrementar el contador de fallos
   
    # Mostrar la palabra parcialmente adivinada
    word_displayed = get_partial_word(secret_word, level, guessed_letters)
    print(f"Palabra: {word_displayed}")
    
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"¡Oh no! Has alcanzado el número máximo de fallos ({max_failures}).")
    print(f"La palabra secreta era: {secret_word}")