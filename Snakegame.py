import pygame as pg
import random as rd 

# Starting the program
pg.init()
pg.display.set_caption('Snakegame')
score = 0
highscore = 0
clock = pg.time.Clock()


# Window size & display
WINDOW = 800
screen = pg.display.set_mode([WINDOW]*2)
Cell_size = 50

# We are making the possible randomness in the beginning position according to the size of each cell
RANGE = (Cell_size // 2, WINDOW - Cell_size // 2, Cell_size)
get_random_position = lambda: [rd.randrange(*RANGE), rd.randrange(*RANGE)]

# Snake status and drawing the snake according to the Cell_size
snake = pg.rect.Rect([0,0,Cell_size-2,Cell_size-2])
snake.center = get_random_position()
snake_tar = (0,0)
bodies = [snake.copy()]
size = 1

# Food status
food = pg.rect.Rect([0,0,Cell_size-2,Cell_size-2])
food.center = get_random_position()

time, time_step = 0, 110

# Movement of the snake
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                snake_tar = (0, -Cell_size)
            if event.key == pg.K_s:
                snake_tar = (0, Cell_size)
            if event.key == pg.K_a:
                snake_tar = (-Cell_size, 0)
            if event.key == pg.K_d:
                snake_tar = (Cell_size, 0)

    screen.fill('brown')

    # Checks if collision is true and excludes the tail of the snake as a body
    self_eating = pg.Rect.collidelist(snake, bodies[:-1]) != -1
        
    # Whenever the snake-head touches the food, the food gets a random position and the snake grows in length
    if food.center == snake.center:
        food.center = get_random_position()
        size +=1
        score += 1
        highscore += 1
        print('Score get')
    # Erecting food
    pg.draw.rect(screen, 'green', food)
    
    # Erecting the snake
    [pg.draw.rect(screen, 'orange', bodies) for bodies in bodies]

    # If the snake has extended itself outside the WINODW then the snake is reset and teleported to a random location
    if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:
        snake.center, food.center = get_random_position(), get_random_position()
        size, snake_tar = 1, (0, 0)
        bodies = [snake.copy()]
        score = 0
    # Shows the scoring throughout the game
    font = pg.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    font = pg.font.Font(None, 36)
    highscore_text = font.render(f"Highscore: {highscore}", True, (255, 255, 255))
    screen.blit(highscore_text, (10, 30))
    # To update the time and rids of the old snakes posistion from the history
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_tar)
        bodies.append(snake.copy())
        bodies = bodies[-size:]

    pg.display.update()
    clock.tick(60)