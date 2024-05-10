# Este script implementa la función factorial de un número utilizando recursividad.

def factorial(n):
    """
    Calcula el factorial de un número dado de manera recursiva.
    
    Parámetros
    ----------
    n : int
        Número entero no negativo para calcular su factorial.
        
    Devoluciones
    -------
    int
        El factorial del número dado.
        
    Ejemplo
    -------
    factorial(5)
    Retorna 120
    
    Explicación
    -----------
    El caso base es cuando n es 0, retornando 1 porque por definición 0! = 1.
    Si n es mayor que 0, se calcula el factorial de n multiplicando n por el factorial de n-1.
    Esta llamada recursiva continúa reduciendo n hasta que n es 0.
    """
    # Caso base: si n es 0, se retorna 1 directamente, ya que 0! = 1 por definición.
    if n == 0:
        return 1
    # Paso recursivo: si n es mayor que 0, se calcula el factorial llamando a la función factorial con n-1.
    else:
        return n * factorial(n - 1)

def main():
    """
    Función principal que ejecuta la prueba del cálculo factorial.
    """
    # Imprime una línea de separación y el título del caso de prueba.
    print("=================================================================")
    print("Test Case 1: Check the Factorial of 5")
    print("=================================================================")
    # Calcula y muestra el resultado del factorial de 5.
    print("The factorial of 5 is: ", factorial(5))

# Este bloque verifica si el script se ejecuta como programa principal y llama a la función main.
if __name__ == "__main__":
    main()
