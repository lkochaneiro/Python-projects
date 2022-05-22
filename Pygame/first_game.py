import pygame
from math import pi

pygame.init()
M, N = 800, 600  # window size
window = pygame.display.set_mode((M, N))

# Loading images
question_mark = pygame.image.load('images/pytajnik.png').convert_alpha()
finish = pygame.image.load('images/flaga_v1.png').convert_alpha()
main_screen = pygame.image.load('images/Mini_games.png').convert_alpha()
number_1 = pygame.image.load('images/numerek11.png').convert_alpha()
number_1_clicked = pygame.image.load('images/numerek11v2.png').convert_alpha()
number_2 = pygame.image.load('images/numerek2.png').convert_alpha()
number_2_clicked = pygame.image.load('images/numerek2v2.png').convert_alpha()
sky = pygame.image.load('images/sky.png').convert_alpha()
not_clicked_yet = pygame.image.load('images/click_me_v2.png')
clicked = pygame.image.load('images/click_me_v1.png')
play_again = pygame.image.load('images/play_again.png')
play_again_clicked = pygame.image.load('images/play_again_v2.png')
back_to_menu = pygame.image.load('images/back_to_menu.png')
back_to_menu_clicked = pygame.image.load('images/back_to_menu_v2.png')

# Text to print on screen
to_show1 = 'You can move with the arrows or WASD.'
to_show2 = 'Your goal is to get to the finish without touching the line!'
to_show3 = 'Finish'
to_show4 = 'Congratulations!'
to_show5 = 'You finish this game.'

# Help variables
text1 = pygame.font.Font.render(pygame.font.SysFont("bahnschrift", 15), to_show1, True, (0, 0, 0))
text2 = pygame.font.Font.render(pygame.font.SysFont("bahnschrift", 15), to_show2, True, (0, 0, 0))
text3 = pygame.font.Font.render(pygame.font.SysFont("bahnschrift", 15), to_show3, True, (0, 0, 0))
text4 = pygame.font.Font.render(pygame.font.SysFont("bahnschrift", 35), to_show4, True, (255, 255, 255))
text5 = pygame.font.Font.render(pygame.font.SysFont("bahnschrift", 20), to_show5, True, (255, 255, 255))


class Circle:
    def __init__(self, x, y, diameter, color=None):
        self.x = x
        self.y = y
        self.diameter = diameter
        self.color = color

        if color is None:
            self.color = [25, 189, 175]

        self.speed = 2
        self.hitbox = pygame.Rect(self.x - self.diameter, self.x - self.diameter,
                                  2*self.diameter, 2*self.diameter)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if self.y >= 0:
                self.y -= self.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            if self.y <= N:
                self.y += self.speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if self.x >= 0:
                self.x -= self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if self.x <= M:
                self.x += self.speed

        self.hitbox = pygame.Rect(self.x, self.y, self.diameter, self.diameter)

    def check_if_circle_touche_the_line(self):
        x_start, y_start = 30, 300  # coordinates of the starting point
        check_point_x, check_point_y = 470, 40  # first check point
        last_check_point_x, last_check_point_y = 660, 450  # last check point
        d = self.diameter

        t = Track()
        green_lines, yellow_lines, red_lines = t.get_rect_from_straight_lines()

        # Check if circle touche straight lines
        for line in green_lines:
            if self.hitbox.colliderect(line):
                self.x, self.y = x_start, y_start

        for line in yellow_lines:
            if self.hitbox.colliderect(line):
                self.x, self.y = check_point_x, check_point_y

        for line in red_lines:
            if self.hitbox.colliderect(line):
                self.x, self.y = last_check_point_x, last_check_point_y

        # Yellow y = ax + b lines.
        if ((self.y == self.x - (190+d)) or (self.y == self.x - (250-d)))\
                and (440 < self.x < 550) and (250 < self.y < 300):  # y = x - (190+2r), y = x - (250-2r)
            self.x, self.y = check_point_x, check_point_y

        if ((self.y == -self.x + 790+d) or (self.y == -self.x + 850-d))\
                and (345 < self.x < 550) and (300 < self.y < 460):  # y = -x + (790+2r), y = -x + (850-2r)
            self.x, self.y = check_point_x, check_point_y

        if self.y == self.x - 290+d and self.x > 760:
            self.x, self.y = check_point_x, check_point_y

        # Circle inequality
        if (self.x - 360)**2 + (self.y - 100)**2 <= (80 + d)**2:
            self.x, self.y = x_start, y_start

        if (self.x - 720)**2 + (self.y - 543)**2 <= (40 + d)**2:
            self.x, self.y = check_point_x, check_point_y

    def draw(self):
        pygame.draw.circle(window, self.color, [self.x, self.y], self.diameter)

    def draw_circle_hitbox(self):
        pygame.draw.rect(window, (255, 255, 255),
                         (self.x - self.diameter, self.y - self.diameter,
                          self.diameter*2, self.diameter*2), 1)


