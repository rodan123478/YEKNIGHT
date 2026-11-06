import pygame
import random
import time

# Inicialización
pygame.init()
ventana = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Caballero Dorado y el Rubí Escarlata")
clock = pygame.time.Clock()

# Cargar fondos
fondos = []
for i in range(1, 11):
    fondo = pygame.image.load(f"fondo{i}.png")
    fondo = pygame.transform.scale(fondo, (1200, 800))
    fondos.append(fondo)

# Personaje
personaje_img = pygame.image.load("personaje2.png")
personaje_img = pygame.transform.scale(personaje_img, (80, 80))
personaje_img_left = pygame.transform.flip(personaje_img, True, False)

personaje_rect = personaje_img.get_rect()
personaje_rect.topleft = (400, 400)
direccion = "right"

# Rubí
rubi_img = pygame.image.load("rubi.png")
rubi_img = pygame.transform.scale(rubi_img, (60, 60))
rubi_rect = rubi_img.get_rect()
rubi_rect.topleft = (600, 400)

# Variables de control
habitacion = 1
habitacion_rubi = random.randint(2, 10)
rubi_visible = False
mensaje = ""

# Vida del caballero
vida = 100
vida_max = 100

# Fuente
fuente = pygame.font.SysFont("Arial", 36)

# Función para dibujar barra de vida
def dibujar_barra_vida(superficie, x, y, vida, vida_max):
    ancho = 300
    alto = 25
    relleno = int((vida / vida_max) * ancho)
    borde = pygame.Rect(x, y, ancho, alto)
    barra = pygame.Rect(x, y, relleno, alto)
    pygame.draw.rect(superficie, (255, 0, 0), barra)     # Rojo = vida
    pygame.draw.rect(superficie, (255, 255, 255), borde, 2)  # Borde blanco

# Enemigos en el fondo8 (castillo de duendes)
enemigos_iniciales = [
    {"pos": (200, 200)},
    {"pos": (400, 300)},
    {"pos": (600, 400)},
    {"pos": (800, 500)},
    {"pos": (1000, 600)}
]

def crear_enemigos():
    return [{"rect": pygame.Rect(pos[0], pos[1], 60, 60), "ultimo_ataque": 0} for pos in [e["pos"] for e in enemigos_iniciales]]

enemigos_por_habitacion = {8: crear_enemigos()}

# Velocidad de enemigos
velocidad_enemigo = 3

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Guardar posición anterior
    pos_anterior = personaje_rect.copy()

    # Movimiento del caballero
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
        personaje_rect.x -= 7
        direccion = "left"
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        personaje_rect.x += 7
        direccion = "right"
    if teclas[pygame.K_UP] or teclas[pygame.K_w]:
        personaje_rect.y -= 7
    if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
        personaje_rect.y += 7

    # Movimiento y ataque de enemigos (solo en fondo8)
    if habitacion in enemigos_por_habitacion:
        for enemigo in enemigos_por_habitacion[habitacion]:
            # Movimiento hacia el jugador
            if enemigo["rect"].x < personaje_rect.x:
                enemigo["rect"].x += velocidad_enemigo
            elif enemigo["rect"].x > personaje_rect.x:
                enemigo["rect"].x -= velocidad_enemigo

            if enemigo["rect"].y < personaje_rect.y:
                enemigo["rect"].y += velocidad_enemigo
            elif enemigo["rect"].y > personaje_rect.y:
                enemigo["rect"].y -= velocidad_enemigo

            # Ataque con recarga de 3 segundos
            if personaje_rect.colliderect(enemigo["rect"]):
                tiempo_actual = time.time()
                if tiempo_actual - enemigo["ultimo_ataque"] >= 3:
                    vida -= 7
                    enemigo["ultimo_ataque"] = tiempo_actual
                    if vida < 0:
                        vida = 0
                        mensaje = "¡Has sido derrotado!"

    # Cambio de habitación
    if personaje_rect.x < 0 or personaje_rect.x > 1200 or personaje_rect.y < 0 or personaje_rect.y > 800:
        nueva_habitacion = random.randint(1, 10)
        while nueva_habitacion == habitacion:
            nueva_habitacion = random.randint(1, 10)
        habitacion = nueva_habitacion

        personaje_rect.topleft = (400, 400)
        mensaje = ""
        rubi_visible = (habitacion == habitacion_rubi)

        # Reiniciar enemigos al volver a fondo8
        if habitacion == 8:
            enemigos_por_habitacion[8] = crear_enemigos()

    # Colisión con rubí
    if rubi_visible and personaje_rect.colliderect(rubi_rect):
        mensaje = "¡Felicidades! Has encontrado el rubí."
        rubi_visible = False

    # Dibujar escena
    ventana.blit(fondos[habitacion - 1], (0, 0))

    # Dibujar personaje
    if direccion == "right":
        ventana.blit(personaje_img, personaje_rect)
    else:
        ventana.blit(personaje_img_left, personaje_rect)

    # Dibujar rubí
    if rubi_visible:
        ventana.blit(rubi_img, rubi_rect)

    # Dibujar enemigos (solo si estamos en fondo8)
    if habitacion in enemigos_por_habitacion:
        for enemigo in enemigos_por_habitacion[habitacion]:
            pygame.draw.rect(ventana, (0, 200, 0), enemigo["rect"])  # Verde = duende

    # Dibujar barra de vida
    dibujar_barra_vida(ventana, 20, 20, vida, vida_max)

    # Mensaje
    if mensaje != "":
        sombra = fuente.render(mensaje, True, (0, 0, 0))
        ventana.blit(sombra, (402, 102))
        texto = fuente.render(mensaje, True, (255, 255, 0))
        ventana.blit(texto, (400, 100))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
