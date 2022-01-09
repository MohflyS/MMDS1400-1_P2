from functions import d

#Find the overlap between two points
def findOverlap(win, winN):
  overlap = []
  for Ni in winN:
    if win is not Ni:
      if d(win.centroid, Ni.centroid) - (win.radius + Ni.radius) < 0:
        overlap.append(Ni)
  return overlap
