#!/bin/python
# This app was created by Leo Platti in 2023, to work on my first gui application and expand my understanding of classes in python
import tkinter
import tkinter.filedialog
import pygame
# Creating display - setting variables - creating font and timer
pygame.init()
display = pygame.display
screen = display.set_mode((250,300))
display.set_caption('AudioZip - Created by Leo Platti')
screen.fill('grey')
display.flip()
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 18)
# Defining button class... will be used for multiple buttons with different purposes
class buttons:
    def __init__(self,text,x_pos,y_pos, enabled):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.draw()
    
    def draw(self):
        button_text = font.render(self.text, True, 'black')
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos),(100,40))
        if self.check_click():
            pygame.draw.rect(screen, 'dark grey', button_rect, 0, 5,)
        else:
            pygame.draw.rect(screen, 'light blue', button_rect, 0, 5)
        pygame.draw.rect(screen, 'black', button_rect, 2, 5)
        screen.blit(button_text, (self.x_pos + 3, self.y_pos + 3))
    
    def check_click(self):
        mouse = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos),(100,40))
        if left_click and button_rect.collidepoint(mouse) and self.enabled:
            return True
        else:
            return False
# main loop - checks buttons for clicks - button functions if clicked
run = True
while run:
    timer.tick(fps)
    play_button = buttons('Play File', 10, 25, True)
    pause_button = buttons('Pause', 10, 100, True)
    unpause_button = buttons('Unpause', 10, 175, True)
    stop_button = buttons('Stop', 10, 250, True)
    audiozip_display = buttons('AudioZip!', 135, 130, True)
    pmm = pygame.mixer.music
    
    if play_button.check_click():
        print()
        print("Click enter once your file is selected (may require to be pressed twice)")
        file = tkinter.filedialog.askdirectory()
        pygame.mixer.init()
        pmm.load(file)
        pmm.play()
        pmm.get_busy()
        print("Playing File")
    
    if pause_button.check_click():
        pmm.pause()
    
    if unpause_button.check_click():
        pmm.unpause()
    
    if stop_button.check_click():
        pmm.stop()

    for event in pygame.event.get():
     if event.type == pygame.QUIT:
        run = False
        
    display.flip()
pygame.quit()