import functools

class SimpleOperations:
    def apply_discount(self, price, discount):
        """
        Aplica un descuento al precio dado y retorna el nuevo precio.
        
        Args:
            price (float): El precio original del producto.
            discount (float): El porcentaje de descuento aplicado, representado como decimal 
                              (ej. 0.10 para un 10% de descuento).
        
        Returns:
            float: El precio final después de aplicar el descuento.
        """
        return price * (1 - discount)

    def calculate_tax(self, price, tax_rate):
        """
        Calcula y agrega el impuesto al precio dado y retorna el precio final.
        
        Args:
            price (float): El precio original del producto.
            tax_rate (float): El porcentaje de impuesto a aplicar, representado como decimal 
                              (ej. 0.21 para un impuesto del 21%).
        
        Returns:
            float: El precio final después de agregar el impuesto.
        """
        return price * (1 + tax_rate)

# Crear una instancia de SimpleOperations
operations = SimpleOperations()

# Configurar funciones con descuentos y tasas de impuestos predefinidos utilizando functools.partial.
# Creando una función que aplica un descuento del 20%
twenty_percent_discount = functools.partial(operations.apply_discount, discount=0.20)

# Creando una función que aplica un impuesto del valor agregado (IVA) del 21%
vat_tax = functools.partial(operations.calculate_tax, tax_rate=0.21)

# Ejemplo de uso de las funciones preconfiguradas
price_before_discount = 150  # Precio original antes del descuento
price_after_discount = twenty_percent_discount(price=price_before_discount)
print(f"El precio después de aplicar un descuento del 20% sobre {price_before_discount} es {price_after_discount}")

price_before_tax = 150  # Precio antes de impuestos
price_after_tax = vat_tax(price=price_before_tax)
print(f"El precio después de agregar un 21% de IVA sobre {price_before_tax} es {price_after_tax}")
