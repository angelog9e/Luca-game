import pygame
import random
import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("Current Working Directory:", os.getcwd())

pygame.init()
pygame.mixer.init()

# Display
height = 1000
width = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("LUCA")

#Background music
pygame.mixer.music.load("assets/background_music.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.6)

#Sound effects
missed_treat_sound = pygame.mixer.Sound("assets/missed_treat_sound.mp3")
caught_treat_sound = pygame.mixer.Sound("assets/caught_treat_sound.mp3")
powerup_sound = pygame.mixer.Sound("assets/powerup_sound.mp3")
game_over_sound = pygame.mixer.Sound("assets/game_over_sound.wav")

#Volume
missed_treat_sound.set_volume(1.0)
caught_treat_sound.set_volume(1.0)
powerup_sound.set_volume(1.0)
game_over_sound.set_volume(1.0)

#Images
background = pygame.image.load("images/background.png")  #Background
luca_image = pygame.image.load("images/luca_image.png")  #Luca's image
treat_image = pygame.image.load("images/treat_image.png")  #Treat image
score_image = pygame.image.load("images/score_image.png")  #Score image
lives_image = pygame.image.load("images/lives_image.png")  #Lives image
powerup_image = pygame.image.load("images/powerup_image.png") #Powerup image
start_image = pygame.image.load("images/start_image.png") #Start image
play_again_button_image = pygame.image.load("images/play_again_button.png")
exit_button_image = pygame.image.load("images/exit_button.png")

#Luca's properties
luca_x = width - 430
luca_y = height - 410
luca_vel = 7.5

#Treat properties
treat_x = random.randint(0, width - treat_image.get_width())
treat_y = 0
treat_speed = 5  #Treat's speed
treats_caught = 0  #Counter to track the number of treats caught
missed_treats = 0  #Counter for missed treats
lives = 3

#Powerup properties
powerup_x = random.randint(0, width - powerup_image.get_width())
powerup_y = 0
powerup_speed = 12  #Initial speed at which the powerup falls
powerup_timer = 0
powerup_chance = 0.002  #Chance of powerup appearing
powerup_active = False
powerup_duration = 5000
powerup_counter = 0

#Score
score = 0

#Game loop
running = True
game_started = False
clock = pygame.time.Clock()

#Luca's lives
def luca_lives(num_lives):
    x = width - 200
    y = 15
    offset = 60
    
    for i in range(num_lives):
        screen.blit(lives_image, (x + i * offset, y))

# Function to reset game state
def reset_game():
    global luca_x, luca_y, treat_y, treats_caught, missed_treats, lives, powerup_active, powerup_counter, score, treat_speed, luca_vel
    luca_x = width - 430
    luca_y = height - 410
    treat_y = 0
    treats_caught = 0
    missed_treats = 0
    lives = 3
    powerup_active = False
    powerup_counter = 0
    score = 0
    treat_speed = 5
    luca_vel = 7
    pygame.mixer.music.play(-1)

# Get button Rect objects
play_again_button_rect = play_again_button_image.get_rect(center=(width // 2 - 133, height // 2))
exit_button_rect = exit_button_image.get_rect(center=(width // 2 + 133, height // 2))

# Function to display play again and exit button
def game_over():
    final_font = pygame.font.Font("PixelFont.TTF", 30)
    final_text = final_font.render(f"Your Final Score: {score}", True, (0, 0, 0))
    screen.blit(final_text, (width // 2 - 230, height // 3.5))
    screen.blit(play_again_button_image, play_again_button_rect.topleft)
    screen.blit(exit_button_image, exit_button_rect.topleft)
    screen.blit(play_text, play_rect)
    screen.blit(again_text, again_rect)
    screen.blit(exit_text, exit_rect)
    pygame.mixer.music.stop()
    game_over_sound.play()
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    reset_game()
                    return True  # Play again
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()  # Exit

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_button_rect.collidepoint(event.pos):
                    reset_game()
                    return True  # Play again
                elif exit_button_rect.collidepoint(event.pos):
                    sys.exit()  # Exit

# Start screen
start_font = pygame.font.Font("PixelFont.TTF", 24)
start_luca_font = pygame.font.Font("PixelFont.TTF", 80)
start_luca = start_luca_font.render("LUCA", True, (0, 0, 0))
start_luca_rect = start_luca.get_rect(center=(width // 2, height * 2 // 4.5))
start_text = start_font.render("Press Spacebar to Start", True, (255, 255, 255))
start_rect = start_text.get_rect(center=(width // 2, height * 3 // 4.3))

# Play again button text
play_font = pygame.font.Font("PixelFont.TTF", 24)
play_text = play_font.render("Play", True, (0, 0, 0))
play_rect = play_text.get_rect(center=(width // 2 - 135, height // 1- 515))
again_font = pygame.font.Font("PixelFont.TTF", 24)
again_text = again_font.render("Again", True, (0, 0, 0))
again_rect = again_text.get_rect(center=(width // 2 - 133, height // 1 - 490))

# Exit buttn text
exit_font = pygame.font.Font("PixelFont.TTF", 24)
exit_text = exit_font.render("Exit", True, (0, 0, 0))
exit_rect = exit_text.get_rect(center=(width // 2 + 137, height // 2))

# Event Handling
while not game_started:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_started = True

    screen.blit(background, (0, 0))
    screen.blit(start_image, (width // 2 - start_image.get_width() // 2, height * 3 // 200))
    screen.blit(start_luca, start_luca_rect)
    screen.blit(start_text, start_rect)

    pygame.display.update()

while running:
    clock.tick(80)
    screen.blit(background, (0, 0))  # Draw background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and luca_x > -45:
        luca_x -= luca_vel
    if keys[pygame.K_RIGHT] and luca_x < 395:
        luca_x += luca_vel
    if keys[pygame.K_a] and luca_x > -45:
        luca_x -= luca_vel
    if keys[pygame.K_d] and luca_x < 395:
        luca_x += luca_vel

    # Treats handling
    treat_y += treat_speed  # Update the treat's position

    if treat_y > 750:
        treat_x = random.randint(0, width - treat_image.get_width())
        treat_y = 0
        missed_treats += 1
        lives -= 1
        missed_treat_sound.play()
        if missed_treats >= 3:  # Game will end if 3 treats are missed.
            if game_over():
                continue
            else:
                break

    luca_rect = pygame.Rect(luca_x + 60, luca_y + 50, luca_image.get_width() - 120, luca_image.get_height() - 100)
    treat_rect = treat_image.get_rect(topleft=(treat_x, treat_y))

    if luca_rect.colliderect(treat_rect):
        score += 1 # Update the score
        treats_caught += 1
        treat_x = random.randint(0, width - treat_image.get_width())
        treat_y = 0
        caught_treat_sound.play()

    if treats_caught == 3:
        treat_speed += 0.75
        treats_caught = 0

    # Powerup handling
    if not powerup_active and powerup_counter == 0 and random.random() < powerup_chance:
        powerup_x = random.randint(0, width - powerup_image.get_width())
        powerup_y = 0
        powerup_active = True
        powerup_timer = pygame.time.get_ticks()  # Record the time when the powerup was caught

    if powerup_active:
        powerup_y += powerup_speed
        powerup_rect = powerup_image.get_rect(topleft=(powerup_x, powerup_y))

        if luca_rect.colliderect(powerup_rect):
            powerup_active = False
            score += 2
            luca_vel += 7  # Increase luca's speed when the powerup is caught
            powerup_timer = pygame.time.get_ticks()  # Reset the timer when the powerup is caught
            powerup_sound.play()

        screen.blit(powerup_image, (powerup_x, powerup_y))

        if powerup_y > 750:
            powerup_active = False
            powerup_counter = 800  # Control powerup appearance

    if pygame.time.get_ticks() - powerup_timer > powerup_duration:
        luca_vel = 7
        powerup_active = False

    if powerup_counter > 0:
        powerup_counter -= 1

    screen.blit(luca_image, (luca_x, luca_y))
    screen.blit(treat_image, (treat_x, treat_y))

    pixel_font = "PixelFont.TTF"
    font = pygame.font.Font(pixel_font, 20)
    text = font.render(f"Treats: {score}", True, (0, 0, 0))
    screen.blit(score_image, (-40, -30))
    screen.blit(text, (16, 50))
    luca_lives(lives)

    pygame.display.update()

pygame.quit()