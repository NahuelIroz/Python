#set
dias={'lunes','martes','miercoles','jueves','viernes','sábado'} #SET es una colección
print(dias)

#calculamos el largo de la colección con LEN
print(len(dias))

#revisar si el elementomestá en la colección, si está devuelve TRUE
print('lunes' in dias)

#Agregaos un elemento con el metodo ADD
dias.add('domingo')#Agregamos DOMINGO A LA COLECCION
print(dias)

#Vamos a eliminar el elemento DOMINGO con REMOVE (tia un error si el elemento no está)
dias.remove('domingo')
print(dias)

#Vamos a eliminar domingo con DISCARD
dias.discard('domingo')
print(dias)

#limpiar el SET con CLEAR
dias.clear()
print(dias)

#Eliminar el set por completo con DEL
del dias