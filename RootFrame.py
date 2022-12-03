class RootFrame(JFrame):

#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public RootFrame() throws java.io.IOException
    def __init__(self):
        #instance fields found by Java to Python Converter:
        self.fileName = Configuration.getBackgroundImagePath()

        print((java.io.File(self.fileName)).exists())

        panel = ImageJPanel(self.fileName)
        setSize(panel.getImageWidth(),panel.getImageHeight())

        print(getSize())
        self.setContentPane(panel)


        setDefaultCloseOperation(EXIT_ON_CLOSE)

        #pack()
        setLayout(None)
        setVisible(True)
