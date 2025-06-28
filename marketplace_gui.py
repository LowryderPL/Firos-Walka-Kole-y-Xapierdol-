# marketplace_gui.py — Interfejs GUI dla Marketu Firos
import pygame

from marketplace import Marketplace, Item, Player

pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Firos: Rynek Handlowy")
font = pygame.font.SysFont("georgia", 24)

marketplace = Marketplace()
marketplace.add_item(Item("Miecz Runiczny", "Starożytny miecz o mocy ognia", "epicki", 200, 0.5))
marketplace.add_item(Item("Karta Bohatera: Żarogniew", "Unikalna karta NFT", "legendarna", 0, 1.2))
marketplace.add_item(Item("Hełm Mgły", "Hełm zapewniający ochronę przed magią", "rzadki", 120, 0.3))

player = Player("Wiedźmograd", 600, 3.0)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_marketplace():
    screen.fill(BLACK)
    title = font.render("Rynek Firos — Kliknij przedmiot, aby kupić", True, WHITE)
    screen.blit(title, (50, 30))

    y = 100
    for idx, item in enumerate(marketplace.items):
        text = font.render(
            f"{idx + 1}. {item.name} ({item.rarity}) — {item.price_rfn} RFN / {item.price_ton} TON", True, WHITE
        )
        screen.blit(text, (60, y))
        y += 40

    pygame.display.flip()

def main_loop():
    running = True
    while running:
        draw_marketplace()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_y = pygame.mouse.get_pos()[1]
                selected_index = (mouse_y - 100) // 40
                if 0 <= selected_index < len(marketplace.items):
                    item = marketplace.items[selected_index]
                    result = marketplace.buy_item(item.name, player, "RFN")
                    print(result)

    pygame.quit()

if __name__ == "__main__":
    main_loop()
