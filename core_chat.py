core_chat_system.py — Rozszerzony system czatu dla Szachów Królewskich FIROS

import pygame

class ChatSystem: def init(self, quick_messages=None): self.messages = [] self.max_messages = 20 self.font = pygame.font.SysFont("timesnewroman", 20) self.input_active = False self.input_text = "" self.quick_messages = quick_messages if quick_messages else [] self.rect = pygame.Rect(20, 520, 800, 250) self.scroll_offset = 0

def draw(self, screen):
    pygame.draw.rect(screen, (10, 10, 10), self.rect)
    pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

    y_offset = self.rect.y + 5
    visible_messages = self.messages[-(self.max_messages + self.scroll_offset):-self.scroll_offset or None]
    for msg in visible_messages:
        msg_surface = self.font.render(msg, True, (200, 200, 200))
        screen.blit(msg_surface, (self.rect.x + 5, y_offset))
        y_offset += 20

    if self.input_active:
        input_surface = self.font.render(self.input_text + "|", True, (0, 255, 0))
        screen.blit(input_surface, (self.rect.x + 5, y_offset))

def update(self):
    pass

def handle_click(self, pos):
    if self.rect.collidepoint(pos):
        self.input_active = True
    else:
        self.input_active = False

def handle_key(self, key):
    if not self.input_active:
        return

    if key == pygame.K_RETURN:
        self.send_message(self.input_text)
        self.input_text = ""
    elif key == pygame.K_BACKSPACE:
        self.input_text = self.input_text[:-1]
    elif key == pygame.K_UP:
        self.scroll_offset = min(self.scroll_offset + 1, len(self.messages) - self.max_messages)
    elif key == pygame.K_DOWN:
        self.scroll_offset = max(self.scroll_offset - 1, 0)
    else:
        name = pygame.key.name(key)
        if len(name) == 1:
            self.input_text += name

def send_message(self, text):
    if text.strip():
        self.messages.append(f"Ty: {text}")

def send_quick_message(self, text):
    self.messages.append(f"(Szybko): {text}")

def receive_message(self, text):
    self.messages.append(f"Gracz: {text}")

