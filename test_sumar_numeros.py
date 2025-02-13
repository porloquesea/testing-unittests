import unittest  # Importamos el módulo unittest, que nos permite crear y ejecutar pruebas unitarias.


# ESTA ES LA FUNCION PARA LA QUE VAMOS A ESCRIBIR PRUEBAS UNITARIAS.

def suma_lista(numeros):
    """
    Función que recibe una lista de números y devuelve su suma.

    Parámetros:
        numeros (list): Lista de números (enteros o flotantes).

    Retorna:
        int o float: La suma de todos los elementos de la lista.
    """
    total = 0  # Inicializamos la variable 'total' en 0.
    for numero in numeros:  # Iteramos sobre cada elemento 'numero' en la lista 'numeros'.
        total += numero  # Sumamos el valor de 'numero' a 'total'.
    return total  # Devolvemos el valor acumulado en 'total'.


# A CONTINUACIÓN VAMOS A ESCRIBIR LAS PRUEBAS UNITARIAS PARA LA FUNCIÓN 'suma_lista'.

# Creamos una clase de pruebas que hereda de unittest.TestCase.
class TestSumaLista(unittest.TestCase):
    def test_lista_vacia(self):
        # Probamos que la suma de una lista vacía sea 0.
        entrada = []
        resultado_esperado = 0
        salida = suma_lista(entrada)
        # Comprobamos el resultado esperado con la salida obtenida.
        self.assertEqual(salida, resultado_esperado)

    def test_lista_positiva(self):
        # Probamos que la suma de [1, 2, 3, 4] sea 10.
        entrada = [1, 2, 3, 4]
        resultado_esperado = 10
        salida = suma_lista(entrada)
        # Comprobamos el resultado esperado con la salida obtenida.
        self.assertEqual(salida, resultado_esperado)

    def test_lista_negativos(self):
        # Probamos que la suma de [-1, -2, -3] sea -6.
        entrada = [-1, -2, -3]
        resultado_esperado = -6
        salida = suma_lista(entrada)
        # Comprobamos el resultado esperado con la salida obtenida.
        self.assertEqual(salida, resultado_esperado)

    def test_lista_mixta(self):
        # Probamos que la suma de una lista mixta [1, -1, 0] sea 0.
        entrada = [1, -1, 0]
        resultado_esperado = 0
        salida = suma_lista(entrada)
        # Comprobamos el resultado esperado con la salida obtenida.
        self.assertEqual(salida, resultado_esperado)

    def test_lista_flotantes(self):  # Los numeros flotantes son aquellos que tienen decimales.
        # Probamos que la suma de [1.5, 2.5, -1.0] sea 3.0.
        # Usamos assertAlmostEqual para comparar números flotantes debido a posibles imprecisiones.
        entrada = [1.5, 2.5, -1.0]
        resultado_esperado = 3.0
        salida = suma_lista(entrada)
        # Comprobamos el resultado esperado con la salida obtenida.
        self.assertAlmostEqual(salida, resultado_esperado)


# Este bloque se ejecuta solo si el script se corre directamente.
if __name__ == '__main__':
    unittest.main()  # Ejecuta todos los métodos de prueba definidos en la clase TestSumaLista.
