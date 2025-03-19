import random

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
# Selecciona las 3 preguntas y se agregan en una lista de tuplas
selected_questions = random.sample(list(zip(questions,answers,correct_answers_index)), k=3)
score = 0
# El usuario deberá contestar 3 preguntas
for asked_question, answer_list, correct_answer in selected_questions:
    # Se selecciona una pregunta aleatoria

    # Se muestra la pregunta y las respuestas posibles
    print(asked_question)
    for i, answer in enumerate(answer_list):
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = (input("Respuesta: "))
        # Se verifica si la respuesta es númerica
        if not user_answer.isdigit():
            print("Respuesta no válida")
            exit(1)
        # En caso de ser númerica se convierte a int
        user_answer = int(user_answer)
        # Se verifica si la respuesta está en rango
        if  user_answer > 4 or user_answer < 1:
            print("Respuesta no válida")
            exit(1)
        # Se verifica si la respuesta es correcta y se suma puntuacion si lo es
        if user_answer - 1 == correct_answer:
            print("¡Correcto!")
            score = score + 1
            break
        # En caso de ser incorrecta se deducen puntos
        else:
            score = score - 0.5
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(answer_list[correct_answer])

    # Se imprime un blanco al final de la pregunta
    print()
print("Puntuación:",score)
