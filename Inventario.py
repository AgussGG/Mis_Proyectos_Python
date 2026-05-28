lista_productos = []
programa_activo = True
print("--- 🛠️ BIENVENIDO AL SISTEMA DE INVENTARIO ---")
while programa_activo == True:
    print("\n¿Qué deseas hacer?")
    print("1. Agregar producto")
    print("2. Ver inventario actual")
    print("3. Salir del programa")
    opcion = input("Selecciona una opción (1, 2 o 3): ")
    if opcion == "1":
        nuevo_producto = input("Escribe el nombre del producto: ")
        lista_productos.append(nuevo_producto) 
        print(f"✅ '{nuevo_producto}' ha sido agregado con éxito.")        
    elif opcion == "2":
        print("\n📦 --- INVENTARIO ACTUAL ---")
        # Si la lista está vacía
        if len(lista_productos) == 0:
            print("El inventario está completamente vacío.")
        else:
            for producto in lista_productos:
                print(f"- {producto}")
    elif opcion == "3":
        print("Cerrando el sistema... ¡Hasta luego!")
        programa_activo = False   
    else:
        print("❌ Opción no válida. Por favor, elige 1, 2 o 3.")
