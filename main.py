from datetime import datetime, timedelta
import math
import os
import random

import pygame
from pygame.locals import *

from CircleDrawer import CircleDrawer, Circle
from Coord2D import Coord2D
from Path import Path
from SimpleTrafficAnalysis import SimpleTrafficAnalysis
from SpaceTimeLocation import SpaceTimeLocation
from TilesManager import TilesManager

NUMBER_OF_TILES = 10
WORLD_WIDTH = 10000
WORLD_HEIGHT = 10000

simulatedPath = Path()

initialX = math.trunc(WORLD_WIDTH / float(2))
initialY = math.trunc(WORLD_HEIGHT / float(2))
currX = initialX
currY = initialY

amountOfDelta = 100
timeStamp = datetime.now()

for n in range(0, 100):

    deltaX = random.randint(-math.trunc(amountOfDelta / float(2)), amountOfDelta)
    deltaY = random.randint(-math.trunc(amountOfDelta / float(2)), amountOfDelta)
    currX += deltaX
    currY += deltaY

    if currX < 0:
        currX = 0
    elif currX > WORLD_WIDTH:
        currX = WORLD_WIDTH
    if currY < 0:
        currY = 0
    elif currY > WORLD_HEIGHT:
        currY = WORLD_HEIGHT

    curr = Coord2D(currX, currY)
    timeStamp += timedelta(seconds=24)
    simulatedPath.addSpaceTimeLocation(
        SpaceTimeLocation(curr, timeStamp))
print(simulatedPath)

pygame.init()
screen = pygame.display.set_mode((500, 500), HWSURFACE | DOUBLEBUF | RESIZABLE)
pic = pygame.image.load("images/2D-warehouse-model-final-path-executed.png")
screen.blit(pygame.transform.scale(pic, (500, 500)), (0, 0))
pygame.display.flip()
while True:
    pygame.event.pump()
    event = pygame.event.wait()
    if event.type == QUIT:
        pygame.display.quit()
    elif event.type == VIDEORESIZE:
        screen = pygame.display.set_mode(
            event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
        screen.blit(pygame.transform.scale(pic, event.dict['size']), (0, 0))
        pygame.display.flip()

    tilesManager = TilesManager()
    tilesManager.generateTiles(NUMBER_OF_TILES, WORLD_WIDTH, WORLD_HEIGHT)

    tilesManager.drawGridToPlane(screen, screen.get_width(), screen.get_height())

    trafficAnalysis = SimpleTrafficAnalysis(tilesManager)
    trafficAnalysis.analyzeTraffic(simulatedPath)
    tilesTraffic = trafficAnalysis.getTrafficAnalysis()

    for tileK in tilesTraffic.keys():
        trafficColor = trafficAnalysis.getTrafficColor(tileK)
        tilesManager.fillCorrespondingTileWithColor(screen, tileK, screen.get_width(), screen.get_height(),
                                                    trafficColor)

    for l in simulatedPath.getPath():
        circleDrawer = CircleDrawer(WORLD_WIDTH, WORLD_HEIGHT)
        circleDrawer.drawCircleToPlane(screen, Circle(l.getSpace().getX(), l.getSpace().getY(), 10, (0, 0, 255)),
                                       screen.get_width(), screen.get_height())
    pygame.display.flip()