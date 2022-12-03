import math


class Utils:

    @staticmethod
    def mapRangeToRange(x, in_min, in_max, out_min, out_max):
        return math.trunc((x - in_min) * (out_max - out_min) / float(in_max - in_min)) + out_min
