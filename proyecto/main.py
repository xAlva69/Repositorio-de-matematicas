import eel
from sympy import*


eel.init('web')

@eel.expose
def main(funcion, variable_ind):
    x=Symbol('x')
    resultado_var1=eval(funcion)
    var1=limit(resultado_var1, x,variable_ind )
    print(var1)
    return var1

eel.start("main.html",size=(800, 600))