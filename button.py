import pygame as pg
from settings import *
vec = pg.math.Vector2

class Button:
    def __init__(self, surface, x, y, text):
        self.surface = surface
        self.x = x
        self.y = y
        self.width = 150
        self.text = text
        self.height = 50
        self.clicked = False
        self.hovering = False
        self.image = pg.Surface((self.width, self.height))
        self.rect = self.image.get_rect()

    def update(self):
        if self.mouse_hovering(pos):
            self.hovering = True
        else:
            self.hovering = False

    def draw(self):
        action = False

        #get mouse position
        pos = pg.mouse.get_pos()

        #create pygame Rect object for the button
        button_rect = pg.Rect(self.x, self.y, self.width, self.height)
        #check mouseover and clicked conditions
        if button_rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1:
                self.clicked = True
                pg.draw.rect(self.surface, PURPLE, button_rect)
            elif pg.mouse.get_pressed()[0] == 0 and self.clicked == True:
                self.clicked = False
                action = True
            else:
                pg.draw.rect(self.surface, LIGHTBLUE2, button_rect)
        else:
            pg.draw.rect(self.surface, LIGHTBLUE, button_rect)

        #add text to button
        font = pg.font.SysFont("arial", 25)
        text_img = font.render(self.text, True, BLACK)
        text_len = text_img.get_width()
        self.surface.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 13))

        return action
