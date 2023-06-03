#Funciones para testearlas
def sum(x,y):
    return x + y

def is_greater_than(number_1, number_2):
    return number_1 > number_2

def login(username, password):
    if ((username == "bas-clavijo") and (password == "123456")):
        return True
    else:
        return False

#para ejecutar las pruebas se debe de ingresar en la consola pytest
#pytest -v: muestra mas informacion sobre las pruebas 