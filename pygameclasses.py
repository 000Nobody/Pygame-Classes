import random
import pygame
from pygame.locals import *

pygame.init()

class Button():

    def __init__(
            self,
            x,
            y,
            width,
            height,
            font,
            text='',
            color='white',
            pressed_color='grey',
            text_color='black',
            border_color='black',
            border_width=5,
        ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = font
        self.text = text
        self.color = color
        self.pressed_color = pressed_color
        self.text_color = text_color
        self.border_color = border_color
        self.border_width = border_width

        self.rect = pygame.Rect(x, y, width, height)
        self.rendered_text = self.font.render(self.text, 1, self.text_color)
        self.text_rect = self.rendered_text.get_rect()
        self.text_rect.center = self.rect.center


    def isOver(self, mx, my):
        return self.rect.collidepoint(mx, my)


    def draw(self, display, mx, my):
        if self.isOver(mx, my):
            pygame.draw.rect(display, self.pressed_color, self.rect)
        else:
            pygame.draw.rect(display, self.color, self.rect)

        pygame.draw.rect(display, self.border_color, self.rect, self.border_width)
        display.blit(self.rendered_text, (self.text_rect.x, self.text_rect.y))


class TextInput():

    def __init__(
            self,
            x,
            y,
            width,
            height,
            font,
            bgcolor='white',
            text_color='black',
            title_text_color='black',
            border_color=(100, 100, 100),
            selected_border_color=(0, 0, 0),
            border_thickness=5,
            placeholder_text='',
            char_limit=50
        ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = font
        self.bgcolor = bgcolor
        self.text_color = text_color
        self.title_text_color = title_text_color
        self.border_color = border_color
        self.selected_border_color = selected_border_color
        self.border_thickness = border_thickness
        self.text = placeholder_text
        self.char_limit = char_limit
        self.selected = False
        self.rect = pygame.Rect(x, y, width, height)


    def addText(self, text):
        if self.selected:
            if text == 'BACKSPACE':
                self.text = self.text[:-1]
            elif len(self.text) < self.char_limit:
                if self.rendered_text.get_rect().width < self.rect.width-25:
                    self.text += text


    def draw(self, display):
        self.rendered_text = self.font.render(self.text, True, self.text_color)
        pygame.draw.rect(display, self.bgcolor, self.rect)
        if self.selected:
            pygame.draw.rect(display, self.border_color, self.rect, self.border_thickness)
        else:
            pygame.draw.rect(display, self.selected_border_color, self.rect, self.border_thickness)
        display.blit(self.rendered_text, (self.x + 5, self.y + 5))


    def isOver(self, mx, my):
        return self.rect.collidepoint(mx, my)


class Particle:

    def __init__(
            self,
            x,
            y,
            colors,
            min_xvel,
            max_xvel,
            min_yvel,
            max_yvel,
            min_radius,
            max_radius,
            shrink_rate,
            gravity,
        ):
        self.x = x
        self.y = y
        self.color = random.choice(colors)

        if min_xvel < max_xvel:
            self.xvel = random.randint(min_xvel, max_xvel) / 10
        else:
            self.xvel = random.randint(max_xvel, min_xvel) / 10

        if min_yvel < max_yvel:
            self.yvel = random.randint(min_yvel, max_yvel) / 10
        else:
            self.yvel = random.randint(max_yvel, min_yvel) / 10

        self.radius = random.randint(min_radius, max_radius)
        self.shrink_rate = shrink_rate
        self.gravity = gravity


    def update(self):
        self.x += self.xvel
        self.y += self.yvel
        self.radius -= self.shrink_rate
        self.yvel += self.gravity


    def draw(self, display):
        pygame.draw.circle(
            display, self.color, (int(self.x), int(self.y)), int(self.radius)
        )


class CheckBox():

    def __init__(
            self,
            x,
            y,
            width,
            height,
            color='white',
            border_color='black',
            border_thickness=5,
            checked_color=(30, 30, 30)
        ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.border_color = border_color
        self.border_thickness = border_thickness
        self.checked_color = checked_color
        self.checked = False
        self.rect = pygame.Rect(x, y, width, height)


    def draw(self, display):
        if self.checked:
            pygame.draw.rect(display, self.checked_color, self.rect)
        else:
            pygame.draw.rect(display, self.color, self.rect)
        pygame.draw.rect(display, self.border_color, self.rect, self.border_thickness)


    def isOver(self, mx, my):
        return self.rect.collidepoint(mx, my)
        