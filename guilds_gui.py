guilds_gui.py — GUI do zarzadzania gildiami w grze Firos: Magic & Magic

import pygame import sys from guild_logic import GuildManager

pygame.init() screen = pygame.display.set_mode((1280, 800)) pygame.display.set_caption("FIROS: Gildie") font = pygame.font.SysFont("timesnewroman", 28)

Kolory

WHITE = (255, 255, 255) BLACK = (0, 0, 0) GREY = (80, 80, 80) BLUE = (50, 120, 200)

Inicjalizacja logiki gildi

guilds = GuildManager() selected_guild = None input_name = "" creating_guild = False

def draw_text(text, x, y, color=WHITE): label = font.render(text, True, color) screen.blit(label, (x, y))

def draw_guild_menu(): screen.fill(BLACK) draw_text("Twoje Gildie:", 50, 50)

y_offset = 100
for guild in guilds.get_all_guilds():
    draw_text(f"- {guild['name']} | Lv.{guild['level']} | Exp: {guild['exp']}", 60, y_offset)
    y_offset += 40

draw_text("[N] Nowa Gildia", 50, y_offset + 30)

if creating_guild:
    draw_text("Nazwa nowej gildii:", 50, y_offset + 90)
    pygame.draw.rect(screen, GREY, (400, y_offset + 90, 300, 40))
    draw_text(input_name, 410, y_offset + 95, BLUE)

pygame.display.flip()

running = True clock = pygame.time.Clock()

while running: draw_guild_menu()

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        guilds.save_guilds()
        running = False

    elif event.type == pygame.KEYDOWN:
        if creating_guild:
            if event.key == pygame.K_RETURN:
                if input_name.strip():
                    guilds.create_guild(input_name.strip())
                    input_name = ""
                    creating_guild = False
            elif event.key == pygame.K_BACKSPACE:
                input_name = input_name[:-1]
            else:
                input_name += event.unicode
        elif event.key == pygame.K_n:
            creating_guild = True

clock.tick(30)

pygame.quit() sys.exit()

