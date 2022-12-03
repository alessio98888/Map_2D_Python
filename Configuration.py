class Configuration:
    _CONFIGURATION_FILE_NAME = "configuration.properties"
    _BACKGROUND_IMAGE_PATH_KEY = "backgroundImagePath"
    _NUMBER_OF_TILES_KEY = "numberOfTiles"
    _WORLD_WIDTH_KEY = "worldWidth"
    _WORLD_HEIGHT_KEY = "worldHeight"
    _DRAW_GRID_KEY = "drawGrid"

    _numberOfTiles = 0


    _backgroundImagePath = None
    _worldWidth = 0
    _worldHeight = 0
    _drawGrid = False

    _alreadyCalled = False

    @staticmethod
    def getConfiguration():
        if not Configuration._alreadyCalled:
            Configuration._alreadyCalled = True
            properties = java.util.Properties()
            try:
                loader = Thread.currentThread().getContextClassLoader()
                stream = loader.getResourceAsStream(Configuration._CONFIGURATION_FILE_NAME)
                properties.load(stream)

            except java.io.IOException as e:
                System.err.println("Error reading " + Configuration._CONFIGURATION_FILE_NAME + ".")
                raise RuntimeException(e)

            try:
                Configuration._numberOfTiles = int(properties.getProperty(Configuration._NUMBER_OF_TILES_KEY))
                Configuration._worldHeight = int(properties.getProperty(Configuration._WORLD_WIDTH_KEY))
                Configuration._worldWidth = int(properties.getProperty(Configuration._WORLD_HEIGHT_KEY))
                Configuration._drawGrid = bool(properties.getProperty(Configuration._DRAW_GRID_KEY))
                Configuration._backgroundImagePath = properties.getProperty(Configuration._BACKGROUND_IMAGE_PATH_KEY)

            except java.lang.NumberFormatException as e:
                System.err.println("Some properties are in the wrong format in file " + Configuration._CONFIGURATION_FILE_NAME + ".")
                raise RuntimeException(e)

    @staticmethod
    def getBackgroundImagePath():
        Configuration._getConfigIfNeeded()
        return Configuration._backgroundImagePath

    @staticmethod
    def getNumberOfTiles():
        Configuration._getConfigIfNeeded()
        return Configuration._numberOfTiles

    @staticmethod
    def getWorldWidth():
        Configuration._getConfigIfNeeded()
        return Configuration._worldWidth

    @staticmethod
    def getWorldHeight():
        Configuration._getConfigIfNeeded()
        return Configuration._worldHeight

    @staticmethod
    def isDrawGrid():
        Configuration._getConfigIfNeeded()
        return Configuration._drawGrid

    @staticmethod
    def _getConfigIfNeeded():
        if not Configuration._alreadyCalled:
            Configuration.getConfiguration()
