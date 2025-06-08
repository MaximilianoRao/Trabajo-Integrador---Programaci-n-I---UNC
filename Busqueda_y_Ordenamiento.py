#Trabajo Practico Integrador - Programación I - UTN
#Algoritmos de Búsqueda y Ordenamiento en Python
from colorama import Fore, Style


# Búsqueda lineal: se recorre la lista comparando cada nombre de producto
def buscar_producto(nombre_buscado, lista):
    for producto in lista:
        # Convierte ambos nombres a minúsculas para comparar sin importar mayúsculas/minúsculas
        # Si hay coincidencia, se retorna el producto
        if producto["nombre"].lower() == nombre_buscado.lower():
            return producto
    # Si no se encuentra el producto, se retorna None
    return None


# Ordenamiento QuickSort por precio de menor a mayor
def quicksort(lista):
    # Caso base: si la lista tiene un solo elemento o está vacía, ya está ordenada
    if len(lista) <= 1:
        return lista
    else:
        # Toma el primer elemento como pivote
        pivote = lista[0]
        # Lista con los elementos cuyo precio es menor o igual al del pivote
        menores = [x for x in lista[1:] if x["precio"] <= pivote["precio"]]
        # Lista con los elementos cuyo precio es mayor al del pivote
        mayores = [x for x in lista[1:] if x["precio"] > pivote["precio"]]
        # Aplicar QuickSort de forma recursiva y combinar los resultados
        return quicksort(menores) + [pivote] + quicksort(mayores)

# Imprimir lista de diccionarios
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

# Validación:
print("Lista original:")
imprimir_diccionario(productos)


#Búsqueda
nombre = input("Ingrese el artículo a buscar: ")
resultado = buscar_producto(nombre, productos)
print("Resultado de búsqueda: ")
if resultado:
    print(Fore.GREEN + "Producto encontrado: "+ Style.RESET_ALL)
    imprimir_diccionario([resultado])
else:
    print(Fore.RED + "Producto no encontrado" + Style.RESET_ALL)

#Ordenamiento
print(Style.RESET_ALL +"\nLista ordenada por precio:")
productos_ordenados = quicksort(productos)
imprimir_diccionario(productos_ordenados)