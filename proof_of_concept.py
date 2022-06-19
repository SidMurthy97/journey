'''This script tests whether I can actually retrieve the data that I want'''

import os
from turtle import home 
import googlemaps
from datetime import datetime
import pprint
#first get the API key 
api_key = os.getenv("JOURNEY_KEY")
home_address = os.getenv("JOURNIFY_HOME_ADDRESS")
work_address = os.getenv("JOURNIFY_WORK_ADDRESS")

#authenciate
gmaps = googlemaps.Client(key=api_key)

now = datetime.now()
directions_result = gmaps.directions("21 Selwyn Road, CB39EA",
                                     "Evonetix",
                                     mode="driving",
                                     departure_time=now)

pprint.pprint(directions_result)

