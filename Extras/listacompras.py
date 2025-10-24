'''
Lista de Compras
-Engadir produto
-Eliminar produto
-Amosar lista
-Saír
'''

listacompras = []

while True:
    print('''
========[ Lista de Compras ]========

        [1] Engadir produto
        [2] Eliminar produto
        [3] Amosar lista
        [4] Saír
    ''')

    opcion = int(input("    [?] Opción: "))

    if opcion == 1:
        produto = input("    [?] Produto a engadir: ")
        listacompras.append(produto)
    elif opcion == 2:
        produto = input("    [?] Produto a eliminar: ")
        listacompras.remove(produto)
    elif opcion == 3:
        print("    [+] Lista de Compras: ")
        for produto in listacompras:
            print(f"         [+] {produto}.")
    elif opcion == 4:
            print("    [i] Saíndo do programa...")
            break
    else:
        print("     [!] Opción inválida!")