import pygame
from tkinter import *


class Draw:

    def __init__(self):
        pygame.init()
        self.pen_thickness = 4
        self.pen_drawtype = 'pen'
        self.touched = False
        self.draw_line = False
        self.screen = pygame.display.set_mode((800, 400))
        pygame.display.set_caption('Draw!')
        self.screen.fill([255, 255, 255])
        self.first_pos = (None, None)
        self.clock = pygame.time.Clock()
        self.TICK = 10
        self.pen_color = pygame.Color(0, 0, 0)
        self.pen_color_2 = self.pen_color
        self.loop()

    def loop(self):
        while True:
            self.clock.tick(7000)
            self.input()
            self.pen_color_2 = self.pen_color

            pygame.draw.rect(self.screen, pygame.Color(0, 0, 0), (0, 0, 700, 2))
            pygame.draw.rect(self.screen, pygame.Color(0, 0, 0), (0, 0, 2, 400))
            pygame.draw.rect(self.screen, pygame.Color(0, 0, 0), (0, 398, 700, 2))

            pygame.draw.rect(self.screen, pygame.Color(207, 164, 109), (700, 0, 100, 400))
            pygame.draw.rect(self.screen, pygame.Color(0, 0, 0), (700, 0, 2, 400))
            pygame.draw.rect(self.screen, pygame.Color(0, 0, 0), (700, 0, 100, 2))
            pygame.draw.rect(self.screen, pygame.Color(0, 0, 0), (798, 0, 2, 400))
            pygame.draw.rect(self.screen, pygame.Color(0, 0, 0), (700, 398, 100, 2))
            self.show_pen_thickness()

            ## Buttons ##
            self.button(720, 20, 20, 20, pygame.Color(219, 68, 55))
            self.button(760, 20, 20, 20, pygame.Color(66, 133, 244))
            self.button(720, 60, 20, 20, pygame.Color(244, 244, 0))
            self.button(760, 60, 20, 20, pygame.Color(15, 157, 88))
            self.button(720, 100, 20, 20, pygame.Color(244, 160, 0))
            self.button(760, 100, 20, 20, pygame.Color(0, 0, 0))
            self.button_BLACK(720, 140, 20, 20)
            self.button(721, 141, 18, 18, pygame.Color(255, 255, 255))

            ## penmode-buttons ##
            self.penmode_pen(720, 200, 20, 20, 2)
            self.penmode_line(760, 200, 20, 20)

            self.touched = pygame.mouse.get_pressed()[0]

            pygame.display.flip()

    ## pressable buttons ##
    def input(self):
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                exit()
        m_pos = pygame.mouse.get_pos()
        x = m_pos[0]
        y = m_pos[1]
        if click[0] is True:
            if 700 > x > -1 and 400 > y > -1 and self.pen_drawtype == 'pen':
                pygame.draw.circle(self.screen, self.pen_color, (x, y), self.pen_thickness)
            elif 700 > x > -1 and 400 > y > -1 and self.pen_drawtype == 'line' and self.draw_line is False:
                pygame.draw.circle(self.screen, self.pen_color, (x, y), self.pen_thickness)
                self.first_pos = (x, y)
                self.draw_line = True
        if 700 > x > -1 and 400 > y > -1 and self.pen_drawtype == 'line' and self.draw_line is True:
            if not click[0] is True and self.draw_line is True:
                pygame.draw.line(self.screen, self.pen_color, (self.first_pos[0], self.first_pos[1]), (x, y),
                                 self.pen_thickness*2)
                pygame.draw.circle(self.screen, self.pen_color, (x+1, y), self.pen_thickness/1)
                self.draw_line = False

        if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
            self.screen.fill([255, 255, 255])
        if pygame.key.get_pressed()[pygame.K_PLUS] or pygame.key.get_pressed()[pygame.K_UP]:
            if self.pen_thickness < 50:
                self.clock.tick(self.TICK)
                self.pen_thickness += 1
        if pygame.key.get_pressed()[pygame.K_MINUS] or pygame.key.get_pressed()[pygame.K_DOWN]:
            if self.pen_thickness > 2:
                self.clock.tick(self.TICK)
                self.pen_thickness -= 1

    def show_pen_thickness(self):
        pygame.draw.circle(self.screen, pygame.Color(0, 0, 0), (750, 350), self.pen_thickness)

    ## show and interact with buttons ##
    def button(self, xp, yp, xw, yw, color):
        pygame.draw.rect(self.screen, color, (xp, yp, xw, yw))
        click = pygame.mouse.get_pressed()
        x, y = pygame.mouse.get_pos()
        if click[0] is True and self.touched is False:
            if x >= xp <= (xp + xw) and y >= yp <= (yp + yw):
                self.pen_color = color

    def button_BLACK(self, xp, yp, xw, yw):
        pygame.draw.rect(self.screen, pygame.Color(0, 0, 0), (xp, yp, xw, yw))
        click = pygame.mouse.get_pressed()
        x, y = pygame.mouse.get_pos()
        if click[0] is True and self.touched is False:
            if x >= xp <= (xp + xw) and y >= yp <= (yp + yw):
                self.pen_color = pygame.Color(0, 0, 0)

    def penmode_pen(self, xp, yp, xw, yw, r):
        pygame.draw.rect(self.screen, pygame.Color(0, 0, 0), (xp, yp, xw, yw))
        pygame.draw.rect(self.screen, pygame.Color(255, 255, 255), (xp+1, yp+1, xw-2, yw-2))
        pygame.draw.circle(self.screen, pygame.Color(0, 0, 0), (xp+(xw/2), yp+(yw/2)), r)
        click = pygame.mouse.get_pressed()
        x, y = pygame.mouse.get_pos()
        if click[0] is True and self.touched is False:
            if x >= xp <= (xp + xw) and y >= yp <= (yp + yw):
                self.pen_drawtype = 'pen'
                self.pen_color = self.pen_color_2

    def penmode_line(self, xp, yp, xw, yw):
        pygame.draw.rect(self.screen, pygame.Color(0, 0, 0), (xp, yp, xw, yw))
        pygame.draw.rect(self.screen, pygame.Color(255, 255, 255), (xp+1, yp+1, xw-2, yw-2))
        pygame.draw.line(self.screen, pygame.Color(0, 0, 0), (xp, yp + yw), (xp + xw, yp))
        click = pygame.mouse.get_pressed()
        x, y = pygame.mouse.get_pos()
        if click[0] is True and self.touched is False:
            if x >= xp <= (xp + xw) and y >= yp <= (yp + yw):
                self.pen_drawtype = 'line'
                self.pen_color = self.pen_color_2


Draw()
