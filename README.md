# Analizador Léxico en Python

Este es un ejemplo de un analizador léxico básico implementado en Python. El analizador léxico toma una cadena de texto de entrada y la divide en tokens, que son unidades significativas como palabras clave, identificadores, operadores, símbolos, etc.

## Uso

1. Asegúrate de tener instalado Python en tu sistema.
2. Descarga o clona este repositorio en tu máquina local.
3. Abre el archivo `analizador_lexico.py` en tu editor de código favorito.
4. Modifica el archivo según tus necesidades. Puedes agregar, eliminar o modificar los patrones de tokens en la lista `token_patterns` para adaptarlos a tu lenguaje o requisitos específicos.
5. Guarda los cambios en el archivo `analizador_lexico.py`.
6. Abre una terminal y navega hasta el directorio donde se encuentra el archivo `analizador_lexico.py`.
7. Ejecuta el siguiente comando para iniciar el analizador léxico:

```bash
python analizador_lexico.py
```
8. Se te solicitará ingresar una cadena de texto de entrada. Ingresa una cadena y presiona Enter.
9. El analizador léxico procesará la cadena de texto de entrada y mostrará los tokens generados en la consola.



# Ejemplo
Supongamos que ingresamos la siguiente cadena de texto de entrada: 

> 3 + 4 * (2 - 1)

El analizador léxico generará los siguientes tokens:


- ('NUMERO', '3')
- ('ESPACIO', ' ')
- ('OPERADOR', '+')
- ('ESPACIO', ' ')
- ('NUMERO', '4')
- ('ESPACIO', ' ')
- ('OPERADOR', '*')
- ('ESPACIO', ' ')
- ('PARENTESIS', '(')
- ('NUMERO', '2')
- ('ESPACIO', ' ')
- ('OPERADOR', '-')
- ('ESPACIO', ' ')
- ('NUMERO', '1')
- ('PARENTESIS', ')')
