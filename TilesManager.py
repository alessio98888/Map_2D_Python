import math

import pygame

from Coord2D import Coord2D
from TileRect import TileRect


class TilesManager:

    def __init__(self):
        # instance fields found by Java to Python Converter:
        self._numberOfTiles = 0
        self._tileWidth = 0
        self._tileHeight = 0
        self._worldWidth = 0
        self._worldHeight = 0
        self._tiles = None

    def getWorldWidth(self):
        return self._worldWidth

    def setWorldWidth(self, worldWidth):
        self._worldWidth = worldWidth

    def getWorldHeight(self):
        return self._worldHeight

    def setWorldHeight(self, worldHeight):
        self._worldHeight = worldHeight

    def getNumberOfTiles(self):
        return self._numberOfTiles

    def setNumberOfTiles(self, numberOfTiles):
        self._numberOfTiles = numberOfTiles

    def getTileWidth(self):
        return self._tileWidth

    def setTileWidth(self, tileWidth):
        self._tileWidth = tileWidth

    def getTileHeight(self):
        return self._tileHeight

    def setTileHeight(self, tileHeight):
        self._tileHeight = tileHeight

    def getTiles(self):
        return self._tiles

    def setTiles(self, tiles):
        self._tiles = tiles

    def generateTiles(self, numberOfTiles, worldWidth, worldHeight):
        tilesNonMappedUpperLeftCoord = []
        # DRAW GRID
        stepVertical = math.trunc(worldWidth / float(numberOfTiles))
        stepHorizontal = math.trunc(worldHeight / float(numberOfTiles))
        currentX = stepVertical
        currentY = stepHorizontal
        for i in range(0, numberOfTiles):
            tileCoord = Coord2D()
            tileCoord.setX(currentX)
            tileCoord.setY(currentY)
            tilesNonMappedUpperLeftCoord.append(tileCoord)
            currentX += stepVertical
            currentY += stepHorizontal
        self.setTiles(tilesNonMappedUpperLeftCoord)
        self.setTileWidth(stepVertical)
        self.setTileHeight(stepHorizontal)
        self.setNumberOfTiles(numberOfTiles)
        self.setWorldHeight(worldHeight)
        self.setWorldWidth(worldWidth)

    def drawGridToPlane(self, screen, planeWidth, planeHeight):
        for tile in self._tiles:
            mappedToPlaneTile = tile.mapFromWorldToPlane(self._worldWidth, self._worldHeight, planeWidth, planeHeight)
            mappedX = mappedToPlaneTile.getX()
            mappedY = mappedToPlaneTile.getY()

            pygame.draw.line(screen, (0, 0, 0), (mappedX, 0), (mappedX, planeHeight))
            pygame.draw.line(screen, (0, 0, 0), (0, mappedY), (planeWidth, mappedY))


    def fillCorrespondingTileWithColor(self, screen, worldCoord, planeWidth, planeHeight, color):
        self._drawTileToPlane(screen, self.getCorrespondingTile(worldCoord), planeWidth, planeHeight, color)

    def _drawTileToPlane(self, screen, worldTile, planeWidth, planeHeight, color):
        tileRect = TileRect(worldTile, self.getTileWidth(), self.getTileHeight())
        tileRect.toPlane(self._worldWidth, self._worldHeight, planeWidth, planeHeight)
        tileRect.draw(screen, color)

    def getCorrespondingTile(self, worldCoord):
        correspondingTile = Coord2D()
        correspondingTile.setX((worldCoord.getX() // self.getTileWidth()) * self.getTileWidth())
        correspondingTile.setY((worldCoord.getY() // self.getTileHeight()) * self.getTileHeight())
        return correspondingTile
