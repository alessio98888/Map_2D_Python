import math

class CircleDrawer:

    class Circle:
        # Center of circle coordinates
        def __init__(self, x, y, diameter, color):
            #instance fields found by Java to Python Converter:
            self.coord = None
            self.diameter = 0
            self.color = None

            self.coord = Coord2D(x, y)
            self.diameter = diameter
            self.color = color

        def coordThatIndicatesCenter(self, coordinate):
            return coordinate - math.trunc(self.diameter / float(2))
        def coordThatIndicatesCenter(self):
            return Coord2D(self.coord.getX() - math.trunc(self.diameter / float(2)), self.coord.getY() - math.trunc(self.diameter / float(2)))

        def toPlane(self, worldWidth, worldHeight, planeWidth, planeHeight):
            mappedCoord = self.coordThatIndicatesCenter().mapFromWorldToPlane(worldWidth, worldHeight, planeWidth, planeHeight)
            planeDiameter = Utils.mapRangeToRange(self.diameter, 0, worldWidth, 0, planeWidth + planeHeight)
            return Circle(mappedCoord.getX(), mappedCoord.getY(), planeDiameter, self.color)



    def _initCircles(self):
        self.circles = []

    def __init__(self, worldWidth, worldHeight):
        #instance fields found by Java to Python Converter:
        self.worldWidth = 0
        self.worldHeight = 0
        self.circles = None

        self.worldWidth = worldWidth
        self.worldHeight = worldHeight
        self._initCircles()
    def addCircleToPlane(self, c, planeWidth, planeHeight):
        self.circles.append(c.toPlane(self.worldWidth, self.worldHeight, planeWidth, planeHeight))
    def draw(self, g): # draw must be called by paintComponent of the panel
        for c in self.circles:
            g.fillOval(c.coord.getX(), c.coord.getY(), c.diameter, c.diameter)

    def drawCircleToPlane(self, g, circleToDraw, planeWidth, planeHeight): # draw must be called by paintComponent of the panel
        prevColor = g.getColor()
        g.setColor(circleToDraw.color)
        cToPlane = circleToDraw.toPlane(self.worldWidth, self.worldHeight, planeWidth, planeHeight)
        g.fillOval(cToPlane.coord.getX(), cToPlane.coord.getY(), cToPlane.diameter, cToPlane.diameter)
        g.setColor(prevColor)



