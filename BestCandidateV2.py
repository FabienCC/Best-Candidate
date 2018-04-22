import rhinoscriptsyntax as rs 
import random as rd
import operator
Axe = rs.GetObjects("Axe",4)
#Gen = rs.GetObjects("Generatrice",4)
srf = rs.GetObjects("Surface",8)

# Creation dimension lineaire aleatoire
x = []
y = []
z = []

for i in range (0,25):
     x.append(rd.uniform(4,7))
     y.append(rd.uniform(3,5))
     z.append(rd.uniform(40,150))

lineaire = x,y,z

# Intersection des perp frame de l'axe avec la surface

DomAxe = []
DomAxe = rs.CurveDomain(Axe)

OrigineAxe = rs.EvaluateCurve(Axe,DomAxe[0])
cutplane = rs.CurvePerpFrame(Axe, DomAxe[0])

clength = []

if cutplane:
    planesrf = rs.AddPlaneSurface(cutplane, 100, 100)
    curves = rs.IntersectBreps( srf, planesrf)
    rs.DeleteObject(planesrf)
    clength = rs.CurveLength(curves)

#Best Candidate
bat_Util = []

for j in range(len(z)-1):
    bat_Util.append(0)

for k in range(len(z)-1):
    ind = 0
    BDiff = 10
    IsMatching = False
    if bat_Util[k]==0:
        if z[k] > clength:
            diff = z[k] - clength
            if diff < BDiff:
                BDiff = diff
                BBat = z[k]
                ind = k
                IsMatching = True
    if IsMatching:
        bat_Util[ind] = 1

min_index, min_value = min(enumerate(z), key=operator.itemgetter(1))
