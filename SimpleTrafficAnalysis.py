from ColorUtilities import ColorUtilities
from TrafficAnalysis import TrafficAnalysis


class SimpleTrafficAnalysis(TrafficAnalysis):

    def __init__(self, tilesManager):
        self._tilesManager = None
        self._tilesTraffic = None
        self._maxTraffic = 0

        self._tilesManager = tilesManager

    def getTrafficColor(self, tile):
        tileKTraffic = self._tilesTraffic[tile]
        return ColorUtilities.transitionOfHueRange(tileKTraffic/float(self._maxTraffic), 120, 0)

    def getTrafficAnalysis(self):
        return self._tilesTraffic

    def analyzeTraffic(self, path):
        self._tilesTraffic = dict()
        for l in path.getPath():

            tile = self._tilesManager.getCorrespondingTile(l.getSpace())

            if tile in self._tilesTraffic:
                self._tilesTraffic[tile] = self._tilesTraffic[tile] + 1
            else:
                self._tilesTraffic[tile] = 0

        self._maxTraffic = max(self._tilesTraffic.values())

    def getTilesTraffic(self):
        return self._tilesTraffic

