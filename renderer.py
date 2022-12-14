#!/usr/bin/python3

import pygame
# import pygame_gui
import numpy as np
from world import World
from creature import Creature
from config import *

def main():
  pygame.init()

  WINDOWSIZE = (640, 640)

  pygame.display.set_caption('aybio')
  window_surface = pygame.display.set_mode(WINDOWSIZE, pygame.RESIZABLE | pygame.DOUBLEBUF)

  background = pygame.Surface(CONFIG['WORLDSIZE'])
  clock = pygame.time.Clock()
  is_running = 1

  world = World(borderDims=CONFIG['WORLDSIZE'])
  MAX_FPS=240

  font = pygame.font.Font('freesansbold.ttf', 16)
  updateWindow = False
  ticksPassed = 0
  while is_running:
    time_delta = clock.tick(MAX_FPS)/1000.0
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        is_running = 0

      elif event.type == pygame.VIDEORESIZE:
        WINDOWSIZE = (event.w,event.h)
        window_surface = pygame.display.set_mode(WINDOWSIZE,pygame.RESIZABLE | pygame.DOUBLEBUF)
        # manager.set_window_resolution(WINDOWSIZE)

      elif event.type == pygame.MOUSEBUTTONDOWN:
        button1 = pygame.mouse.get_pressed(num_buttons=3)[0]
        if button1:
          pos = list(pygame.mouse.get_pos())
          widthScale = CONFIG['WORLDSIZE'][0]/window_surface.get_width()
          heightScale = CONFIG['WORLDSIZE'][1]/window_surface.get_height()
          pos[0] = pos[0] * widthScale
          pos[1] = pos[1] * heightScale
          for c in world.creatureList:
            c: Creature
            if c.rect.collidepoint(*pos):
              print(c.genecolor)
              print(c.age)
              print(c.energyLeft)
              print(c.getFitness())

      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          updateWindow = not(updateWindow)

    offscreen_surface = pygame.Surface(CONFIG['WORLDSIZE'])
    # manager.update(time_delta)

    offscreen_surface.blit(background, (0, 0))

    ### simulation logic here
    coords = (
      np.random.randint(CONFIG['FOODSIZE'][0], CONFIG['WORLDSIZE'][0] - CONFIG['FOODSIZE'][0]), 
      np.random.randint(CONFIG['FOODSIZE'][1], CONFIG['WORLDSIZE'][1] - CONFIG['FOODSIZE'][1]), 
    )

    world.update(offscreen_surface)
    ### 
    if updateWindow:
      offscreen_surface = pygame.transform.scale(offscreen_surface, WINDOWSIZE)

      window_surface.blit(offscreen_surface, (0,0))

      numText = font.render(f'Produced: {world.creatureGen}', True, (125,255,125), (0,0,125))
      fitText = font.render(f'Max. Fit: {world.maxFitness}', True, (125,255,125), (0,0,125))
      numTextRect = numText.get_rect()
      numTextRect.topleft = (0,0)
      fitTextRect = fitText.get_rect()
      fitTextRect.topleft = numTextRect.bottomleft
      window_surface.blit(numText, numTextRect)
      window_surface.blit(fitText, fitTextRect)


    # manager.draw_ui(window_surface)

      pygame.display.flip()

    if ticksPassed % 240 == 0:
      fps = str(int(clock.get_fps()))
      print(fps)
    
    ticksPassed += 1

main()