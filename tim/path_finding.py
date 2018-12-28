#!/usr/bin/python3

import pygrib, numpy, networkx

def main():

    # Open weather data files
    dirFile = pygrib.open('gfs.t18z.pgrb2.0p25.f008.VGRD')
    vFile = pygrib.open('gfs.t18z.pgrb2.0p25.f008.UGRD')

    # Extract primary message
    vMessage = vFile.message(1)
    dirMessage = dirFile.message(1)

    # Extract subset of global grid for faster processing
    globalGrid = gribToDict(vMessage, dirMessage)
    extractGrid = extractData(globalGrid, 100, 100)

    graph = buildGraph(extractGrid)
    print(networkx.shortest_path(graph, 8, 8000))

def gribToDict(v, d):

    data = {
            'count': v.numberOfValues,
            'height': 360 * 4,
            'width': 360 * 4,

            'v': v.codedValues,
            'd': d.codedValues,

            'units': {
                'v': v.units,
                'd': d.units,
                },
            }

    return data

def extractData(superSet, h, w):
    
    resolution = 0.25 # 0.25 degree grid resolution
    gridDimention = int(360 / resolution)

    data = superSet

    data['count'] = h * w
    data['height'] = h
    data['width'] = w

    data['v'] = data['d'] = []

    for i in range(0, h):
        lower = gridDimention * h
        upper = lower + w

        data['v'] += superSet['v'][lower:upper]
        data['d'] += superSet['d'][lower:upper]

    return data

def buildGraph(grid):
    graph = networkx.Graph()
    graph.add_nodes_from(range(grid['count']))

    for i in range(grid['width']):
        for j in range(grid['height']):

            a = i * grid['width'] + j

            # if there is a node to the left, connect it
            if (i < grid['width']):
                b = a + 1
                graph.add_edge(a, b, weight=avg(a,b))


                # if there is a node to the [down, left] connect it
                if (j < grid['height']):
                    b = a + grid['width'] + 1
                    graph.add_edge(a, b, weight=avg(a,b))

            # if there is a node to the [down, right] connect it
            if (i > 0 and j < grid['height']):
                b = a + grid['width'] - 1
                graph.add_edge(a, b, weight=avg(a,b))

            
            # if there is a node below connect it
            if (j < grid['height']):
                b = a + grid['width']
                graph.add_edge(a, b, weight=avg(a,b))
                
    return graph

def avg(a, b):
    return (a + b) / 2

main()
