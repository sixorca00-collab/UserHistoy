# --- FASE 1: ENTRADA DE DATOS ---
# Se piden los tres datos: nombre, precio y cantidad.
# 1. Solicitar nombre:
nombre = input("Ingresa el nombre del objeto: ").strip()# el Strip elimina los espacios
while nombre == "":
    print("El nombre no puede estar vacío.")
    nombre = input("Ingresa nuevamente el nombre del objeto: ").strip()

# 2. Solicitar precio (debe ser un número mayor a 0)
while True:
    try:
        precio = float(input("Ingresa el costo del objeto ($): "))
        if precio > 0:
            break
        else:
            print("El precio debe ser mayor que 0.")
    except ValueError:
        print("Debes ingresar un valor numérico válido para el precio.")

# 3. Solicitar cantidad (debe ser un número entero positivo)
while True:
    try:
        cantidad = int(input("Ingresa la cantidad del objeto: "))
        if cantidad > 0:
            break
        else:
            print("La cantidad debe ser un número mayor que 0.")
    except ValueError: #El try excep se hace para evitar mostrar la chorrera de codigo 
        #cuando se comete un error, solo mostrara lo del excep
        print("Debes ingresar un número entero válido para la cantidad.")

#FASE 2: PROCESAMIENTO 
#Se calcula el costo total multiplicando el precio por la cantidad.
costo_total = precio * cantidad

# FASE 3: SALIDA
#  Se muestran los resultados de manera clara y ordenada.
print("Los datos fueron registrados correctamente.")

print("RESUMEN DEL PRODUCTO")
print(f"Nombre: {nombre}")
print(f"Precio unitario: ${precio:.2f}")#.2f es para mostrar solo 2 decimales
print(f"Cantidad: {cantidad}")
print(f"Costo total del inventario: ${costo_total:.2f}")

# Este programa permite registrar un producto con su nombre, precio y cantidad.
# Valida los datos ingresados, calcula el costo total y muestra los resultados.
# Incluye control de errores y repite las preguntas hasta obtener valores válidos.

