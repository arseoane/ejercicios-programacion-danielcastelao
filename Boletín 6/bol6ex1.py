''' 1. Escribir un programa que almacene as asignaturas dun curso (por exemplo Matemáticas, Física, Química, Historia e Língua)
nunha lista, pregunte o usuario a nota que sacou en cada asignatura, e despois as mostre por pantalla co mensaxe
En <asignatura> sacaches <nota> onde <asignatura> é cada unha das asignaturas da lista e <nota> cada unha das correspondentes notas introducidas polo usuario.
'''

asignaturas = ["matemáticas", "física", "química", "historia", "lingua"]
notas = []
i = 0

for asignatura in asignaturas:
    notas.append(int(input(f"[?] Nota de {asignatura}: ")))

print("\n")
for nota in notas:
    print(f"[+] En {asignaturas[i]} sacaches un {nota}.")
    i += 1
