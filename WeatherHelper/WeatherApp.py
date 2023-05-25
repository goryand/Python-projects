import random
import requests

locationZip = None

randomLocations = [
    'Miami',
    'Orlando',
    'Atlanta',
    'New York',
    'Cupertino',
    'Scranton',
    'London',
    'Sydney',
    'Las Vegas',
    'Los Angeles',
    'Phoenix'
]

doesUserWantTheirLocation = input("Do you want to see weather data for your location (1) or a random location (2)? ")
if int(doesUserWantTheirLocation):
    if int(doesUserWantTheirLocation) == 1:
        # User wants to do their location
        locationJson = requests.get('http://ip-api.com/json').json()
        locationZip = locationJson.get("zip")
    else:
        # Do a random location from the selection above
        locationZip = random.choice(randomLocations)

# API key based on the website weatherapi.com
# Key has been omitted for GitHub publishing purposes. Poor key. You'll have to add your own if you want this to work.. which you probably don't
weatherApiKey = 'KEY_WAS_OMITTED'

if locationZip is not None:
    responseJson = requests.get('http://api.weatherapi.com/v1/current.json?key=' + str(weatherApiKey) + '&q=' + str(locationZip) + '&aqi=no').json()
    # Returns the weather data as a JSON

    # Put all the city,region,and continent in easy access variables
    requestedCity = responseJson['location']['name']
    requestedRegion = responseJson['location']['region']
    requestedContinent = responseJson['location']['country']
    cityRegion = requestedCity + ", " + requestedRegion

    print("Current weather for " + cityRegion + " in the " + requestedContinent + ":")

    print("It is currently " + responseJson['current']['condition']['text'] + " in " + cityRegion)
    WeatherDataToShow = [
        'humidity',
        'temp_f',
        'last_updated',
        'wind_mph',
        'wind_dir',
        'feelslike_f',
        'vis_miles',
        'precip_in'
    ]

    CachedWeatherData = []

    for iWeatherData in responseJson['current']:
        # Run through the entire JSON
        for ImportantData in WeatherDataToShow:
            # Check if the current JSON iteration is what we want to show in the table WeatherDataToShow
            if iWeatherData == ImportantData:
                # The current JSON iteration is what we want to show, now add it to the list of current weather data
                CachedWeatherData.append(str(iWeatherData) + " is " + str(responseJson['current'][iWeatherData]))
                # I know appending this to a table is dumb.. but I wanted to do it anyway. Sorry not sorry!!!
                # I wanted to get good at .append() , now I am!

    doesUserWantExtraInfo = input("\nDo you want to see extra weather data for " + cityRegion + "?\nY/N: ")

    # If user wants more data, give them all the useless stuff!
    if doesUserWantExtraInfo.lower() == "y":
        for i in CachedWeatherData:
            print(i)
else:
    # locationZip is None, meaning the locationJson doesnt have a 'zip' dictionary entry
    print("Your location doesn't have a Zip code. Maybe you're in some place that doesn't have those.")
    print("Do a random location instead. Oops! :-(")
