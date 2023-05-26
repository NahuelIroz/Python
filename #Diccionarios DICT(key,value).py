#Diccionarios DICT(key,value)
# #En este ejemlo el diccionario es NOMBRES

nombres={
    'primerNombre':'Nahuel', #primerNombre es la KEY y Nahuel es el VALUE
    'segundoNombre':'Lucas',
    'apellido':'Iroz'
}
print(nombres)

#largo del diccionario
print(len(nombres))

#acceder a un elemnto, hay que indicar la KEY
print(nombres['primerNombre']) #primerNombre es la KEY

#Recupermos un elemento con GET
print(nombres.get('segundoNombre'))

#Modificar elementos
nombres['primerNombre']='nahuel' #entre corchetes va la llave a modificar, y del lado dereho el nuevo valor
print(nombres)

#Recorrer elemnto de un diccionario
for i in nombres.keys(): #recupera unicamente la llave sin el valor asociado
     print(i)

#recuperamos la llave con el valor asociado
for v in nombres.values():
    print(v)

#comprobar existencia de un elemento en el diccionario
print('primerNombre' in nombres) #pregunta si la llave primerNombre existe en el dicconario nombres, de ser asi devuelve TRUE

#Agregar un elemnto al diccionario
nombres['apodo']='Nahue'
print(nombres)

#Eliminar un elemento (Hay que especificar la llave)
nombres.pop('apodo')
print(nombres)

#limpiar el diccionario con CLEAR
nombres.clear()
print(nombres)

#Eliminar el diccionario con DEL
del nombres
print(nombres)