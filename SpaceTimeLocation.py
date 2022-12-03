class SpaceTimeLocation:

    def __init__(self, space, time):
        self._space = space
        self._time = time

    def getSpace(self):
        return self._space

    def setSpace(self, space):
        self._space = space

    def getTime(self):
        return self._time

    def setTime(self, time):
        self._time = time
