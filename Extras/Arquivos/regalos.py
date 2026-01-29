def saudo():
    print("Saudo")

def decorador (func):
    def envoltorio():
        print("Executa antes da función", func.__name__)
        func()
        print("Se executa despois da función", func.__name__)
    return envoltorio

print("-----")
def suma(var1,var2):
    return var1+var2

def decorador2(func):
    def envoltorio(*args):
        print("Ejecuta antes de la funcion", func.__name__)
        result = func(*args)
        print("Despues de la funcion", func.__name__)
        return result
    return envoltorio

print(decorador2(suma)(2,3))

@decorador2
def resta(var1,var2):
    return var1-var2
print(resta(2,3))