import random
import time
import os
import sys

# Create the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Initialize the snake and food
snake = [(5, 5)]
food = (10, 10)
direction = (0, 1)  # Initial direction: right

def move_snake():
    global snake
    head_x, head_y = snake[0]
    dir_x, dir_y = direction
    new_head = (head_x + dir_x, head_y + dir_y)
    snake = [new_head] + snake[:-1]

def display_screen():
    clear_screen()
    for y in range(20):
        for x in range(20):
            if (x, y) in snake:
                print('S', end='')
            elif (x, y) == food:
                print('F', end='')
            else:
                print('.', end='')
        print()

def main():
    while True:
        move_snake()
        display_screen()
        time.sleep(0.5)

if __name__ == '__main__':
    main()
