from Utils import Utils


class Coord2D:

    def __init__(self, x=None, y=None):

        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y

    def mapFromWorldToPlane(self, worldWidth, worldHeight, planeWidth, planeHeight):

        ret = Coord2D()
        ret.setX(Utils.mapRangeToRange(self.getX(), 0, worldWidth, 0, planeWidth))

        ret.setY(Utils.mapRangeToRange(self.getY(), 0, worldHeight, 0, planeHeight))

        return ret

    @staticmethod
    def mapFromWorldToPlaneX(x, worldWidth, planeWidth):
        return Utils.mapRangeToRange(x, 0, worldWidth, 0, planeWidth)

    @staticmethod
    def mapFromWorldToPlaneY(y, worldHeight, planeHeight):
        return Utils.mapRangeToRange(y, 0, worldHeight, 0, planeHeight)

    def __str__(self):
        return str(self.getX()) + " " + str(self.getY())

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not(self == other)
