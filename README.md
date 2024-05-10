# ALGORITMOS_2_Virginia_Diaz_Quilez

# ALGORITMOS_2_Virginia_Diaz_Quilez


## 2. Ejercicio de Recursividad: Cálculo del Factorial

### Descripción General
Este programa implementa una función que calcula el factorial de un número entero no negativo usando un enfoque recursivo. El factorial de un número \(n\), denotado como \(n!\), es el producto de todos los enteros positivos menores o iguales a \(n\). Por ejemplo, \(5! = 5 \times 4 \times 3 \times 2 \times 1 = 120\).

### Detalles de la Implementación

#### Función `factorial`
La función `factorial` es el núcleo de este programa, diseñada para calcular el factorial de un número mediante recursividad.

##### Parámetros
- **n**: Número entero no negativo al que se le calculará el factorial.

##### Devolución
- **int**: El factorial del número dado.

##### Lógica
- **Caso Base**: Cuando \(n\) es 0, la función retorna 1, ya que \(0! = 1\) por definición.
- **Paso Recursivo**: Si \(n\) es mayor que 0, la función se llama a sí misma con \(n-1\), multiplicando el resultado por \(n\). Este proceso se repite hasta que se alcanza el caso base.

#### Ejemplo de Funcionamiento
Para calcular \(5!\):
1. `factorial(5)` se llama a sí misma para calcular `factorial(4)`, y multiplica el resultado por 5.
2. `factorial(4)` se llama a sí misma para calcular `factorial(3)`, y multiplica el resultado por 4.
3. `factorial(3)` se llama a sí misma para calcular `factorial(2)`, y multiplica el resultado por 3.
4. `factorial(2)` se llama a sí misma para calcular `factorial(1)`, y multiplica el resultado por 2.
5. `factorial(1)` se llama a sí misma para calcular `factorial(0)`, y multiplica el resultado por 1.
6. `factorial(0)` retorna 1.
7. Remontando la cadena de llamadas, se multiplican los resultados sucesivos, obteniendo \(5 \times 4 \times 3 \times 2 \times 1 = 120\).

#### Función `main`
La función `main` sirve como punto de entrada al programa y está diseñada para realizar pruebas básicas de la función `factorial`. En este caso específico, prueba el cálculo de \(5!\). Imprime en consola el resultado de la prueba para facilitar la verificación y demostración de funcionalidad.

##### Ejecución de prueba
- **Test Case 1**: Verifica el factorial de 5.
  ```bash
  The factorial of 5 is: 120


## 3. Bubble Sort (Ordenamiento Burbuja)

### Descripción del Método
Bubble Sort, también conocido como ordenamiento burbuja, es un algoritmo de ordenación simple que funciona revisando repetidamente la lista que se necesita ordenar, comparando elementos adyacentes e intercambiándolos si están en el orden incorrecto. Este proceso se repite varias veces hasta que no se necesitan más intercambios, lo que significa que la lista está ordenada.

### Funcionamiento de Bubble Sort
El funcionamiento del Bubble Sort se basa en la comparación de pares de elementos adyacentes a lo largo de la lista, y si un par está en el orden incorrecto (el primero es mayor que el segundo), los elementos se intercambian. El proceso se repite para cada elemento de la lista, pasando repetidamente por la lista hasta que no se necesitan más intercambios, lo cual ocurre cuando la lista está completamente ordenada.

#### Pasos del Bubble Sort:
1. Comenzar en el primer elemento de la lista.
2. Comparar el elemento actual con el siguiente en la lista.
3. Si el elemento actual es mayor que el siguiente, intercambiarlos.
4. Moverse al siguiente par de elementos y repetir el proceso.
5. Al final de cada "pase" por la lista, el siguiente elemento más grande se habrá "burbujeado" a su posición correcta al final de la lista.
6. Repetir el proceso para toda la lista hasta que no se realicen más intercambios en un nuevo pase.


### Casos en los que es conveniente utilizar este método de ordenación
Bubble Sort es preferible en ciertos escenarios específicos debido a sus características únicas:
- **Listas pequeñas**: Para colecciones pequeñas, Bubble Sort puede ser rápido y eficiente en términos de tiempo de ejecución.
- **Colecciones casi ordenadas**: En listas que están casi ordenadas, Bubble Sort puede terminar en muy pocas pasadas, detectando rápidamente cuando la lista está ordenada.
- **Simplicidad y enseñanza**: Es ideal para fines educativos, ofreciendo una clara ilustración de cómo funciona la ordenación y el concepto de algoritmos.
- **Limitaciones de espacio**: Al ser un algoritmo de ordenación "in place", no requiere memoria adicional más allá del espacio de almacenamiento original, lo cual es beneficioso en entornos con restricciones de memoria.
- **Necesidad de estabilidad en la ordenación**: Su naturaleza estable lo hace adecuado para casos donde se debe preservar el orden relativo de registros equivalentes.
  

### Ejemplo Conceptual
Consideremos la siguiente lista de números para ordenar usando Bubble Sort:
- Lista inicial: [34, 7, 23, 32, 5]

#### Aplicación del Bubble Sort:
1. Primera pasada:
   - Compara 34 y 7, intercambia: [7, 34, 23, 32, 5]
   - Compara 34 y 23, intercambia: [7, 23, 34, 32, 5]
   - Compara 34 y 32, intercambia: [7, 23, 32, 34, 5]
   - Compara 34 y 5, intercambia: [7, 23, 32, 5, 34]
2. Segunda pasada:
   - Compara 7 y 23, no intercambia.
   - Compara 23 y 32, no intercambia.
   - Compara 32 y 5, intercambia: [7, 23, 5, 32, 34]
3. Tercera pasada:
   - Compara 7 y 23, no intercambia.
   - Compara 23 y 5, intercambia: [7, 5, 23, 32, 34]
4. Cuarta pasada:
   - Compara 7 y 5, intercambia: [5, 7, 23, 32, 34]

Después de estas pasadas, la lista queda completamente ordenada como [5, 7, 23, 32, 34], y no se necesitan más intercambios.

Este ejemplo muestra cómo Bubble Sort "burbujea" los elementos más grandes hacia el final de la lista paso a paso, asegurando que cada elemento se coloque en su posición correcta gradualmente.


## 4. Ejercicio Functools

### Uso de SimpleOperations con functools.partial

Este proyecto demuestra el uso de la clase `SimpleOperations` para aplicar descuentos y calcular impuestos, así como cómo `functools.partial` puede ser utilizado para crear versiones especializadas de estas funciones con argumentos preconfigurados.

#### SimpleOperations Clase

La clase `SimpleOperations` incluye métodos para aplicar descuentos y calcular impuestos en precios de productos. Cada método recibe el precio inicial y un porcentaje, y devuelve el precio modificado.

##### Métodos

- `apply_discount`: Aplica un descuento al precio original y retorna el nuevo precio.
- `calculate_tax`: Calcula y agrega un impuesto al precio original y retorna el nuevo precio.

#### Utilizando functools.partial

`functools.partial` se utiliza para crear funciones que tienen algunos de los parámetros necesarios ya preconfigurados. Esto es especialmente útil para operaciones que se realizarán con parámetros comunes en múltiples llamadas.

##### Configuración de las Funciones

Se crearon dos funciones especializadas con `functools.partial`:

- **twenty_percent_discount**: Función preconfigurada para aplicar un descuento del 20% a cualquier precio.
- **vat_tax**: Función preconfigurada para agregar un impuesto del 21% a cualquier precio.
