from graphics import*
winW = 300
winH = 300

bTriWin = GraphWin("Blue Triangle", winW, winH)
bTriWin.setCoords(0, 0, 300, 300)
#triangle
bTri = Polygon(Point(250,290), Point(290, 290), Point(265, 240))
bTri.setFill(color_rgb(30, 30, 230))
bTri.draw(bTriWin)
#quad
bQuad = Polygon(Point(10,60), Point(60,60), Point(60,10), Point(10,10))
bQuad.setFill(color_rgb(200, 30, 30))
bQuad.draw(bTriWin)
#penta
bPenta = Polygon(Point(10, 290), Point(60, 290), Point(60, 240), Point(35, 215), Point(10,240))
bPenta.setFill(color_rgb(200,30,200))
bPenta.draw(bTriWin)
#hexagon
bHexa = Polygon(Point(200, 60), Point(225, 110),Point(275, 110), Point(300,60), Point(275,10), Point(225,10))
bHexa.setFill(color_rgb(30,225,40))
bHexa.draw(bTriWin)
#diamond
bDia = Polygon(Point(winW/2,200), Point(200,winH/2), Point(winW/2,100), Point(100,winH/2))
bDia.setFill(color_rgb(70,80,75))
bDia.draw(bTriWin)
