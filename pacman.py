import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 600
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pac-Man")

# Set up game variables
player_size = 32
player_speed = 5
player_pos = [screen_width/2 - player_size/2, screen_height/2 - player_size/2]

enemy_size = 32
enemy_speed = 3
enemy_pos = [random.randint(0, screen_width-enemy_size), random.randint(0, screen_height-enemy_size)]

# Load images
player_img = pygame.image.load("pacman.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (player_size, player_size))

enemy_img = pygame.image.load("ghost.png").convert_alpha()
enemy_img = pygame.transform.scale(enemy_img, (enemy_size, enemy_size))

# Set up game loop
game_over = False
clock = pygame.time.Clock()

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        # Handle player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_pos[0] -= player_speed
            elif event.key == pygame.K_RIGHT:
                player_pos[0] += player_speed
            elif event.key == pygame.K_UP:
                player_pos[1] -= player_speed
            elif event.key == pygame.K_DOWN:
                player_pos[1] += player_speed

    # Check for collision between player and enemy
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    enemy_rect = pygame.Rect(enemy_pos[0], enemy_pos[1], enemy_size, enemy_size)
    if player_rect.colliderect(enemy_rect):
        game_over = True

    # Draw the game objects
    screen.fill((0, 0, 0))
    screen.blit(player_img, player_pos)
    screen.blit(enemy_img, enemy_pos)

    # Move the enemy randomly
    enemy_pos[0] += enemy_speed * random.choice([-1, 1])
    enemy_pos[1] += enemy_speed * random.choice([-1, 1])

    # Keep the enemy on the screen
    if enemy_pos[0] <= 0:
        enemy_pos[0] = 0
    elif enemy_pos[0] >= screen_width - enemy_size:
        enemy_pos[0] = screen_width - enemy_size
    if enemy_pos[1] <= 0:
        enemy_pos[1] = 0
    elif enemy_pos[1] >= screen_height - enemy_size:
        enemy_pos[1] = screen_height - enemy_size

    # Update the screen
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)

# Clean up Pygame
pygame.quit()
