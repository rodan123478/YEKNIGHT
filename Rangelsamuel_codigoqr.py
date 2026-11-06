import qrcode

contenido_qr = input("ingresa el contenido para generar el código QR: ")

nombre_archivo = input("ingresa el nombre del archivo para guardar el código QR (sin extensión): ")

img = qrcode.make(contenido_qr)

img.save(nombre_archivo + ".png")

print("QR code generado y guardado como ", nombre_archivo + ".png")