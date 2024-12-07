# Import necessary modules for Pygame, time, and random functionalities
import pygame
import time
import random

# Initialize fonts for text rendering in Pygame
pygame.font.init()

# Set up the window dimensions and player velocity
WIDTH, HEIGHT = 1000, 800
PLAYER_VEL = 5
STAR_VEL = 3
FONT = pygame.font.SysFont("comicsans", 30)

# Player dimensions for the rectangular shape representing the player
PLAYER_WIDTH, PLAYER_HEIGHT = 40, 60

# Initialize the Pygame window with the specified dimensions
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up dimensions for falling stars
STAR_WIDTH, STAR_HEIGHT = 10, 20

# Set the window title
pygame.display.set_caption("Space Dodge")

# Load background image for the game (ensure the file exists)
BG = pygame.image.load("bg.jpeg")

# Function to draw the player, stars, and elapsed time onto the screen
def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0, 0))  # Draw the background on the screen
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")  # Display the elapsed time
    WIN.blit(time_text, (10, 10))  # Position the time text on the screen
    pygame.draw.rect(WIN, "red", player)  # Draw the player as a red rectangle
    for star in stars:  # Loop through all the stars
        pygame.draw.rect(WIN, "white", star)  # Draw each star as a white rectangle
    pygame.display.update()  # Update the display to show the changes

# Main game loop function
def main():
    run = True  # Start the game loop
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_HEIGHT, PLAYER_HEIGHT)  # Create player as a rectangle
    clock = pygame.time.Clock()  # Set up the clock to control frame rate

    start_time = time.time()  # Record the start time to calculate elapsed time
    elapsed_time = 0  # Initialize the elapsed time variable
    star_add_increment = 2000  # Set the initial time interval for adding new stars
    star_count = 0  # Initialize the star count
    stars = []  # List to store stars
    hit = False  # Flag to track if the player has hit a star

    while run:
        star_count += clock.tick(60)  # Control the game to run at 60 frames per second
        elapsed_time = time.time() - start_time  # Update the elapsed time

        # Add stars periodically based on the star_add_increment
        if star_count > star_add_increment:
            for _ in range(7):  # Add 3 stars at a time
                star_x = random.randint(0, WIDTH - STAR_WIDTH)  # Randomly choose the X position of the star
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)  # Create the star at the top of the screen
                stars.append(star)  # Add the star to the list
            star_add_increment = max(200, star_add_increment - 50)  # Decrease the interval for adding stars
            star_count = 0  # Reset the star count

        # Check for events, specifically for quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the user closes the game window
                run = False  # Exit the game loop
                break

        # Check for key presses to move the player left or right
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:  # Move left but not off the screen
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + PLAYER_WIDTH <= WIDTH:  # Move right but not off the screen
            player.x += PLAYER_VEL

        # Update the position of the stars and check for collisions
        for star in stars[:]:  # Loop through all the stars
            star.y += STAR_VEL  # Move the star down the screen
            if star.y > HEIGHT:  # If the star goes off the bottom of the screen
                stars.remove(star)  # Remove the star from the list
            elif star.y + star.height >= player.y and star.colliderect(player):  # If the star hits the player
                stars.remove(star)  # Remove the star
                hit = True  # Set hit flag to True
                break  # Exit the loop as the player has been hit

        # If the player is hit, display a "You Lost" message and end the game
        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")  # Create the "You Lost!" text
            WIN.blit(lost_text, (WIDTH / 2 - lost_text.get_width() / 2, HEIGHT / 2 - lost_text.get_height() / 2))  # Display it in the center
            pygame.display.update()  # Update the screen
            pygame.time.delay(4000)  # Wait for 4 seconds before closing
            break  # Exit the game loop

        # Call the draw function to update the screen with the player, stars, and time
        draw(player, elapsed_time, stars)

    pygame.quit()  # Quit the Pygame window

# Run the main game function when the script is executed
if __name__ == "__main__":
    main()
