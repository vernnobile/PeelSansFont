from robofab.world import CurrentFont

font = CurrentFont()

minContourLength = 2

for glyph in font:
    for contourIndex in reversed(range(len(glyph))):
        contour = glyph[contourIndex]
        if len(contour) <= minContourLength:
            glyph.removeContour(contour)