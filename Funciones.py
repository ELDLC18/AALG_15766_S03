def resta(a,b):
    return a-b

def multiplicacion(a:int,b:int) -> int:
    return a*b

def saludo(a:str) -> str:
    x = "Hola " + a
    return x

def despedida(a:str) -> None:
    x = "Chao " + a
    print(x)

print (resta(5,2))
print (multiplicacion(5,2))
print (saludo("Carlos"))
despedida("Carlos")

#####

c = 5
d : int = 2

print(resta(c,d))
print(multiplicacion(c,d))
print(saludo("Carlos"))
despedida("Carlos")