class Path:

    def __init__(self, path=None):
        if path is None:
            path = list()
        self._path = path

    def __str__(self):
        s = ""
        for l in self.getPath():
            s += str(l.getSpace())
            s += " ("
            s += str(l.getTime())
            s += "); "
        return s

    def addSpaceTimeLocation(self, toAdd):
        self._path.append(toAdd)

    def getPath(self):
        return self._path

    def setPath(self, path):
        self._path = path