# Class which draw the lines.
class Track:

    @staticmethod
    def get_rect_from_straight_lines():
        # Numbers of green lines
        g1_line = pygame.Rect(0, 260, 212, 13)
        g2_line = pygame.Rect(200, 100, 13, 160)
        g3_line = pygame.Rect(0, 340, 280, 13)
        g4_line = pygame.Rect(280, 100, 13, 240)
        g5_line = pygame.Rect(440, 100, 13, 150)
        g6_line = pygame.Rect(500, 0, 13, 250)
        g7_line = pygame.Rect(20, 100, 180, 13)
        g8_line = pygame.Rect(20, 0, 13, 100)

        # Number of yellow lines
        y1_line = pygame.Rect(345, 445, 13, 155)
        y2_line = pygame.Rect(390, 460, 13, 120)
        y3_line = pygame.Rect(390, 580, 330, 13)
        y4_line = pygame.Rect(640, 543, 40, 13)
        y5_line = pygame.Rect(640, 400, 13, 143)
        y6_line = pygame.Rect(683, 400, 13, 70)
        y7_line = pygame.Rect(683, 470, 77, 13)

        # Number or red lines
        r1_line = pygame.Rect(640, 60, 13, 180)
        r2_line = pygame.Rect(640, 60, 140, 13)
        r3_line = pygame.Rect(780, 60, 13, 80)
        r4_line = pygame.Rect(683, 140, 13, 100)
        r5_line = pygame.Rect(683, 140, 97, 13)
        r6_line = pygame.Rect(640, 360, 11, 40)
        r7_line = pygame.Rect(640, 360, 140, 11)
        r8_line = pygame.Rect(780, 280, 11, 80)
        r9_line = pygame.Rect(640, 280, 140, 11)
        r10_line = pygame.Rect(640, 240, 11, 40)
        r11_line = pygame.Rect(683, 240, 120, 11)
        r12_line = pygame.Rect(683, 400, 120, 11)

        # Array of all straight lines
        get_green_lines = [g1_line, g2_line, g3_line, g4_line, g5_line, g6_line, g7_line, g8_line]
        get_yellow_lines = [y1_line, y2_line, y3_line, y4_line, y5_line, y6_line, y7_line]
        get_red_lines = [r1_line, r2_line, r3_line, r4_line, r5_line, r6_line, r7_line,
                         r8_line, r9_line, r10_line, r11_line, r12_line]

        return get_green_lines, get_yellow_lines, get_red_lines

    @staticmethod
    def draw_lines():
        # Colors
        green = (77, 184, 15)
        yellow = (189, 132, 25)
        red = (219, 20, 20)

        # Green lines
        pygame.draw.rect(window, green, pygame.Rect(0, 260, 200, 2), 1)
        pygame.draw.rect(window, green, pygame.Rect(200, 100, 2, 162), 1)
        pygame.draw.rect(window, green, pygame.Rect(0, 340, 280, 2), 1)
        pygame.draw.rect(window, green, pygame.Rect(280, 100.5, 2, 242), 1)
        pygame.draw.rect(window, green, pygame.Rect(440, 100, 2, 150), 1)
        pygame.draw.rect(window, green, pygame.Rect(500, 0, 2, 250), 1)
        pygame.draw.rect(window, green, pygame.Rect(20, 100, 180, 2), 1)
        pygame.draw.rect(window, green, pygame.Rect(20, 0, 2, 100), 1)

        # Yellow lines
        pygame.draw.rect(window, yellow, pygame.Rect(345, 445, 2, 155), 1)
        pygame.draw.rect(window, yellow, pygame.Rect(390, 460, 2, 120), 1)
        pygame.draw.rect(window, yellow, pygame.Rect(390, 580, 330, 2), 1)
        pygame.draw.rect(window, yellow, pygame.Rect(640, 543, 40, 2), 1)
        pygame.draw.rect(window, yellow, pygame.Rect(640, 400, 2, 143), 1)
        pygame.draw.rect(window, yellow, pygame.Rect(683, 400, 2, 70), 1)
        pygame.draw.rect(window, yellow, pygame.Rect(683, 470, 77, 2), 1)

        yellow_axb_1 = [(440, 250), (490, 300), (345, 445)]  # y = ax + b, a = 1 v a = -1
        yellow_axb_2 = [(500, 250), (550, 300), (390, 460)]  # y = ax + b
        yellow_axb_3 = [(760, 470), (800, 510)]  # y = ax + b

        # Red lines
        pygame.draw.rect(window, red, pygame.Rect(640, 60, 2, 180), 1)
        pygame.draw.rect(window, red, pygame.Rect(640, 60, 140, 2), 1)
        pygame.draw.rect(window, red, pygame.Rect(780, 60, 2, 80), 1)
        pygame.draw.rect(window, red, pygame.Rect(683, 140, 2, 100), 1)
        pygame.draw.rect(window, red, pygame.Rect(683, 140, 97, 2), 1)
        pygame.draw.rect(window, red, pygame.Rect(640, 360, 2, 40), 1)
        pygame.draw.rect(window, red, pygame.Rect(640, 360, 140, 2), 1)
        pygame.draw.rect(window, red, pygame.Rect(780, 280, 2, 80), 1)
        pygame.draw.rect(window, red, pygame.Rect(640, 280, 140, 2), 1)
        pygame.draw.rect(window, red, pygame.Rect(640, 240, 2, 40), 1)
        pygame.draw.rect(window, red, pygame.Rect(683, 240, 120, 2), 1)
        pygame.draw.rect(window, red, pygame.Rect(683, 400, 120, 2), 1)

        # Draw y = ax + b lines and arcs.
        pygame.draw.lines(window, yellow, False, yellow_axb_1, 2)
        pygame.draw.lines(window, yellow, False, yellow_axb_2, 2)
        pygame.draw.lines(window, yellow, False, yellow_axb_3, 2)
        pygame.draw.arc(window, green, [280, 20, 162, 160], 0, pi, 3)
        pygame.draw.arc(window, yellow, [680, 503, 80, 80], 3/2*pi, pi, 3)