#!/usr/bin/env python

import pygame
from pygame.locals import K_UP, K_DOWN, K_RIGHT, K_LEFT, KEYDOWN, K_ESCAPE
import time
import pickle
from snake import Snake
from apple import Apple


def check_btn_press(btn, curdir):
    """A helper function for checking button press and changing direction.
    Arguments:
    btn -- Pressed key (pygame format, such as K_UP)
    curdir -- Current direction of the snake (D, U, L, R)
    Returns:
    direction -- The new direction
    """
    direction = curdir
    # Note: we cannot move to the opposite direction
    # (the snake would overlap itself)
    if btn == K_UP and curdir != 'D':
        direction = 'U'
    if btn == K_DOWN and curdir != 'U':
        direction = 'D'
    if btn == K_RIGHT and curdir != 'L':
        direction = 'R'
    if btn == K_LEFT and curdir != 'R':
        direction = 'L'
    return direction


def main():
    """The main function including game loop."""
    # The logical size of the playfield
    n, m = 30, 20
    # The scaling parameter for changing logical size to pixels
    scale = 25
    # The pixel size of the screen is calculated
    w, h = n * scale, m * scale
    # Set the background color
    background_color = (100, 250, 100)

    # Init screen
    pygame.init()
    # Adds some extra space in the bottom for text
    screen = pygame.display.set_mode((w, h + scale * 2))
    pygame.display.set_caption('Snake test game')

    # fill background
    background = pygame.Surface((w, h + scale * 2))
    background = background.convert()
    background.fill(background_color)

    textbox = pygame.Surface.subsurface(background, (scale, h + 2, scale * 15,
                                                     scale * 2 - 2))
    textbox.convert()

    # Fill lines, making a grid
    for i in range(0, h + scale, scale):
        pygame.draw.line(background, (0, 0, 0), (0, i), (w, i))
    for i in range(0, w + scale, scale):
        pygame.draw.line(background, (0, 0, 0), (i, 0), (i, h))

    # Init text
    font = pygame.font.Font(None, 35)

    # Init snake and apple
    # In this example the snake is 3 elements long
    snake = Snake([(1, 3), (2, 3), (3, 3)])
    apple = Apple((5, 5))
    apple.update(snake.body, n, m)

    # Load high score from file if it exists
    try:
        with open('score.dat', 'rb') as file:
            highscore = pickle.load(file)
    except:
        highscore = 0

    # Event loop, this is where the magic happens.
    # A loop counter, explained below
    i = 0
    # A ticker, logically if ticker is n, snake moves every n frames
    ticker = 20
    # The starting direction
    key = K_RIGHT
    # Init current score
    score = 0
    # This will be 0 when we want to quit
    running = 1
    # Some explanation about the loop:
    # The game loop works the way it does because we want the controls to be
    # responsive. In this loop, the loop is repeated every 0.01 seconds,
    # giving us about 100 FPS. For every frame the counter i is incremented.
    # When i is ticker (e.g., 20) we move the snake.
    # What this means is:
    # - Button presses are recorded every frame
    # - The snake moves only every 20 frames
    # - The latest button press is the one that determines snake direction
    try:
        while running:

            screen.blit(background, (0, 0))

            textbox.fill(background_color)

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    key = event.key
                    # Press escape to quit
                    if key == K_ESCAPE:
                        running = 0

            # Move the snake every [ticker] frames
            if i == ticker:
                snake.direction = check_btn_press(key, snake.direction)
                # The snake returns it's own status
                snakestatus = snake.update(n, m, apple.location)
                # If the snake ate an apple (status 1)
                if snakestatus == 1:
                    score = score + 1
                    apple.update(snake.body, n, m)
                    # This makes the game run faster, by decreasing ticker
                    # The minimum value (max speed) is every 7 frames
                    if ticker > 7:
                        ticker = ticker - 1
                # Snake status == 2 means the snake died
                if snakestatus == 2:
                    running = 0
                i = 0

            # Apple and snake draw themselves
            snake.draw(screen, scale)
            apple.draw(screen, scale)

            # Update the text at the bottom
            text = font.render('Score: ' + str(score) + '  High score: ' +
                               str(highscore), 1, (0, 0, 0))
            textbox.blit(text, (0, 0))

            pygame.display.flip()

            i = i + 1
            time.sleep(0.01)

        # Update the high score if necessary
        if score > highscore:
            with open('score.dat', 'wb') as file:
                pickle.dump(score, file)

    finally:
        pygame.quit()


if __name__ == '__main__':
    main()
