import random  # Librería para seleccionar un alumno al azar

# Lista de alumnos
alumnos = [
    "ALVARADO RAMIREZ BRYAN MANUEL",
    "CANIZALES PALAFOX ALAN SAMUEL",
    "CHACON VILLEGAS ULISES GAMALIEL",
    "CORONA PACHECO BENJAMIN",
    "DELGADO QUIÑONEZ DANIEL",
    "FLORES MARCOS DANIEL",
    "GARCIA MENDOZA CARLOS EDUAN",
    "GONZALEZ SAUCEDO DIEGO IVAN",
    "GUILLEN VAZQUEZ ANGEL DE JESUS",
    "GUILLEN VAZQUEZ IRIS GUADALUPE",
    "HIGUERA GONZALES BRANDON ELIAS",
    "LARIOS RINCON FERNANDO ALEXIS",
    "LEMUS MARTINEZ FERNANDO DE JESUS",
    "LUCEMA ANGULO LUNA LIZETH",
    "MARQUEZ LIZARRAGA RENE",
    "MATA SALAZAR NELLY JHOANA",
    "MENDOZA ROMAY JOSE RICARDO",
    "MOLLINEDO GAMEZ EVER",
    "MONDRAGON ESCOBAR ANGEL",
    "MONZON DE LEON JOSE IGNACIO",
    "NAVARRO AVILA CHRISTIAN GAEL",
    "PASILLAS LIZARRAGA GERMAN",
    "PEREZ MORALES DANIEL JEREMIAS",
    "RANGEL PEREZ SAMUEL",
    "RODRIGUEZ CONTRERAS ANGELA JOSELINE",
    "RODRIGUEZ CONTRERAS JESHUA FERNANDO",
    "RUEDA GIL JOSE IVAN",
    "SANTOS MONTIEL MAGDIEL IVAN",
    "SOTO RUBIO LUIS ALBERTO",
    "VELAZQUEZ FLORES NIMSI JEHIELI",
]

# Lista vacía para los alumnos que ya pasaron
alumnos_pasados = []

# Bucle while que se ejecuta mientras haya alumnos en la lista
#len() se usa para contar cuántos alumnos quedan en la lista de alumnos después de que uno ha sido seleccionado y eliminado
#random.randint() se usa para generar un número aleatorio que se usará como índice para seleccionar un alumno de la lista
#pop() se usa para eliminar al alumno seleccionado de la lista de alumnos y devolverlo como resultado
#append() se usa para agregar el alumno seleccionado a la lista de alumnos que ya pasaron
#\n se usa para agregar una línea en blanco entre los mensajes de salida
while len(alumnos) > 0:
    # Generar un índice aleatorio para seleccionar un alumno y le le da el valor a la variable alumno_actual
    indice = random.randint(0, len(alumnos) - 1)
    
    # Sacar al alumno con pop (lo elimina y lo devuelve)
    alumno_actual = alumnos.pop(indice)
    
    # Mostrar el alumno que va a participar
    print("EL QUE VA A PARTICIPAR ES:", alumno_actual)
    
    # Guardar al alumno en la lista de pasados
    alumnos_pasados.append(alumno_actual)

# Cuando ya no queden alumnos
print("\nYA NO QUEDAN ALUMNOS POR PARTICIPAR.")
print("ALUMNOS QUE YA PASARON:", alumnos_pasados)
