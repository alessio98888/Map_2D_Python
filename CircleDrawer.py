import math

import pygame

from Coord2D import Coord2D
from Utils import Utils


class Circle:
    # Center of circle coordinates
    def __init__(self, x, y, diameter, color):
        self.coord = Coord2D(x, y)
        self.diameter = diameter
        self.color = color

    def coordThatIndicatesCenter(self):
        return Coord2D(self.coord.getX(),
                       self.coord.getY())

    def toPlane(self, worldWidth, worldHeight, planeWidth, planeHeight):
        mappedCoord = self.coordThatIndicatesCenter().mapFromWorldToPlane(worldWidth, worldHeight, planeWidth,
                                                                          planeHeight)
        planeDiameter = Utils.mapRangeToRange(self.diameter, 0, worldWidth, 0, planeWidth + planeHeight)
        return Circle(mappedCoord.getX(), mappedCoord.getY(), planeDiameter, self.color)


class CircleDrawer:

    def _initCircles(self):
        self.circles = []

    def __init__(self, worldWidth, worldHeight):
        # instance fields found by Java to Python Converter:
        self.worldWidth = 0
        self.worldHeight = 0
        self.circles = None

        self.worldWidth = worldWidth
        self.worldHeight = worldHeight
        self._initCircles()

    def addCircleToPlane(self, c, planeWidth, planeHeight):
        self.circles.append(c.toPlane(self.worldWidth, self.worldHeight, planeWidth, planeHeight))

    def draw(self, screen):
        for c in self.circles:
            pos = c.coord.getX(), c.coord.getY()
            pygame.draw.circle(screen, (0, 0, 255), pos, c.diameter)
            pygame.display.flip()

    def drawCircleToPlane(self, screen, circleToDraw, planeWidth,
                          planeHeight):  # draw must be called by paintComponent of the panel

        cToPlane = circleToDraw.toPlane(self.worldWidth, self.worldHeight, planeWidth, planeHeight)

        pos = cToPlane.coord.getX(), cToPlane.coord.getY()
        pygame.draw.circle(screen, (0, 0, 255), pos, cToPlane.diameter)

