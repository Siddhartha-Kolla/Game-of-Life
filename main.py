"""
##################################################################################################
Author: Siddhartha Kolla
Date: 26-01-2023
My GitHub: https://github.com/Siddhartha-Kolla
##################################################################################################

Controls:
Up Arrow: Speed Up the life cycle
Down Arrow: Slow Down the life cycle
Space Bar: Pause or Resume the life cycle

Numbers 1 to 4: Change the color theme of the life canvas

Left Mouse Button: Add cell to the life canvas
Right Mouse Button: Remove cell from the life canvas

##################################################################################################
"""




import numpy as np
import pygame as pygame
import random
from tkinter import *
import tkinter.ttk as ttk
from PIL import ImageTk, Image
from tkinter_api import configure_window


def initialize():

    # Initializing pygame
    pygame.init()
    # Initializing font for the pygame
    pygame.font.init()

    list_configure = configure_window()

    global extra_space
    extra_space = 200

    # Size of each cell
    global cell_size
    cell_size = list_configure["size"]

    # Number of rows and columns
    global rows , cols
    rows , cols = list_configure["row"], list_configure["col"]
    # Creating a numpy array to check whether cell is alive or not(currently randomly generated)
    global cell_status_list
    cell_status_list = list_configure["r_or_d"]
    if cell_status_list == "Random":
        cell_status_list = []
        for i in range(rows):
            cell_status_list.append([random.getrandbits(1) for i in range(cols)])
        cell_status_list = np.array(cell_status_list)
    else:
        cell_status_list = np.zeros((rows,cols),np.int8)


    # Creating a numpy array for the cell status after checking the neighbors
    global future_status_list
    future_status_list = np.zeros((rows,cols),np.int8)

    # Speed of the cycle
    global speed
    speed = list_configure["speed"]

    #Border width
    global b_wid
    b_wid = 1

    # Border color
    global border_color
    border_color = (135,135,135)

    list_d = {"Grey - Yellow":(106,106,106),"Black - White":(0,0,0),"Black- Red":(0,0,0),"Green - Purple":(180,40,190)}

    # Dead cell color
    global cell_d_color
    cell_d_color = list_d[list_configure["color_theme"]]

    list_a = {"Grey - Yellow":(255,255,0),"Black - White":(210,10,10),"Black- Red":(245,245,245),"Green - Purple":(40,190,60)}
    # Alive cell color
    global cell_a_color
    cell_a_color = list_a[list_configure["color_theme"]]
    '''Color Combinations
    1. (255,255,0) - (106,106,106)
    2. (210,10,10) - (0,0,0)
    3. (245,245,245) - (0,0,0)
    4. (0,0,0) - (245,245,245)
    5. (40,190,60) - (180,40,190)

    '''

    # Text display screen color
    global t_s_bg
    t_s_bg = (74, 182, 212)

    # Text color
    global t_color
    t_color = (29, 133, 34)

    # Boolean that indicates whether to continue life cycle or not
    global cycle_running
    cycle_running = False

    # Count of life cycles
    global cycle_count
    cycle_count = 0

    global normal_width
    normal_width = cols*(cell_size+b_wid)

    global normal_height
    normal_height = rows*(cell_size+b_wid)

    # Configuring screen(setting its size by finding out the space rows and cols need)
    global screen
    screen = pygame.display.set_mode([normal_width+extra_space,normal_height])

    # Adding clock
    global clock
    clock = pygame.time.Clock()

    # Adding a title
    pygame.display.set_caption("Conways Game of Life")

    # Adding an icon to the screen
    global icon
    icon = pygame.image.load("logo.png")
    pygame.display.set_icon(icon)

    # Setting the font
    global font
    font = pygame.font.Font("freesansbold.ttf", 20)

    # Game Loop
    global running
    running = True

