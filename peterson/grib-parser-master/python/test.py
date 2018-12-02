import pygrib, numpy
grbs = pygrib.open('gfs.t12z.pgrb2.1p00.f000')
#out = open("output.txt", "w")

for grb in grbs:
#   print(grb)
    pass

windDirn = grbs.message(266)
print(windDirn.values)

#print(windDirn[0])
#test = grbs.select(name='metre U wind component')
#print(test)
#selected_grbs=grbs(shortName=['u'],typeOfLevel='heightAboveGround',level=[10,10])
#print(selected_grbs)
exit()
