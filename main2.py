import datetime
import math
import random

from SpaceTimeLocation import SpaceTimeLocation


class Main:
    p = None

    @staticmethod
    def main(args):

        numberOfTiles = Configuration.getNumberOfTiles()
        worldWidth = Configuration.getWorldWidth()
        worldHeight = Configuration.getWorldHeight()

        Main.p = Path()

        initialX = math.trunc(worldWidth / float(2))
        initialY = math.trunc(worldHeight / float(2))
        currX = initialX
        currY = initialY

        amountOfDelta = 500
        for n in range(0, 100):

            deltaX = random.randint(amountOfDelta) - math.trunc(amountOfDelta / float(2))
            deltaY = random.randint(amountOfDelta) - math.trunc(amountOfDelta / float(2))
            currX += deltaX
            currY += deltaY

            if currX < 0:
                currX = 0
            elif currX > worldWidth:
                currX = worldWidth
            if currY < 0:
                currY = 0
            elif currY > worldHeight:
                currY = worldHeight

            curr = Coord2D(currX, currY)

            Main.p.addSpaceTimeLocation(
                SpaceTimeLocation(curr, datetime.datetime.now() + datetime.timedelta(seconds=24)))

        print(Main.p)
