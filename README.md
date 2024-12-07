# SpaceDodgeGame
A simple game built entirely using pygame


# Space Dodge

## Game Overview
Space Dodge is a simple arcade-style game where the player controls a red square (representing a spaceship) that must avoid falling stars. The player moves the spaceship left and right at the bottom of the screen, trying to survive as long as possible. The objective is to avoid being hit by stars that randomly fall from the top. The game tracks the player's survival time and displays a "You Lost!" message when a star collides with the spaceship.

## Features:
- **Player Movement:** The player can move the spaceship left and right using the arrow keys.
- **Falling Stars:** Randomly generated stars fall from the top of the screen. Each star moves down at a fixed speed.
- **Collision Detection:** If the player collides with a star, the game ends.
- **Elapsed Time:** The time the player has survived is displayed on the screen.

## Gameplay Mechanics:
1. **Player Control:** The spaceship is controlled using the left and right arrow keys. The spaceship moves at a fixed speed (5 pixels per frame).
2. **Stars:** Every few seconds, stars are added to the game, with a maximum of 3 new stars at a time. The stars fall downwards at a constant speed (3 pixels per frame).
3. **Collisions:** If a star reaches the bottom of the screen or collides with the player, it is removed from the game. When a star collides with the player, the game ends, and the player is shown a "You Lost!" message.
4. **Time Tracking:** The game continuously tracks how long the player survives, displaying this time in seconds on the screen.

## Controls:
- **Left Arrow Key**: Move the spaceship to the left.
- **Right Arrow Key**: Move the spaceship to the right.

## Logic

The Space Dodge game is built using the Pygame library and is a simple game where the player controls a spaceship and attempts to avoid falling stars. Below is a breakdown of how the game works:

1. Game Initialization
The game begins by initializing the necessary libraries: pygame, time, and random. The pygame library is used for handling graphics, user input, and game events. The time library is used to track how long the player survives, while random generates random positions for the falling stars.

Once the libraries are imported, constants for the game window's size, the player's velocity, star velocity, and font settings are defined. The game window is created using pygame.display.set_mode(), setting the window dimensions to 1000x800 pixels. The background image is loaded and displayed throughout the game, giving the player a space-themed backdrop.

2. Game Elements
The player's spaceship is represented by a red rectangle, and its position is initialized at the bottom of the screen. The spaceship can move left or right using the arrow keys, and its position is restricted to the screen's boundaries.

Falling stars are also represented as white rectangles. The stars fall from random positions at the top of the screen and continue to fall down at a constant speed. Every few seconds, new stars are added to the screen. Initially, the game adds 3 stars at a time, and as the game progresses, this frequency increases, making the game more challenging. The stars’ positions are updated every frame, and if a star reaches the bottom of the screen, it is removed.

3. Game Loop
The game’s core logic runs inside a loop, where the game constantly checks for events (like key presses or window closures) and updates the screen. Each frame, the game checks if the player has pressed the left or right arrow keys. Based on the key pressed, the player's spaceship moves horizontally. However, the spaceship cannot move off the screen, so boundaries are checked to ensure the player remains within the game window.

The game also tracks the time elapsed since the start of the game and displays it on the screen. The more time the player survives, the higher the score (time survived). This time counter is updated every frame, providing the player with feedback on their performance.

4. Collision Detection
As the stars fall, the game checks if any of the stars collide with the player’s spaceship. If a collision is detected (i.e., if a falling star touches the spaceship), the game immediately ends, displaying a “You Lost!” message at the center of the screen. The game then waits for a few seconds before quitting.

5. Ending the Game
Once a collision is detected, the game stops the main loop, and the player is shown the "You Lost!" message. After a brief delay, the game window closes, marking the end of the game.

6. Increasing Difficulty
The game becomes more difficult as time passes. Initially, stars are added at a slow rate, but over time, the frequency of star generation increases. This ensures that as the player survives longer, the challenge becomes more intense, requiring faster reactions and better control.

7. Overall Flow
The game starts, the player moves the spaceship to avoid falling stars, and the time is tracked. If the player collides with a star, the game ends, and the player is shown how long they survived. This simple loop repeats until the player loses, making it an exciting and challenging experience.

