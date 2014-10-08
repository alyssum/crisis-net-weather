def getWeatherData(source='weather'):
    import requests
    import json
    """
    Make an API request from CrisisNET using a specified source.
    Outputs the data in JSON.
    """
    
    # Make API request
    apiKey = '5435a0326d18ed0f54deb848'
    
    # Construct request URL
    apiURL = 'http://api.crisis.net/item/?tags=%s' % source

    # Request header
    headers = {'Authorization': 'Bearer ' + apiKey}

    r = requests.get(apiURL, headers=headers)  
    return r.json()

    # to print
    # print json.dumps(r.json(), indent=4, sort_keys=True)
