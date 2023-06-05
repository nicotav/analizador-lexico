import re

# Definición de los patrones de tokens
token_patterns = [
    ("ID", r"[a-zA-Z_][a-zA-Z0-9_]*"),  # Identificadores
    ("NUM", r"\d+(\.\d+)?"),  # Números
    ("OP", r"[+\-*/=<>!]+"),  # Operadores
    ("RPARENT", r"[)}]"),  # Paréntesis
    ("LPARENT", r"[({]"),  # Paréntesis
    ("KEYWORD", r"if|else|while|for"),  # Palabras clave
    ("SPACE", r"\s+"),  # Espacios en blanco (ignorados)
    ("SEMICOLON", r";"),  # Punto y coma
    ("ERROR", r"."),  # Otros caracteres (error)
]


# Función para analizar la cadena de entrada y generar los tokens
def lexer(input_string):
    tokens = []
    position = 0

    while position < len(input_string):
        match = None

        for token_name, pattern in token_patterns:
            regex = re.compile(pattern)
            match = regex.match(input_string, position)

            if match:
                value = match.group(0)
                if token_name != "SPACE":
                    tokens.append((token_name, value))
                break

        if not match:
            print(f"Error: Caracter no válido en la posición {position}")
            break

        position = match.end()

    return tokens


# Ejemplo de uso
input_string = "if (x > 5) { y = x + 2; }"
tokens = lexer(input_string)

for token in tokens:
    print(token)
