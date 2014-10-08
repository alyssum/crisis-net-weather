def correlateDataPoints(weatherData, refugeeData, distanceThreshold, units='miles'):
    """
    Finds intersection of two lists of CrisisNet records
    which occcur within x distance of each other
    """
    import json
    results = []
    for refugeeDataPoint in refugeeData['data']:
        for weatherDataPoint in weatherData['data']:
            if refugeeData.has_key('geo') is None:
                print "Skipping refugee record because missing 'geo': " + refugeeData
                continue
            if weatherData.has_key('geo') is None:
                print "Skipping weather record because missing 'geo': " + weatherData
                continue
            weatherCoords = weatherDataPoint['geo']['coords']
            refugeeCoords = refugeeData['geo']['coords']
            distance = GPSProximity(weatherCoords, refugeeCoords, units)
            if distance < distanceThreshold:
                results.append([refugeeCoords, weatherCoords])

    return results

