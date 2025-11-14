# Aquí se almacenarán todos los productos del inventario.
# Cada producto será un diccionario con nombre, precio y cantidad.
inventario = []


#  FUNCIÓN 1: Agregar producto.
def agregar_producto():
    "Agrega un nuevo producto al inventario."
    print(" Agregar producto ")

    # Se pide el nombre del producto 
    nombre = input("Ingrese el nombre del producto: ")

    # Se validan los valores numéricos con try/except para evitar errores
    try:
        precio = int(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad disponible: "))
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")
        return  # Si hay error, se sale de la función

    # Crear un diccionario con la información del producto
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    # Agregar el producto a la lista inventario
    inventario.append(producto)
    print(f"Producto '{nombre}' agregado correctamente.")


# FUNCIÓN 2: Mostrar inventario 
def mostrar_inventario():
    """Muestra todos los productos guardados en el inventario."""
    print(" Mostrar inventario ")

    # Validar si hay productos
    if not inventario:
        print("El inventario está vacío.")
        return

    # Recorrer la lista e imprimir cada producto
    for producto in inventario:
        print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
    print("-----------------------------")
    print(f"Total de productos registrados: {len(inventario)}")#len para contar cuantas cosas hay en el diccionario


# FUNCIÓN 3: Calcular estadísticas 
def calcular_estadisticas():
    "Calcula y muestra estadísticas básicas del inventario."
    print("\n--- Calcular estadísticas ---")

    # Validar si hay productos en la lista
    if not inventario:
        print("No hay productos para calcular estadísticas.")
        return

    # Calcular valor total (precio × cantidad) de todos los productos
    valor_total = 0
    cantidad_total = 0

    # Recorremos cada producto con un bucle for
    for producto in inventario:
        valor_total += producto["precio"] * producto["cantidad"]
        cantidad_total += producto["cantidad"]

    # Mostrar resultados
    print(f"Valor total del inventario: ${valor_total}")
    print(f"Cantidad total de unidades: {cantidad_total}")
    print(f"Número de productos diferentes: {len(inventario)}")


#  FUNCIÓN PRINCIPAL: Menú del sistema 
def menu():
    """Muestra el menú principal y controla el flujo del programa."""
    while True:  # El menú se repite hasta que el usuario elija salir
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadísticas")
        print("4. Salir")
        print("==========================")

        # Validar que la opción ingresada sea numérica
        try:
            opcion = int(input("Elija una opción (1-4): "))
        except ValueError:
            print("Opción inválida. Ingrese un número del 1 al 4.")
            continue  # Regresa al menú sin cerrar el programa

        # CONTROL DE FLUJO 
        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            mostrar_inventario()
        elif opcion == 3:
            calcular_estadisticas()
        elif opcion == 4:
            print("Saliendo del programa...")
            break  # Sale del bucle while y finaliza el programa
        else:
            print("Opción no válida. Intente de nuevo.")


menu()

# Este programa permite gestionar un inventario usando estructuras de control,
# bucles y colecciones en Python (listas y diccionarios).
# Cumple con el objetivo de la semana al aplicar lógica de programación y control de flujo.
