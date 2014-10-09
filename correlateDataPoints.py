
def correlateDataPoints(weatherData, refugeeData, distanceThreshold, units='miles'):
    """
    Finds intersection of two lists of CrisisNet records
    which occcur within x distance of each other
    """
    import json
    from GPSProximity import *
    results = []
    for refugeeDataPoint in refugeeData['data']: 
        for weatherDataPoint in weatherData['data']:
            if not refugeeDataPoint.has_key('geo') or not refugeeDataPoint['geo'].has_key('coords'):
                print "Skipping refugee record because missing 'geo': " # + json.dumps(refugeeData, indent=4, sort_keys=True)
                continue
            if not weatherDataPoint.has_key('geo') or not weatherDataPoint['geo'].has_key('coords'):
                print "Skipping weather record because missing 'geo': " # + json.dumps(weatherData, indent=4, sort_keys=True)
                continue
            weatherCoords = weatherDataPoint['geo']['coords']
            refugeeCoords = refugeeDataPoint['geo']['coords']
            distance = GPSProximity(weatherCoords, refugeeCoords, units)
            print "Distance between two points " + str(distance)
            if distance < distanceThreshold:
                results.append([refugeeCoords, weatherCoords])

    return results

