import pygame
from main import window


class Image:

    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        img_width = int(width * scale)
        img_height = int(height * scale)
        self.hitbox = pygame.Rect(x, y, img_width, img_height)

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Button(Image):

    def __init__(self, x, y, image, scale, clicked_img):
        super().__init__(x, y, image, scale)
        width = clicked_img.get_width()
        height = clicked_img.get_height()
        self.width_img = int(width * scale)
        self.height_img = int(height * scale)
        self.clicked_img = pygame.transform.scale(clicked_img, (self.width_img, self.height_img))

    # Check if we clicked on our image (left mouse button)
    def tick(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True

    def draw(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            window.blit(self.clicked_img, (self.rect.x, self.rect.y))
        else:
            window.blit(self.image, (self.rect.x, self.rect.y))

    def draw_circuit(self):
        pygame.draw.rect(window, (255, 255, 255),
                         (self.rect.x, self.rect.y, self.width_img, self.height_img), 1)