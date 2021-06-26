import requests
# The requests module allows you to send HTTP requests using Python.
# The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).

# API key
def getDistance(start, end):
    # open the file that writes api keys.
    api_file = open("api_key.txt", "r")
    #fetch the api key from the first line
    api_key = api_file.readline()
    #close file
    api_file.close()
    
    # base url for connecting the Google Maps.
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"

    # get response
    r = requests.get(url + "origins=" + start + "&destinations=" + end + "&key=" + api_key) 

    # We could return the total time needed and distance needed.
    # time = r.json()["rows"][0]["elements"][0]["duration"]["text"]    
    distance = r.json()["rows"][0]["elements"][0]["distance"]["text"]

    # print the travel time
    # print("The total travel distance from {} to {} is {}".format(start, end, distance))
    return distance

# Running tests examples:
# sample1 = getDistance("2125 Franklin blvd","1585 e 13th ave")
# sample2 = getDistance("eugene", "portland")
