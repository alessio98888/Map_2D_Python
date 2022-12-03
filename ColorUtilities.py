class ColorUtilities:
    @staticmethod
    def transitionOfHueRange(percentage, startHue, endHue):
        # From 'startHue' 'percentage'-many to 'endHue'
        # Finally map from [0°, 360°] -> [0, 1.0] by dividing
        hue = ((percentage * (endHue - startHue)) + startHue) / 360

        saturation = 1.0
        lightness = 0.5

        # Get the color
        return ColorUtilities.hslColorToRgb(hue, saturation, lightness)

    @staticmethod
    def hslColorToRgb(hue, saturation, lightness):
        if saturation == 0.0:
            # The color is achromatic (has no color)
            # Thus use its lightness for a grey-scale color
            grey = ColorUtilities.percToColor(lightness)
            return grey, grey, grey

        q = None
        if lightness < 0.5:
            q = lightness * (1 + saturation)
        else:
            q = lightness + saturation - lightness * saturation
        p = 2 * lightness - q

        oneThird = 1.0 / 3
        red = ColorUtilities.percToColor(ColorUtilities.hueToRgb(p, q, hue + oneThird))
        green = ColorUtilities.percToColor(ColorUtilities.hueToRgb(p, q, hue))
        blue = ColorUtilities.percToColor(ColorUtilities.hueToRgb(p, q, hue - oneThird))

        return red, green, blue

    @staticmethod
    def hueToRgb(p, q, t):
        if t < 0:
            t += 1
        if t > 1:
            t -= 1

        if t < 1.0 / 6:
            return p + (q - p) * 6 * t
        if t < 1.0 / 2:
            return q
        if t < 2.0 / 3:
            return p + (q - p) * (2.0 / 3 - t) * 6
        return p

    @staticmethod
    def percToColor(percentage):
        return int(round(percentage * 255))
