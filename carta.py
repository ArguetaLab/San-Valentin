import pygame
from PIL import Image

# Configuración de la pantalla
WIDTH, HEIGHT = 900, 700
BACKGROUND_COLOR = (250, 220, 230)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Para ti mailob")
clock = pygame.time.Clock()

# Fuentes de los textos
font = pygame.font.Font("Feeling Lovely.ttf", 25)
font2 = pygame.font.Font(None, 30)
font_response = pygame.font.Font(None, 35)  # Fuente predeterminada para la respuesta

# Coordenadas de la imagen del GIF y la imagen del hamster
gif_pos_x, gif_pos_y = 300, 50
gif_no_pos_x, gif_no_pos_y = 250, 100
gif_yes_pos_x, gif_yes_pos_y = 250, 100
# Cargar el GIF usando Pillow
gif_pregunta = Image.open('gato.gif')
# Cargar imagen del hamster
gif_no = pygame.image.load('hamster.jpg')
gif_yes = pygame.image.load('gatito.jpg')

answer = None
running = True

pygame.mixer.music.load("musiquita .wav")
pygame.mixer.music.play(-1)  # Reproducir en bucle

#pygame.mixer.music.load("hamster.wav")

# Mensaje
feelings = [
    "Desde hace mucho tiempo llevo sintiendo algo por ti",
    "es por eso que quiero preguntarte. Quieres ser mi San valentin",
    "?"
]
text = font.render(feelings[0], True, (57, 61, 73))
text2 = font.render(feelings[1], True, (57, 61, 73))
text3 = font2.render(feelings[2], True, (57, 61, 73))
text_rect = text.get_rect(center=(450, 350))
text_rect2 = text2.get_rect(center=(450, 400))
text_rect3 = text3.get_rect(center=(755, 400))

# Respuestas
responses = {
    "yes": "Yeii! sabía que me aceptarías",
    "no": "pipipi :("
}

response_text = {key: font_response.render(value, True, (57, 61, 73)) for key, value in responses.items()}
response_rect = {
    "yes": response_text["yes"].get_rect(center=(450, 550)),
    "no": response_text["no"].get_rect(center=(450, 500))
}

# Crear una lista con los cuadros del GIF
frames = []
try:
    while True:
        frames.append(pygame.image.fromstring(gif_pregunta.tobytes(), gif_pregunta.size, gif_pregunta.mode))
        gif_pregunta.seek(gif_pregunta.tell() + 1)
except EOFError:
    pass

# Variables para la animación
frames = frames[2:]  # Evitar los primeros cuadros si son estáticos
frame_count = len(frames)
frame_index = 0

# Coordenadas de la imagen del GIF y la imagen "No"
gif_pos_x, gif_pos_y = 300, 50
gif_no_pos_x, gif_no_pos_y = 250, 100

# Crear los botones de "Sí" y "No"
button_width, button_height = 150, 50
yes_button = pygame.Rect(250, 500, button_width, button_height)  # Botón Sí
no_button = pygame.Rect(500, 500, button_width, button_height)   # Botón No

# Colores de los botones
button_color_yes = (0, 143, 57)
button_color_no = (254, 0, 0)

