#2. Escribir un programa que converta un valor dado en grados Fahrenheit a grados Celsius. Recordade que a fórmula para a conversión é: F = 9/5 * C + 32.

fahrenheit = int(input("Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print("Celsius: ", celsius)
