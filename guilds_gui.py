guilds_gui.py – GUI dla systemu Gildii w grze FIROS

import pygame import sys from core.guilds import GuildManager

pygame.init() screen = pygame.display.set_mode((1280, 800)) pygame.display.set_caption("FIROS: Gildie") font = pygame.font.SysFont("timesnewroman", 24) clock = pygame.time.Clock()

WHITE = (255, 255, 255) BLACK = (0, 0, 0) GRAY = (180, 180, 180)

manager = GuildManager()

selected_guild = None input_box = pygame.Rect(300, 100, 400, 40) input_text = "" input_active = False

def draw_interface(): screen.fill(BLACK) title = font.render("Gildie FIROS - Zarządzanie", True, WHITE) screen.blit(title, (480, 20))

# Gildie
for idx, guild in enumerate(manager.guilds):
    y = 160 + idx * 40
    gtext = font.render(f"{guild.name} | Poziom: {guild.level} | Członkowie: {len(guild.members)}", True, GRAY if guild != selected_guild else WHITE)
    screen.blit(gtext, (80, y))

# Utwórz nową
pygame.draw.rect(screen, WHITE if input_active else GRAY, input_box, 2)
input_surface = font.render(input_text, True, WHITE)
screen.blit(input_surface, (input_box.x + 10, input_box.y + 5))
pygame.display.flip()

running = True while running: draw_interface() for event in pygame.event.get(): if event.type == pygame.QUIT: running = False

elif event.type == pygame.MOUSEBUTTONDOWN:
        if input_box.collidepoint(event.pos):
            input_active = True
        else:
            input_active = False

    elif event.type == pygame.KEYDOWN and input_active:
        if event.key == pygame.K_RETURN:
            if input_text.strip():
                manager.create_guild(input_text.strip(), "Player")  # tymczasowy lider
                input_text = ""
        elif event.key == pygame.K_BACKSPACE:
            input_text = input_text[:-1]
        else:
            input_text += event.unicode

clock.tick(30)

pygame.quit() sys.exit()

