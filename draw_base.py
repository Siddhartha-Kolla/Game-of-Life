"""
##################################################################################################
Author: Siddhartha Kolla
Date: 26-01-2023
My GitHub: https://github.com/Siddhartha-Kolla
##################################################################################################

Left Mouse Button: Add cell to the life canvas
Right Mouse Button: Remove cell from the life canvas

##################################################################################################
"""




import numpy as np
import pygame as pygame
import tkinter
from tkinter import filedialog
import os

def draw():
    # Function to clear the canvas
    def clear_canvas(rows,cols):
        return np.zeros((rows,cols),np.int8)

    # Function to save the array in a file
    def save_file():
        file_types = [('Numpy File', '*.npy')]
        path = filedialog.asksaveasfilename(filetypes= file_types,defaultextension=file_types,initialdir=os.getcwd())    
        if path == "":
            return None
        np.save(path,cell_status_list)

    def open_filedialog():
        file_types = [('Numpy File', '*.npy')]
        path = filedialog.askopenfilename(filetypes= file_types,defaultextension=file_types,initialdir=os.getcwd())
        return path

    # Function to initialize the variables

    # Initializing pygame
    pygame.init()

    # Size of each cell
    global cell_size
    cell_size = 15

    # Number of rows and columns
    global rows , cols
    rows , cols = 15 , 45 
    # Creating a numpy array to check whether cell is alive or not
    global cell_status_list
    cell_status_list = np.zeros((rows,cols),np.int8)

    # Setting Border thickness and color
    global b_wid, b_color
    b_wid, b_color = 1, (135,135,135)

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

    # Determining the screen size
    global width, height
    width, height = cols*(cell_size+b_wid), rows*(cell_size+b_wid)

    # Configuring screen(setting its size by finding out the space rows and cols need)
    global screen
    screen = pygame.display.set_mode([width,height])

    # Adding a title
    pygame.display.set_caption("Conways Game of Life Pattern Drawer")

    # Adding an icon to the screen
    global icon
    icon = pygame.image.load("logo.png")
    pygame.display.set_icon(icon)

    # Game Loop
    global running
    running = True

    # Main game loop
    while running:

        # Checking events
        for event in pygame.event.get():

            # Quit event
            if event.type == pygame.QUIT:
                running = False
            # Event for checking different key press events
            if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_q:
                #     pygame.quit()
                #     initialize()
                # Clearing the canvas
                if event.key == pygame.K_e:
                    cell_status_list= clear_canvas(rows,cols)
                # Saving the design
                if event.key == pygame.K_s:
                    save_file()
                    cell_status_list = clear_canvas(rows,cols)
                if event.key == pygame.K_o:
                    path = open_filedialog()
                    cell_status_list = np.load(path)
        # Mouse button events
        # For left click
        if pygame.mouse.get_pressed()[0]:
            # Mouse pointer position
            MouseX,MouseY = pygame.mouse.get_pos()
            if not(MouseX > width):
                cell_status_list[MouseY//(cell_size+b_wid), MouseX//(cell_size+b_wid)] = 1
        # For right click
        if pygame.mouse.get_pressed()[2]:
            MouseX,MouseY = pygame.mouse.get_pos()
            if not(MouseX > width):
                cell_status_list[MouseY//(cell_size+b_wid), MouseX//(cell_size+b_wid)] = 0


        # Setting background color
        screen.fill(b_color)

        # Drawing the rectangles
        for y in range(rows):
            for x in range(cols):
                pygame.draw.rect(screen,cell_d_color if cell_status_list[y][x] == 0 else cell_a_color,[x*(b_wid+cell_size),y*(b_wid+cell_size),cell_size,cell_size])
        
        # Updating(Flipping) the whole screen
        pygame.display.flip()

    # Exit the program
    pygame.quit()