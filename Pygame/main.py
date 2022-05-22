from first_game import *
from second_game import *
from images import *
from random import randint


# Main function for game nr 1
def first_game():
    # Help variables
    fps = 60
    run = True

    # Class instances
    circle = Circle(30, 300, 12)
    track = Track()
    question_img = Image(20, 20, question_mark, 0.13)
    finish_img = Image(685, 75, finish, 0.1)
    circle_view = Button(50, 500, not_clicked_yet, 0.15, clicked)
    play_again_button = Button(190, 320, play_again, 0.5, play_again_clicked)
    back_to_menu_button = Button(410, 320, back_to_menu, 0.5, back_to_menu_clicked)

    pictures = [question_img, finish_img]

    # Main loop
    while run:
        pygame.time.Clock().tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Operation of the game
        circle.move()
        circle.check_if_circle_touche_the_line()

        if circle.hitbox.colliderect(question_img.hitbox):
            if question_img in pictures:
                pictures.remove(question_img)
                x = randint(1, 3)
                if x == 1:
                    circle = Circle(470, 50, 10, [207, 200, 176])
                elif x == 2:
                    circle = Circle(520, 300, 10, [207, 200, 176])
                else:
                    circle = Circle(372.5, 460, 10, [207, 200, 176])

        # Drawing methods
        window.fill((115, 76, 45))
        window.blit(text1, (7, 390))
        window.blit(text2, (7, 370))
        window.blit(text3, (730, 40))

        if circle_view.tick():
            circle.draw_circle_hitbox()

        if circle.hitbox.colliderect(finish_img.hitbox):
            pygame.draw.rect(window, (10, 10, 10), pygame.Rect(150, 100, 500, 400))
            window.blit(text4, (260, 130))
            window.blit(text5, (300, 180))

            play_again_button.draw()
            play_again_button.draw_circuit()
            back_to_menu_button.draw()
            back_to_menu_button.draw_circuit()

            if play_again_button.tick():
                first_game()

            if back_to_menu_button.tick():
                main()

        for image in pictures:
            image.draw()

        circle.draw()
        track.draw_lines()
        circle_view.draw()

        pygame.display.update()


def second_game():
    run = True

    # Help variables
    pixel_size = 50

    # Class instances
    world = Map(background, pixel_size)
    player = Player(30, 450, character)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.blit(sky, (0, 0))

        world.create_map()
        world.draw_map()
        # grid_lines(pixel_size)
        player.move()
        player.draw()

        pygame.display.update()


# Main function
def main():
    run = True

    # Class instances
    button_1 = Button(120, 250, number_1, 0.45, number_1_clicked)
    button_2 = Button(290, 222, number_2, 0.59, number_2_clicked)

    # Main loop
    while run:
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # After click it moves us to a good section
        if button_1.tick():
            first_game()
        elif button_2.tick():
            second_game()

        window.blit(main_screen, (0, 0))
        button_1.draw()
        button_2.draw()

        pygame.display.update()


if __name__ == '__main__':
    main()