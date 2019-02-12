from graphics import*

bTriWin = GraphWin("Blue Triangle", 300, 300)
bTriWin.setCoords(0, 0, 300, 300)
#triangle
bTri = Polygon(Point(250,300), Point(300, 300), Point(275, 280))
bTri.setFill(color_rgb(30, 30, 230))
bTri.draw(bTriWin)
#quad
bQuad = Polygon(Point(0,50), Point(50,50), Point(50,0), Point(0,0))
bQuad.setFill(color_rgb(200, 30, 30))
bQuad.draw(bTriWin)
#penta
bPenta = Polygon(Point(0, 300), Point(50, 300), Point(50, 250), Point(25, 225), Point(0,250))
bPenta.setFill(color_rgb(200,30,200))
bPenta.draw(bTriWin)
