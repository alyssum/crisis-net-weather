def GPSProximity(coords1, coords2, units='miles'):
    """
    Get the proximity between two GPS locations in miles.
    Depends on the geopy module.
    coords1, coords2 are 2-item lists of [lat, lon]
    """
    from geopy.distance import vincenty as vc
    return vc(coords1, coords2).miles