# Cajero automático simple en Python
# Este código simula un cajero automático donde el usuario puede consultar su saldo, retirar dinero y salir del sistema. El usuario debe ingresar un PIN correcto para acceder a las opciones del cajero.
# El saldo inicial es de 1500 y el PIN correcto es "3478". El usuario tiene un máximo de 3 intentos para ingresar el PIN correctamente antes de que la cuenta se bloquee.
saldo = 1500
pin_code = "3478"

#autenticación del usuario mediante PIN
#if el usuario ingresa el PIN correcto, se le da acceso a las opciones del cajero. Si el usuario ingresa un PIN incorrecto, se le informa y se le da un máximo de 3 intentos antes de bloquear la cuenta.
#cuando el usuario ingresa el PIN correcto, se le da la bienvenida y se le presentan las opciones del cajero.
autenticacion = False
for i in range(3):
    pin = input("Ingrese su PIN: ")
    if pin == pin_code:
        print("bienvenido samuel.")
        autenticacion = True
        break
#esta parte del código es la que se encarga de manejar los intentos de ingreso del PIN. Si el usuario ingresa un PIN incorrecto, se le informa cuántos intentos le quedan. Si el usuario agota los 3 intentos, se le informa que su cuenta ha sido bloqueada y se le indica que contacte al banco.    
#else, se le informa al usuario que el PIN ingresado es incorrecto y se le indica cuántos intentos le quedan.
#if el usuario agota los 3 intentos, se le informa que su cuenta ha sido bloqueada y se le indica que contacte al banco.    
    else:
        print("PIN incorrecto. Intentos restantes:", 2 - i)
        if i == 2:
            print("Se ha bloqueado la cuenta. Por favor, contacte al banco.")

#autennticacion se le da acceso a las opciones del cajero, donde puede consultar su saldo, retirar dinero o salir del sistema. Si el usuario selecciona una opción inválida, se le informa y se le pide que intente de nuevo.
if autenticacion:
        while True:
#seleccione una opcion del cajero, donde puede consultar su saldo, retirar dinero o salir del sistema. Si el usuario selecciona una opción inválida, se le informa y se le pide que intente de nuevo.
            print("\nSeleccione una opción:")
            print("1. Consultar saldo")
            print("2. Depositar dinero")
            print("3. Retirar dinero")
            print("4. Salir")
            opcion = input("Ingrese el número de la opción deseada: ")
#esta parte del código es la que se encarga de manejar las opciones del cajero. 
#si el usuario selecciona la opción 1, se le muestra su saldo actual.
            if opcion == "1":
                print("Su saldo actual es:", saldo)
#si el usuario selecciona la opción 2, se le pide que ingrese el monto a depositar y se actualiza su saldo.
            elif opcion == "2":
                monto = float(input("Ingrese el monto a depositar: "))
                saldo += monto
                print("Depósito exitoso. Su nuevo saldo es:", saldo)
#si el usuario selecciona la opción 3, se le pide que ingrese el monto a retirar. Si el monto ingresado es menor o igual al saldo disponible, se realiza el retiro y se actualiza el saldo. Si el monto ingresado es mayor al saldo disponible, se le informa al usuario que no tiene suficiente saldo para realizar el retiro.        
            elif opcion == "3":
                monto = float(input("Ingrese el monto a retirar: "))
                if monto <= saldo:
                    saldo -= monto
                    print("Retiro exitoso. Su nuevo saldo es:", saldo)
                else:
                    print("Saldo insuficiente.")
#si el usuario selecciona la opción 4, se le agradece por usar el cajero automático y se sale del sistema. Si el usuario selecciona una opción inválida, se le informa y se le pide que intente de nuevo.
            elif opcion == "4":
                print("Gracias por usar el cajero automático. ¡Hasta luego!")
                break
            else:
                print("Opción inválida. Por favor, intente de nuevo.")

    