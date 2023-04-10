import pygame
import random
import time

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (7, 3, 252)

# Set the dimensions of the screen
W = 608
H = 608

# Set the size of each cell
CELL_WIDTH = 30
CELL_HEIGHT = 30
SPEED = 15
# Initialize Pygame
pygame.init()
score = 0
level = 1

# Create the screen
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake Game")
bg = pygame.image.load("week8/images/snake_bg.png")
# Set the clock for the game
clock = pygame.time.Clock()
font = pygame.font.Font("week8/Fonts/Lato-Black.ttf", 40)
game_over = font.render("Game Over", True, BLUE)


# Define the Snake class
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.body = pygame.surface.Surface((CELL_WIDTH, CELL_HEIGHT))
        self.body.fill(BLUE)
        self.rect = self.body.get_rect()
        self.rect.center = (W/2, H/2)
        self.direction = 'left'
        self.segments = [self.rect]  # list to keep track of body segments

    def move(self):
        if self.direction == 'left' and self.rect.left > 30:
                self.rect.move_ip(-SPEED, 0)
        elif self.direction == 'right' and self.rect.right < W-30:
                self.rect.move_ip(SPEED, 0)
        elif self.direction == 'up' and self.rect.top > 100:
                self.rect.move_ip(0, -SPEED)
        elif self.direction == 'down' and self.rect.bottom < H-30:
                self.rect.move_ip(0, SPEED)
    
        # move each body segment to the position of the segment in front of it
        for i in range(len(self.segments)-1, 0, -1):
            self.segments[i].center = self.segments[i-1].center
        self.segments[0].center = self.rect.center  # update position of head segment
        # draw each body segment on the screen
        for segment in self.segments:
            screen.blit(self.body, segment)
        
        # check if the snake has collided with itself
        for segment in self.segments[5:]:
            if self.rect.colliderect(segment):
                # the snake has collided with itself, so end the game
                screen.fill(RED)
                screen.blit(game_over, (200,250))
                screen.blit(level_counter, (230, 300))
                pygame.display.update()
                for entity in all_sprites:
                    entity.kill() 
                time.sleep(2)
                exit()
        # check if the snake has collided with the walls
        if self.rect.left < 30 or self.rect.right > W - 30 or self.rect.top < 100 or self.rect.bottom > H - 30:
            # the snake has collided with the walls, so end the game
            screen.fill(RED)
            screen.blit(game_over, (200,250))
            screen.blit(level_counter, (230, 300))
            pygame.display.update()
            for entity in all_sprites:
                entity.kill() 
            time.sleep(2)
            exit()

    def grow(self):
        # add new body segment to the list
        new_segment = self.body.get_rect(center=self.segments[-1].center)
        new_segment.move_ip((0, -CELL_HEIGHT))
        self.segments.append(new_segment)
        # move food to a new random location
        food.rect.center = (random.randint(45,W-45), random.randint(120,H-50))

# Define the Food class
class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.body = pygame.surface.Surface((20, 20))
        self.body.fill(RED)
        self.rect = self.body.get_rect()
        
        # generate random location for food
        while True:
            rand_x = random.randint(45, W - 45)
            rand_y = random.randint(120, H - 50)
            self.rect.center = (rand_x, rand_y)
            # check if the location is colliding with the snake's body
            if not any(segment.colliderect(self.rect) for segment in snake.segments):
                break

# Create the Snake and Food objects
snake = Snake()
food = Food()
foods = pygame.sprite.Group()
foods.add(food)
all_sprites = pygame.sprite.Group()
all_sprites.add(snake)
all_sprites.add(food)

# Main game loop
while True:
    # Add background for the screen
    screen.blit(bg, (0, 0))
    SCORE = str(score)
    LEVEL = "Level " + str(level)
    score_counter = font.render(SCORE, False, RED)
    level_counter = font.render(LEVEL, True, BLUE)
    screen.blit(score_counter, (70, 10))
    screen.blit(level_counter, (450, 10))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.direction = 'left'
            elif event.key == pygame.K_RIGHT:
                snake.direction = 'right'
            elif event.key == pygame.K_UP:
                snake.direction = 'up'
            elif event.key == pygame.K_DOWN:
                snake.direction = 'down'
    #create sprites on the screen
    for entity in all_sprites:
        screen.blit(entity.body, entity.rect)
    
    # Move the Snake
    snake.move()

    #check if food was eaten
    if pygame.sprite.spritecollideany(snake, foods):
        snake.grow()
        score += 1

    # Check if score is reached for 5 score
    if score == 5:
        SPEED += 3
        score = 0
        level += 1
    # Update the screen
    pygame.display.update()

    # Set the frame rate of the game
    clock.tick(10)