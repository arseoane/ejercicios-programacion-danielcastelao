''' 4. Escribir un programa que almacene as asignaturas dun curso (por exemplo Matemáticas, Física, Química, Historia e Língua) nunha lista,
 pregunte o usuario a nota que sacou en cada asignatura e elimine da lista as asignaturas aprobadas.
 O fin, o programa debe mostrar por pantalla as asignaturas que o usuario ten que repetir.'''

asignaturas = ["matemáticas", "física", "química", "historia", "lingua"]
notas = []

for asignatura in asignaturas:
    notas.append(int(input(f"[?] Nota de {asignatura}: ")))

for asignatura, nota in zip(asignaturas, notas):
    if nota > 5:
        notas.remove(nota)
        asignaturas.remove(asignatura)
    else:
        print(f"[-] Tes que repetir {asignatura}, xa que sacaches un {nota}.")
