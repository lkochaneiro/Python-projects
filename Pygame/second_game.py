import pygame
from first_game import M, N, window

# load images
normal_dirt = pygame.image.load('images/dirt_tile_09.png').convert_alpha()
normal_dirt_with_small_grass = pygame.image.load('images/dirt_tile_10.png').convert_alpha()
grass_dirt = pygame.image.load('images/dirt_tile_05.png').convert_alpha()
brown_square = pygame.image.load('images/dirt_tile_07.png').convert_alpha()
character = pygame.image.load('images/postac.png').convert_alpha()


def grid_lines(side_of_square):
    n = M // side_of_square
    for line in range(n):
        pygame.draw.line(window, (255, 255, 255), (0, line * side_of_square), (M, line * side_of_square))
        pygame.draw.line(window, (255, 255, 255), (line * side_of_square, 0), (line * side_of_square, N))


class Map:

    def __init__(self, map_matrix, side_of_square):
        self.map = map_matrix
        self.side_of_square = side_of_square
        self.map_list = []

    def create_map(self):
        n, m = len(self.map), len(self.map[0])
        A = self.side_of_square

        for i in range(n):
            for j in range(m):
                if self.map[i][j] == 1:
                    image = pygame.transform.scale(brown_square, (A, A))
                    image_rect = image.get_rect()
                    image_rect.x, image_rect.y = j * A, i * A
                    self.map_list.append((image, image_rect))

                # grass block
                if self.map[i][j] == 2:
                    image = pygame.transform.scale(grass_dirt, (A, A))
                    image_rect = image.get_rect()
                    image_rect.x, image_rect.y = j * A, i * A
                    self.map_list.append((image, image_rect))

                # normal block
                if self.map[i][j] == 3:
                    image = pygame.transform.scale(normal_dirt, (A, A))
                    image_rect = image.get_rect()
                    image_rect.x, image_rect.y = j * A, i * A
                    self.map_list.append((image, image_rect))

                if self.map[i][j] == 4:
                    image = pygame.transform.scale(normal_dirt_with_small_grass, (A, A))
                    image_rect = image.get_rect()
                    image_rect.x, image_rect.y = j * A, i * A
                    self.map_list.append((image, image_rect))

    def draw_map(self):
       for square in self.map_list:
           window.blit(square[0], square[1])


class Player:

    def __init__(self, x, y, image):
        self.image = pygame.transform.scale(image, (50, 100))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def draw(self):
        window.blit(self.image, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        x_position = 0
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            x_position -= 4
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            x_position += 4

        self.rect.x += x_position


# Creating map pixels
background = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 2, 4, 4, 2, 2, 2, 2, 2, 4, 0],
    [0, 0, 0, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
    [2, 2, 2, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]