import pygrib, json, numpy

dirFile = pygrib.open('gfs.t18z.pgrb2.0p25.f008.VGRD')
vFile = pygrib.open('gfs.t18z.pgrb2.0p25.f008.UGRD')

vMessage = vFile.message(1)
dirMessage = dirFile.message(1)

data = {
	'count' : dirMessage.numberOfValues,
	'data' : [{
		'pos' : 0,
		'd' : 0,
		'v' : 0,
	}],
	'units' : {
		'v' : vMessage.units,
		'd' : dirMessage.units,
	},
}

#vFilter = vMessage.data(0, 50, 0, 50)
#dirFilter = dirMessage.data(lat1=90, lat2=0, lon1=90, lon2=0)
#print(dirFilter)
lats = dirMessage.latitudes
lons = dirMessage.longitudes

#print(lons[0][0])

bandValCap = 90/0.25
print(bandValCap)

dirn = dirMessage.codedValues

velocities = vMessage.codedValues

#pos = []
#pos.append([])
#count = 0
#row = 0
#print(lons[1])

row = 0

w, h = 180, 180;
pos = [[0 for x in range(w)] for y in range(h)]

for i in range(0, h):
	for j in range(0, w):
		pos[i][j] = lons[j]
		val = {
			'lat' : i * 0.25, 
			'lon' : lons[j], 
			'd' : dirn[i * j], 
			'v' : velocities[i * j]
		}
		data['data'].append(val.copy())
	
for i in range(0, 360 * 360):
	break

#print(pos)
data['pos'] = pos
with open('output.json', 'w') as outfile:  
    json.dump(data, outfile)
exit()
