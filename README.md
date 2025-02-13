# Pruebas Unitarias

## 1. test_sumar_numeros.py

Este script contiene la función `suma_lista`, que suma todos los elementos de una lista, y un conjunto de pruebas unitarias utilizando el módulo `unittest` de Python.

### Descripción de la Prueba

La función `suma_lista` recorre una lista de números y acumula su suma. Las pruebas unitarias verifican los siguientes casos:
- **Lista vacía:** La suma debe ser 0.
- **Lista con números positivos:** Por ejemplo, `[1, 2, 3, 4]` debe sumar 10.
- **Lista con números negativos:** Por ejemplo, `[-1, -2, -3]` debe sumar -6.
- **Lista mixta:** Ejemplo, `[1, -1, 0]` debe dar 0.
- **Lista con números flotantes:** Se utiliza `assertAlmostEqual` para manejar posibles imprecisiones en la suma.

## Cómo Ejecutar las Pruebas

1. Abre una terminal y navega al directorio donde se encuentra el archivo de pruebas (por ejemplo, `test_sumar_numeros.py`).
2. Ejecuta el siguiente comando:

   ```bash
   python test_sumar_numeros.py
