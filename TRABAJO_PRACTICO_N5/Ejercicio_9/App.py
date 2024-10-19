from Producto import Producto 
from MonedaARG import MonedaARG
from MonedaEEUU import MonedaEEUU

# Crear un producto
producto = Producto("90000,50")
print(f"cuesta {producto.get_precio()}")

# En Arg
producto_arg = MonedaARG(producto)
print(f"cuesta {producto_arg.get_line_description() } {producto_arg.get_precio()}")

# En EUU
producto_usd = MonedaEEUU(producto)
print(f"cuesta {producto_usd.get_line_description() } {producto_usd.get_precio()}")