from sympy import*


def calcular_limite_numerico():
    x=Symbol('x')
    var1=input("Ingrese la funcion numerica que quiere calcular Ejemplo: x**2-x+2: ")
    resultado_var1=eval(var1)
    var2=float(input("ingrese al que tiende x: "))
    print(limit(resultado_var1, x, var2))
    return var1

def calcular_limite_infinito():
    x=Symbol('x')
    var3=input("Ingrese la funcion numerica que quiere calcular Ejemplo: x**2-x+2: ")
    resultado_var3=eval(var3)
    var4=("ingrese si quiere evaluar la funcion por izquierda'-' o por derecha '+' ")
    if var4=='-':
        print(limit(resultado_var3, x, oo,'-'))
    else:
        print(limit(resultado_var3, x, oo,'+'))
    return var3

while True:
    print("Menú:")
    print("1. Calcular límite numérico")
    print("2. Calcular límite infinito")
    print("3. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        calcular_limite_numerico()
    elif opcion == "2":
        calcular_limite_infinito()
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, elige una opción válida.")
