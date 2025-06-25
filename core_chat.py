core_chat.py — System czatu dla Firos: Magic & Magic

import pygame

class ChatSystem: def init(self, font=None, max_messages=10, quick_messages=None): self.messages = [] self.max_messages = max_messages self.font = font or pygame.font.SysFont("timesnewroman", 18) self.quick_messages = quick_messages or ["GG", "Dobra tura!", "Potężne zaklęcie!", "Odsuń się!", "Twoja tura."] self.input_text = "" self.active = False self.rect = pygame.Rect(20, 600, 700, 180) self.bg_color = (10, 10, 10) self.text_color = (255, 255, 255) self.input_rect = pygame.Rect(25, 750, 600, 25)

def draw(self, screen):
    pygame.draw.rect(screen, self.bg_color, self.rect)
    y = self.rect.top + 10
    for msg in self.messages[-self.max_messages:]:
        text_surface = self.font.render(msg, True, self.text_color)
        screen.blit(text_surface, (self.rect.left + 10, y))
        y += 20

    pygame.draw.rect(screen, (30, 30, 30), self.input_rect)
    input_surface = self.font.render(self.input_text, True, self.text_color)
    screen.blit(input_surface, (self.input_rect.x + 5, self.input_rect.y + 5))

def handle_key(self, key):
    if key == pygame.K_RETURN:
        if self.input_text.strip():
            self.send_message(self.input_text.strip())
            self.input_text = ""
    elif key == pygame.K_BACKSPACE:
        self.input_text = self.input_text[:-1]
    else:
        if len(self.input_text) < 100:
            self.input_text += pygame.key.name(key)

def send_message(self, message):
    self.messages.append(message)
    if len(self.messages) >

