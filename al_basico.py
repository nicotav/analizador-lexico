import re

# Definir los patrones de los tokens utilizando expresiones regulares
token_patterns = [
    ("NUMERO", r"\d+"),
    ("OPERADOR", r"[+\-*/]"),
    ("PARENTESIS", r"[()]"),
    ("ESPACIO", r"\s+"),
    ("IDENTIFICADOR", r"[a-zA-Z_][a-zA-Z0-9_]*"),
]


# Función para analizar la cadena de texto de entrada y producir los tokens
def analizador_lexico(cadena):
    tokens = []
    posicion = 0

    while posicion < len(cadena):
        coincidencia = None

        for nombre_token, patron in token_patterns:
            regex = re.compile(patron)
            coincidencia = regex.match(cadena, posicion)

            if coincidencia:
                valor = coincidencia.group(0)
                token = (nombre_token, valor)
                tokens.append(token)
                posicion = coincidencia.end(0)
                break

        if not coincidencia:
            print(f"Error: Carácter inválido en la posición {posicion}")
            break

    return tokens


# Ejemplo de uso
entrada = "3 + 4 * (2 - 1)"
tokens = analizador_lexico(entrada)

for token in tokens:
    print(token)
