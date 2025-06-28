import pygame import sys from alchemy import AlchemySystem, Backpack

Inicjalizacja

pygame.init() screen = pygame.display.set_mode((900, 600)) pygame.display.set_caption("FIROS Alchemia") font = pygame.font.SysFont("timesnewroman", 22) clock = pygame.time.Clock()

Systemy

alchemy = AlchemySystem() backpack = Backpack()

Kolory

WHITE = (255, 255, 255) BLACK = (0, 0, 0) GRAY = (100, 100, 100) GREEN = (0, 200, 0)

input_box = pygame.Rect(50, 500, 800, 32) user_text = '' feedback_text = ''

def draw_interface(): screen.fill((30, 30, 30))

title = font.render("System Alchemii FIROS", True, WHITE)
screen.blit(title, (50, 20))

desc = font.render("Wpisz składniki (oddzielone przecinkami) i naciśnij Enter", True, GRAY)
screen.blit(desc, (50, 60))

txt_surface = font.render(user_text, True, WHITE)
screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
pygame.draw.rect(screen, WHITE, input_box, 2)

feedback_surface = font.render(feedback_text, True, GREEN)
screen.blit(feedback_surface, (50, 550))

pygame.display.flip()

def main(): global user_text, feedback_text

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                ingredients = [s.strip() for s in user_text.split(',')]
                result = alchemy.craft(ingredients)
                feedback_text = result
                user_text = ''
            elif event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode

    draw_interface()
    clock.tick(30)

pygame.quit()
sys.exit()

if name == "main": main()

