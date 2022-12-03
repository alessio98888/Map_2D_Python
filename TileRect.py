from Coord2D import Coord2D


class TileRect:

    def __init__(self, upperLeft, width, height):
        # instance fields found by Java to Python Converter:
        self._upperLeft = None
        self._width = 0
        self._height = 0

        self._upperLeft = upperLeft
        self._width = width
        self._height = height

    def toPlane(self, worldWidth, worldHeight, planeWidth, planeHeight):
        self.setUpperLeft(self.getUpperLeft().mapFromWorldToPlane(worldWidth, worldHeight, planeWidth, planeHeight))
        self.setWidth(Coord2D.mapFromWorldToPlaneX(self.getWidth(), worldWidth, planeWidth))
        self.setHeight(Coord2D.mapFromWorldToPlaneY(self.getHeight(), worldHeight, planeHeight))

    def draw(self, g, color):
        prevColor = g.getColor()
        g.setColor(color)
        g.fillRect(self.getUpperLeft().getX(), self.getUpperLeft().getY(), self.getWidth(), self.getHeight())
        g.setColor(prevColor)

    def getUpperLeft(self):
        return self._upperLeft

    def setUpperLeft(self, upperLeft):
        self._upperLeft = upperLeft

    def getWidth(self):
        return self._width

    def setWidth(self, width):
        self._width = width

    def getHeight(self):
        return self._height

    def setHeight(self, height):
        self._height = height
