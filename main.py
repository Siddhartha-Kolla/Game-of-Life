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

# 45 15 , acutal 37 11


import numpy as np
import pygame as pygame
import random
from tkinter import *
import tkinter.ttk as ttk
from PIL import ImageTk, Image
from tkinter_api import configure_window
import os
from tkinter import filedialog
from draw_base import draw


def random_list(rows,cols):
    cell_status_list = []
    for i in range(rows):
        cell_status_list.append([random.getrandbits(1) for i in range(cols)])
    return np.array(cell_status_list)

def draw_line(rows,cols):
    cell_status_list = np.zeros((rows,cols),np.int8)
    middle = rows // 2
    for i in range(cols):
        cell_status_list[middle][i] = 1
    return cell_status_list

def draw_glider(rows,cols):
    cell_status_list = np.zeros((rows,cols),np.int8)
    middle_row = rows//2
    middle_column = cols//2
    cell_status_list[middle_row][middle_column] = 1
    cell_status_list[middle_row][middle_column-1] = 1
    cell_status_list[middle_row][middle_column+1] = 1
    cell_status_list[middle_row-1][middle_column+1] = 1
    cell_status_list[middle_row-2][middle_column] = 1
    return cell_status_list

# B3/S23

def rule_compiler(rule):
    rule_list = rule.split("/")
    for i in range(0,len(rule_list)):
        rule_list[i] = "".join(filter(lambda x: x.isdigit(), rule_list[i]))
    return rule_list

def initialize():

    # Initializing pygame
    pygame.init()
    # Initializing font for the pygame
    pygame.font.init()

    # Configuring screen(setting its size by finding out the space rows and cols need)
    global screen
    screen = pygame.display.set_mode([0,0],pygame.FULLSCREEN)

    # Size of each cell
    global cell_size
    cell_size = 10

    # Extracting the display size
    dis_siz_x , dis_siz_y = screen.get_size()
    # Number of rows and columns
    global rows , cols
    rows , cols = dis_siz_y // cell_size, dis_siz_x // cell_size

    # Creating a numpy array to check whether cell is alive or not(currently randomly generated)
    global cell_status_list
    cell_status_list = "Draw"
    if cell_status_list == "Random":
        cell_status_list = random_list(rows,cols)
    else:
        cell_status_list = np.zeros((rows,cols),np.int8)


    # Creating a numpy array for the cell status after checking the neighbors
    global future_status_list
    future_status_list = np.zeros((rows,cols),np.int8)

    # Speed of the cycle
    global speed
    speed = 20

    # Border color
    global border_color
    border_color = (135,135,135)

    list_d = {"Grey - Yellow":(106,106,106),"Black - White":(0,0,0),"Black- Red":(0,0,0),"Green - Purple":(180,40,190)}

    # Dead cell color
    global cell_d_color
    cell_d_color = list_d["Grey - Yellow"]

    list_a = {"Grey - Yellow":(255,255,0),"Black - White":(210,10,10),"Black- Red":(245,245,245),"Green - Purple":(40,190,60)}
    # Alive cell color
    global cell_a_color
    cell_a_color = list_a["Grey - Yellow"]
    '''Color Combinations
    1. (255,255,0) - (106,106,106)
    2. (210,10,10) - (0,0,0)
    3. (245,245,245) - (0,0,0)
    4. (0,0,0) - (245,245,245)
    5. (40,190,60) - (180,40,190)

    '''
    # Boolean that indicates whether to continue life cycle or not
    global cycle_running
    cycle_running = False

    global check_status
    check_status = None

    # Count of life cycles
    global cycle_count
    cycle_count = 0

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

    global rule
    rule = "B3/S23"
    rule = rule_compiler(rule)

    global draw_mode
    draw_mode = False

# Function to check the neighbors of each cell and update game list
def check_neighbours():
    # Iterating over each cell and counting the number of neighbors
    for row , col in np.ndindex(cell_status_list.shape):
        neib_temp = 0
        neib_temp = np.sum(cell_status_list[row-1:row+2 , col-1:col+2]) - cell_status_list[row,col]
    
        cell_status = cell_status_list[row][col]
        for i in range(len(rule[cell_status])):
            if i != len(rule[cell_status])-1:
                if neib_temp == int(rule[cell_status][i]):
                    future_status_list[row][col] = 1
                    break
                else:
                    continue
            else:
                if neib_temp == int(rule[cell_status][i]):
                    future_status_list[row][col] = 1
                else:
                    future_status_list[row][col] = 0
    return future_status_list

initialize()

# Main game loop
while running:

    # Checking events
    for event in pygame.event.get():

        # Quit event
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            check_status = cycle_running
            cycle_running = False
        if event.type == pygame.MOUSEBUTTONUP:
            cycle_running = check_status
            check_status = None
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
            if event.key == pygame.K_ESCAPE:
                quit()
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
                cell_status_list = np.zeros((rows,cols),np.int8)
            if event.key == pygame.K_r:
                cell_status_list = random_list(rows,cols)
            if event.key == pygame.K_l:
                cell_status_list = draw_line(rows,cols)
                cycle_running = False
                print(cell_status_list)
            if event.key == pygame.K_g:
                cell_status_list = draw_glider(rows,cols)
                cycle_running = False
            if event.key == pygame.K_p:
                pygame.quit()
                print(os.getcwd())
                np.save(f"{os.getcwd()}\\temp.npy", cell_status_list)
                draw()
                initialize()
                cell_status_list = np.load(f"{os.getcwd()}\\temp.npy")
            

    # Mouse button events
    if pygame.mouse.get_pressed()[0]:
        # Mouse pointer position
        MouseX,MouseY = pygame.mouse.get_pos()

        if not(MouseY//cell_size > rows-1) and not(MouseX//cell_size > cols-1):
            # Setting new status of the clicked cell
            cell_status_list[MouseY//cell_size, MouseX//cell_size] = 1
    elif pygame.mouse.get_pressed()[2]:
        MouseX,MouseY = pygame.mouse.get_pos()
        if not(MouseY//cell_size > rows) and not(MouseX//cell_size > cols):
            cell_status_list[MouseY//cell_size, MouseX//cell_size] = 0

    # Setting background color
    screen.fill(border_color)

    # Life cycle
    if cycle_running:
        cycle_count += 1
        cell_status_list = np.array(check_neighbours())



    # Drawing the rectangles
    for y in range(rows):
        for x in range(cols):
            pygame.draw.rect(screen,cell_d_color if cell_status_list[y][x] == 0 else cell_a_color,[x*cell_size,y*cell_size,cell_size,cell_size])
    
    # Updating(Flipping) the whole screen
    pygame.display.flip()

    # Clock tick argument(Useful for making life cycle slower or faster)
    clock.tick(speed)

# Exit the program
pygame.quit()