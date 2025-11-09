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

        [1] Engadir produto.
        [2] Eliminar produto.
        [3] Amosar lista.
        [4] Saír.
    ''')

    opcion = int(input("    [?] Opción: "))

    if opcion == 1:
        produto = input("    [?] Produto a engadir: ")
        listacompras.append(produto)
    elif opcion == 2:
        if len(listacompras) == 0:
            print("    [!] A lista está baleira.")
        else:
            produto = input("    [?] Produto a eliminar: ")
            listacompras.remove(produto)
    elif opcion == 3:
        if len(listacompras) == 0:
            print("    [!] A lista está baleira.")
        else:
            print("    [+] Lista de Compras: ")
            for num in range(len(listacompras)):
                print(f"         [{num + 1}] {listacompras[num]}.")
    elif opcion == 4:
            print("    [i] Saíndo do programa...")
            break
    else:
        print("    [!] Opción inválida.")