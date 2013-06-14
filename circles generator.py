import math 
import rhinoscriptsyntax as rs

circles = []
radii = []

for i in range(x):

	pt = (i, math.cos (i), 0)
	id1 = rs.AddCircle(pt, 0.75)
	circles.append(id1)
	endPt = rs.PointAdd(pt, (0, .125, 0)
	id2 = rs.AddLine(pt, endPt)
	radii.append(id2)
	

	a = circles
	b = radii
