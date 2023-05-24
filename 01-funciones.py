def miFuncion(nombre, apellido="Feliz"):  # nombre -> parametro
    print("Hola mundo")
    print("Ultimate Python")
    print("Bievenido", nombre, apellido)


miFuncion("Alex")  # "Alex" -> argumento
miFuncion("Alex", "Silva")

# def miFuncion(nombre, apellido="Feliz"):
# El parámetro apellido es un argumento OPCIONAL, de esta manera,
# si no le pasamos ningun argumento al llamar la función,
# este parámetro va a tomar el valor por defecto, en este caso "feliz"

miFuncion(apellido="Silva", nombre="Alejandro")
