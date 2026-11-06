print("Bienvenido al sistema de evaluación de ingenierías")
print("Claves válidas:")
print("1. Ingeniería Civil: 7.5")
print("2. Ingeniería Mecánica: 8.0")
print("3. Ingeniería Eléctrica: 8.5")
print("4. Ingeniería en Sistemas: 7.0")

# datos que se solicitan :V
clave = int(input("Ingrese la clave de la carrera (1-4): "))
edad = int(input("Ingrese su edad: "))
promedio = float(input("Ingrese su promedio: "))

# Claves osease las carreras,las edades y los promedios que se necesitan para ser aceptado en cada carrera
if clave >= 1 and clave <= 4:
    # Validar edad
    if edad >= 17:
        # el promedio que se usa para ser aceptado es el que se pone en la clave de la carrera
        if clave == 1:  # ingeniería Civil
            if promedio >= 7.5:
                print("Aceptado en Ingeniería Civil")
            else:
                print("Rechazado por promedio insuficiente para Civil ijoles pa la proxima")
        elif clave == 2:  # ingeniería Mecánica
            if promedio >= 8.0:
                print("Aceptado en Ingeniería Mecánica")
            else:
                print("Rechazado: promedio insuficiente para Mecánica")
        elif clave == 3:  # ingeniería Eléctrica
            if promedio >= 8.5:
                print("Aceptado en Ingeniería Eléctrica")
            else:
                print("Rechazado: promedio insuficiente para Eléctrica")
        elif clave == 4:  # ingeniería en Sistemas
            if promedio >= 7.0:
                print("Estas Aceptado carnal en Ingeniería en Sistemas GGs Felicidades")
            else:
                print("Rechazado: promedio insuficiente para Sistemas")
    else:
        print("Rechazado: edad mínima requerida es 17 años")
else:
    print("Error: clave inválida. Debe ser 1, 2, 3 o 4")
#esto es importante ya que no usa decimal ejemplo 7.5 si no 75 la verdad no entiendo porque
