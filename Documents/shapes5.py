from graphics import*

bTriWin = GraphWin("Blue Triangle", 300, 300)
bTriWin.setCoords(0, 0, 300, 300)

bTri = Polygon(Point(250,300), Point(300, 300), Point(275, 280))
bTri.setFill(color_rgb(30, 30, 230))
bTri.draw(bTriWin)

bTriWin.getMouse()
bTriWin.close()
