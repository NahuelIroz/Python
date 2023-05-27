#se definen con DEF [NOMBRE DE FUNCION]
def miFuncion():
    print('Esto es una funcion en PYTHON')

miFuncion()

#Pasamos parámetros
def funcion1(nombre,apellido):
    print(nombre,apellido)

funcion1('Nahuel','Iroz')

#suma
def suma(a,b):
    c=a+b
    print('La suma de ambos números es: ',c)
a=int(input('Ingrese el primer valor: '))
b=int(input('Ingrese el segundo valor: '))
suma(a,b)

#otra forma de hacer la suma es con la palabra reservada RETURN
def suma2(n1,n2):
    return(n1+n2)
n1=int(input('Ingrese el primer valor: '))
n2=int(input('Ingrese el segundo valor: '))

resultado=suma2(n1,n2)
print(resultado)

#recursion
def factorial(n):
    if (n==1):
        return(n)
    else:
        return (n*factorial(n-1))
n=int(input('Ingrese un número para calcular el factorial: '))
print('El factorial de ',n,' es ',factorial(n) )
