#Imprime las opciones y retorna la opcion seleccionada
def main_menu():
    menu = [
        "Agregar producto",
        "Remover producto",
        "Listar productos",
        "Salir"
        ]
    print("Seleccione una opcion")
    for i, option in enumerate(menu):
        print(f"{i+1}) {option}")
    return input()

#Solicita nombre y cantidad del producto, agregandolos al diccionario 
#o agregando la cantidad si este ya existe
def add_product(inventory):
    product = input("Ingrese el nombre del producto: ")
    ammount = int(input("Ingrese las unidades del producto: "))
    #Se asume que el usuario siempre ingresara un int
    if product in inventory.keys:
        print(list(inventory.keys()))
        ammount+=inventory[product]
    inventory.update(product = ammount)

#Solicita nombre del producto y, si existe, lo elimina del diccionario
def del_product(inventory):
    product = input("Ingrese el nombre del producto: ")
    if product in inventory:
        inventory.pop(product)
    else:
        print("el producto seleccionado no existe")

#Imprime el diccionario
def print_dict(inventory):
    for product in inventory:
        print(f"""Nombre: {product} 
            cantidad: {inventory.get(product)} 
            """)

#Main
inventory = {}
while True:
    choice = main_menu()
    match choice:
        case "1":
            add_product(inventory)
        case "2":
            del_product(inventory)
        case "3":
            print_dict(inventory)
        case "4":
            exit()
        case _:
            print("Ingrese una opcion valida")
    
