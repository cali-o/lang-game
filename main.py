import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1920, 1080
GRID_SIZE = 20
SNAKE_SIZE = 93
SNAKE_SPEED = 8

# Colors
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("lang rapes julius")

# Load images
snake_image = pygame.image.load("snake.png")
food_image = pygame.image.load("food.png")

# Snake variables
snake_segments = [(100, 50)]
snake_direction = (1, 0)

# Food variables
food_x = random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
food_y = random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE

# Score
score = 0
font = pygame.font.Font(None, 36)

# Functions
def draw_snake(snake_segments):
    for segment in snake_segments:
        screen.blit(snake_image, segment)

def draw_food(food_x, food_y):
    screen.blit(food_image, (food_x, food_y))

# Game loop
game_over = False
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)

    # Move snake
    new_head = (snake_segments[0][0] + snake_direction[0] * SNAKE_SIZE, snake_segments[0][1] + snake_direction[1] * SNAKE_SIZE)
    snake_segments.insert(0, new_head)

    # Check for collision with food
    food_rect = pygame.Rect(food_x, food_y, SNAKE_SIZE, SNAKE_SIZE)
    if pygame.Rect(new_head[0], new_head[1], SNAKE_SIZE, SNAKE_SIZE).colliderect(food_rect):
        score += 1
        food_x = random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        food_y = random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
    else:
        snake_segments.pop()

    # Check for collision with walls or itself
    if (new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT or
            new_head in snake_segments[1:]):
        game_over = True

    # Clear the screen
    screen.fill(WHITE)

    # Draw snake and food
    draw_snake(snake_segments)
    draw_food(food_x, food_y)

    # Display score
    text = font.render(f"Score: {score}", True, (0, 255, 0))
    screen.blit(text, (10, 10))

    pygame.display.flip()

    # Control snake speed
    clock.tick(SNAKE_SPEED)

# Game over screen
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)
    game_over_text = font.render("Game Over", True, (0, 255, 0))
    score_text = font.render(f"Score: {score}", True, (0, 255, 0))
    screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2 - 30))
    screen.blit(score_text, (WIDTH // 2 - 60, HEIGHT // 2 + 10))
    pygame.display.flip()