while running:
    screen.fill(BACKGROUND_COLOR)

    if answer is None:
        screen.blit(frames[frame_index], (gif_pos_x, gif_pos_y))  # Usar coordenadas directamente
        frame_index = (frame_index + 1) % frame_count  # Avanzar en la animación

        screen.blit(text, text_rect)
        screen.blit(text2, text_rect2)
        screen.blit(text3, text_rect3)

        pygame.draw.rect(screen, button_color_yes, yes_button)
        pygame.draw.rect(screen, button_color_no, no_button)

        # Texto en los botones
        yes_text = font2.render("Sí", True, (255, 255, 255))
        no_text = font2.render("No", True, (255, 255, 255))
        yes_text_rect = yes_text.get_rect(center=yes_button.center)
        no_text_rect = no_text.get_rect(center=no_button.center)
        screen.blit(yes_text, yes_text_rect)
        screen.blit(no_text, no_text_rect)

    elif answer == responses["yes"]:
        screen.blit(gif_yes, (gif_yes_pos_x, gif_yes_pos_y))
    # Mostrar GIF animado si aún no han respondido o si la respuesta es "Sí"
    elif answer == responses["no"]:
        screen.blit(gif_no, (gif_no_pos_x, gif_no_pos_y))  # Usar coordenadas directamente
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and answer is None:
            if yes_button.collidepoint(event.pos):
                answer = responses["yes"]
            elif no_button.collidepoint(event.pos):
                answer = responses["no"]

    # Mostrar la respuesta si el usuario hizo clic en un botón
    if answer:
        screen.blit(response_text["yes" if answer == responses["yes"] else "no"],
                    response_rect["yes" if answer == responses["yes"] else "no"])

    pygame.display.flip()
    clock.tick(15)  # Controla la velocidad de la animación

pygame.quit()
# Cargar el GIF usando Pillow
gif_yes = Image.open('gato.gif')
gif_no = pygame.image.load('hamster.jpg')  # Imagen cuando responde "No"

# Crear una lista con los cuadros del GIF
frames = []
try:
    while True:
        frames.append(pygame.image.fromstring(gif_yes.tobytes(), gif_yes.size, gif_yes.mode))
        gif_yes.seek(gif_yes.tell() + 1)
except EOFError:
    pass

# Variables para la animación
frames = frames[2:]  # Evitar los primeros cuadros si son estáticos
frame_count = len(frames)
frame_index = 0

# Crear los botones de "Sí" y "No"
button_width, button_height = 150, 50
yes_button = pygame.Rect(250, 500, button_width, button_height)  # Botón Sí
no_button = pygame.Rect(500, 500, button_width, button_height)   # Botón No

# Colores de los botones
button_color_yes = (0, 143, 57)
button_color_no = (254, 0, 0)

# Banderas para determinar la respuesta
answer = None

running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    # Mostrar GIF animado si aún no han respondido o si la respuesta es "Sí"
    if answer is None or answer == "Yeii! sabía que me aceptarías":
        screen.blit(frames[frame_index], (gif_pos_x, gif_pos_y))  # Usar coordenadas directamente
        frame_index = (frame_index + 1) % frame_count  # Avanzar en la animación

    # Si la respuesta es "No", mostrar la imagen triste
    elif answer == "pipipi :(":
        screen.blit(gif_no, (gif_no_pos_x, gif_no_pos_y))  # Usar coordenadas directamente

    # Solo mostrar el texto si la respuesta aún no se ha seleccionado o es "Sí"
    if answer is None or answer == "Yeii! sabía que me aceptarías":
        screen.blit(text, text_rect)
        screen.blit(text2, text_rect2)
        screen.blit(text3, text_rect3)

    # Dibujar los botones solo si no se ha respondido
    if answer is None:
        pygame.draw.rect(screen, button_color_yes, yes_button)
        pygame.draw.rect(screen, button_color_no, no_button)

        # Texto en los botones
        yes_text = font2.render("Sí", True, (255, 255, 255))
        no_text = font2.render("No", True, (255, 255, 255))
        screen.blit(yes_text,
                    (yes_button.centerx - yes_text.get_width() / 2, yes_button.centery - yes_text.get_height() / 2))
        screen.blit(no_text,
                    (no_button.centerx - no_text.get_width() / 2, no_button.centery - no_text.get_height() / 2))

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and answer is None:
            if yes_button.collidepoint(event.pos):
                answer = "Yeii! sabía que me aceptarías"
            elif no_button.collidepoint(event.pos):
                answer = "pipipi :("

    # Mostrar la respuesta si el usuario hizo clic en un botón
    if answer:
        answer_text = font_response.render(answer, True, (57, 61, 73))
        answer_rect = answer_text.get_rect(center=(WIDTH // 2, HEIGHT - 50))
        screen.blit(answer_text, answer_rect)

    pygame.display.flip()
    clock.tick(15)  # Controla la velocidad de la animación

pygame.quit()
