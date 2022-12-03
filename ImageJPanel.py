class ImageJPanel(JPanel):
    WORLDWIDTH = Configuration.getWorldWidth()
    WORLDHEIGHT = Configuration.getWorldHeight()

    NUMBEROFTILES = Configuration.getNumberOfTiles()

    def getImageHeight(self):
        return self._backgroundImage.getHeight()

    def getImageWidth(self):
        return self._backgroundImage.getWidth()
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public ImageJPanel(String fileName) throws java.io.IOException
    def __init__(self, fileName):
        #instance fields found by Java to Python Converter:
        self._backgroundImage = None

        self._backgroundImage = javax.imageio.ImageIO.read(java.io.File(fileName))

    def paintComponent(self, g):
        super().paintComponent(g)
        #        System.out.println(getHeight())
        #        System.out.println(getWidth())

        # Draw the background image.
        g.drawImage(self._backgroundImage, 0, 0, getWidth(), getHeight(),self)


        tilesManager = TilesManager()
        tilesManager.generateTiles(ImageJPanel.NUMBEROFTILES, ImageJPanel.WORLDWIDTH, ImageJPanel.WORLDHEIGHT)
        if Configuration.isDrawGrid():
            tilesManager.drawGridToPlane(g, getWidth(), getHeight())

        #        
        #        tilesManager.fillCorrespondingTileWithColor(
        #                (Graphics2D) g,
        #                new Coord2D(9999, 9999),
        #                getWidth(), getHeight(),
        #                Color.BLUE)
        #
        #        tilesManager.fillCorrespondingTileWithColor(
        #                (Graphics2D) g,
        #                new Coord2D(0, 0),
        #                getWidth(), getHeight(),
        #                Color.RED)
        #        


        trafficAnalysis = SimpleTrafficAnalysis(tilesManager)
        trafficAnalysis.analyzeTraffic()
        tilesTraffic = trafficAnalysis.getTrafficAnalysis()

        for tileK in tilesTraffic.keys():
            trafficColor = trafficAnalysis.getTrafficColor(tileK)
            tilesManager.fillCorrespondingTileWithColor(g, tileK, getWidth(), getHeight(), trafficColor)

        for l in Main.p.getPath():
            circleDrawer = CircleDrawer(ImageJPanel.WORLDWIDTH, ImageJPanel.WORLDHEIGHT)
            circleDrawer.drawCircleToPlane(g, CircleDrawer.Circle(l.getSpace().getX(), l.getSpace().getY(), 30, Color.BLUE), getWidth(), getHeight())
