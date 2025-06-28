import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("FIROS: Alchemia")
font = pygame.font.SysFont("georgia", 22)
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (80, 80, 80)
GOLD = (218, 165, 32)

# Przykładowe składniki i receptury
ingredients = {
    "Cierniokorzeń": "Zwiększa siłę",
    "Żywica Szeptów": "Niewidzialność",
    "Krew Dymna": "Otrucie",
    "Łza Feniksa": "Uleczenie",
    "Mroczna Roślina": "Mutacja"
}

recipes = {
    ("Cierniokorzeń", "Krew Dymna"): "Eliksir Furii",
    ("Żywica Szeptów", "Łza Feniksa"): "Mikstura Cienia",
    ("Mroczna Roślina", "Krew Dymna"): "Wywar Zmiany Duszy"
}

selected = []
messages = []

def draw_ui():
    screen.fill((30, 30, 30))
    y = 50
    for name in ingredients:
        color = GOLD if name in selected else WHITE
        txt = font.render(name, True, color)
        screen.blit(txt, (50, y))
        y += 40

    screen.blit(font.render("Kliknij dwa składniki by stworzyć miksturę", True, GRAY), (50, 10))

    msg_y = 300
    for msg in messages[-4:]:
        screen.blit(font.render(msg, True, GOLD), (50, msg_y))
        msg_y += 30

def create_potion():
    global selected
    pair = tuple(sorted(selected))
    potion = recipes.get(pair)
    if potion:
        messages.append(f"🎉 Stworzono: {potion}")
    else:
        messages.append("❌ Błędna kombinacja.")
    selected = []

def handle_click(pos):
    global selected
    x, y = pos
    index = (y - 50) // 40
    if 0 <= index < len(ingredients):
        name = list(ingredients.keys())[index]
        if name in selected:
            selected.remove(name)
        else:
            selected.append(name)
        if len(selected) == 2:
            create_potion()

def main():
    running = True
    while running:
        draw_ui()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_click(event.pos)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