# Function to check the neighbors of each cell and update game list
def check_neighbours():
    # Iterating over each cell and counting the number of neighbors
    for row , col in np.ndindex(cell_status_list.shape):
        neib_temp = 0
        neib_temp = np.sum(cell_status_list[row-1:row+2 , col-1:col+2]) - cell_status_list[row,col]
    
        # Checking if the cell is alive or not and updating its status by using the rules
        # Rules for alive cells 
        if cell_status_list[row][col] == 1:
            if neib_temp == 3 or neib_temp == 2:
                future_status_list[row][col] = 1
            else:
                future_status_list[row][col] = 0

        # Rules for dead cells
        elif cell_status_list[row][col] == 0:
            if neib_temp == 3:
                future_status_list[row][col] = 1
            else:
                future_status_list[row][col] = 0
    
    # Returning the updated list
    return future_status_list

def display_text():
    pygame.draw.rect(screen,t_s_bg,[normal_width,0,extra_space,normal_height])
    speed_text = font.render(str(speed), True, t_color)
    speedText_rect = speed_text.get_rect()
    speedText_rect.center = (normal_width+extra_space//2,normal_height//4)

    screen.blit(speed_text,speedText_rect)

    speed_text = font.render(str(speed), True, t_color)
    speedText_rect = speed_text.get_rect()
    speedText_rect.center = (normal_width+extra_space//2,normal_height//4)

    screen.blit(speed_text,speedText_rect)

    lifeCount_text = font.render(str(cycle_count), True, t_color)
    lifeCountText_rect = lifeCount_text.get_rect()
    lifeCountText_rect.center = (normal_width+extra_space//2,2*normal_height//4)

    screen.blit(lifeCount_text,lifeCountText_rect)

initialize()

# Main game loop
while running:

    # Checking events
    for event in pygame.event.get():

        # Quit event
        if event.type == pygame.QUIT:
            running = False
        # Event for checking different key press events
        if event.type == pygame.KEYDOWN:
            # Space key event(activates the life cycle)
            if event.key == pygame.K_SPACE:
                cycle_running = not cycle_running
            # Speeding up the life cycle
            if event.key == pygame.K_UP:
                speed = min(25,speed+1)
            # Slowing down the life cycel
            if event.key == pygame.K_DOWN:
                speed = max(5,speed-1)
            if event.key == pygame.K_1:
                cell_a_color = (255,255,0)
                cell_d_color = (106,106,106)
            if event.key == pygame.K_2:
                cell_a_color = (0,0,0)
                cell_d_color = (245,245,245)
            if event.key == pygame.K_3:
                cell_a_color = (210,10,10)
                cell_d_color = (0,0,0)
            if event.key == pygame.K_4:
                cell_a_color = (180,40,190)
                cell_d_color = (40,190,60)
            if event.key == pygame.K_q:
                pygame.quit()
                initialize()
    # Mouse button events
    if pygame.mouse.get_pressed()[0]:
        # Mouse pointer position
        MouseX,MouseY = pygame.mouse.get_pos()

        if not(MouseX > normal_width):
            # Setting new status of the clicked cell
            cell_status_list[MouseY//(cell_size+b_wid), MouseX//(cell_size+b_wid)] = 1
            pygame.display.update()
    if pygame.mouse.get_pressed()[2]:
        MouseX,MouseY = pygame.mouse.get_pos()
        if not(MouseX > normal_width):
            cell_status_list[MouseY//(cell_size+b_wid), MouseX//(cell_size+b_wid)] = 0

    # Setting background color
    screen.fill(border_color)

    # Life cycle
    if cycle_running:
        cycle_count += 1
        cell_status_list = np.array(check_neighbours())
    
    display_text()


    # Drawing the rectangles
    for y in range(rows):
        for x in range(cols):
            pygame.draw.rect(screen,cell_d_color if cell_status_list[y][x] == 0 else cell_a_color,[x*(b_wid+cell_size),y*(b_wid+cell_size),cell_size,cell_size])
    
    # Updating(Flipping) the whole screen
    pygame.display.flip()

    clock.tick(speed)
    # Clock tick argument(Useful for making life cycle slower or faster)

# Exit the program
pygame.quit()