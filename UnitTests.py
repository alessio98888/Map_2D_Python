#JAVA TO PYTHON CONVERTER TODO TASK: Java 'import static' statements are not converted by Java to Python Converter:
#import static org.junit.jupiter.api.Assertions.assertEquals
class UnitTests:

#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @org.junit.jupiter.api.Test void mapFromWorldToPlane()
    def mapFromWorldToPlane(self):

        pass

#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @org.junit.jupiter.api.Test void mapRangeToRange()
    def mapRangeToRange(self):
        assertEquals(500, Utils.mapRangeToRange(0, 0, 254, 500, 5500))

        assertEquals(0, Utils.mapRangeToRange(0, 0, 10000, 0, 5000))

        assertEquals(2500, Utils.mapRangeToRange(5000, 0, 10000, 0, 5000))