#Trabajo Practico Integrador - Programación I - UTN
#Algoritmos de Búsqueda y Ordenamiento en Python
from colorama import init, Fore, Style
import time


# Búsqueda lineal: se recorre la lista comparando cada nombre
def buscar_producto(nombre_buscado, lista):
    for producto in lista:
        if producto["nombre"].lower() == nombre_buscado.lower():
            return producto
    return None


# Ordenamiento QuickSort por precio de menor a mayor
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x["precio"] <= pivote["precio"]]
        mayores = [x for x in lista[1:] if x["precio"] > pivote["precio"]]
        return quicksort(menores) + [pivote] + quicksort(mayores)

# Impremir diccionario
def imprimir_diccionario(diccionario):
    # Imprimir encabezado
    print(Fore.GREEN + "{:<15} {:>10}".format("Producto", "Precio") + Style.RESET_ALL)
    print(Fore.YELLOW +"-" * 26 + Style.RESET_ALL)
    # Imprimir productos
    for producto in diccionario:
        print(f"{producto['nombre']:<15} $ {producto['precio'] :>9.2f}")
    print("")


# Lista simulada de productos en forma de diccionario
productos = [
    {"nombre": "Auriculares", "precio": 100000},
    {"nombre": "Teclado", "precio": 25000},
    {"nombre": "Monitor", "precio": 200000},
    {"nombre": "Mouse", "precio": 10000},
    {"nombre": "Notebook", "precio": 700000}
]

# Validación: ejecutar funciones
print("Lista original:")
imprimir_diccionario(productos)

#Busqueda
nombre = input("Ingrese el artículo a buscar: ")
resultado = buscar_producto(nombre, productos)
print("Resultado de búsqueda: ")
if resultado:
    print(Fore.GREEN + "Producto encontrado:")
    print(f"Nombre: {resultado['nombre']}")
    print(f"Precio: ${resultado['precio']}"+ Style.RESET_ALL)
else:
    print(Fore.RED + "Producto no encontrado" + Style.RESET_ALL)

#Ordenamiento
print(Style.RESET_ALL +"\nLista ordenada por precio:")
productos_ordenados = quicksort(productos)
imprimir_diccionario(productos_ordenados)