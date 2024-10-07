import folium

from streamlit_folium import folium_static

import streamlit as st

from geopy.geocoders import Nominatim

from geopy.exc import GeocoderTimedOut

import climateserv

import pandas as pd

import os




#user interface, change background color

# Custom CSS to change the background color

background_color_style = """

   <style>

   /* CSS to set background color for the whole page */

   .stApp {

       background-color: #88B984;

   }

   </style>

"""












# Inject the custom CSS into the Streamlit app

st.markdown(background_color_style, unsafe_allow_html=True)






# Initialize the geocoder

geolocator = Nominatim(user_agent="streamlit_app")




# Function to get coordinates from an address

def get_coordinates(address):

   try:

       location = geolocator.geocode(address, timeout=10)

       if location:

           return (location.latitude, location.longitude)

       else:

           return None

   except GeocoderTimedOut:

       return None




# Function to make the ClimateSERV API call and retrieve data

def request_climateserv_data(x, y, databranch, outfile='out.csv'):

   GeometryCoords = [

       [x - 0.01, y + 0.01],

       [x + 0.01, y + 0.01],

       [x + 0.01, y - 0.01],

       [x - 0.01, y - 0.01],

       [x - 0.01, y + 0.01]

   ]




   #potench code for drop down option bar

   #dataset_type = st.selectbox(

      # 'I want to learn:',

     #  options=[38,39,40],

     #  index=0

   #)

   #if(option=='Soil Moisture'):

     #  DatasetType==40

   #elif (option=='Precipitation'):

      # DatasetType=90

   #elif (option=='Drought Risk'):

      # DatasetType=41




   OperationType = 'Average'

   #provide data over previous year

   EarliestDate = '01/01/2023'

   LatestDate = '12/31/2023'

   SeasonalEnsemble = ''  # Leave empty when using the new integer dataset IDs

   SeasonalVariable = ''  # Leave empty when using the new integer dataset IDs




   climateserv.api.request_data(

       dataset_type, OperationType,

       EarliestDate, LatestDate, GeometryCoords,

       SeasonalEnsemble, SeasonalVariable, outfile

   )




# text on the page






#page title

#sub-heading. can also do st.subheader

#the * makes it italized, ** bold, *** both




#mess around with title size

st.markdown("<span style='font-size: 38px;'>**MyFarm**: *Connecting the Modern Farmer*</span>", unsafe_allow_html=True)

#st.markdown("<span style='font-size: 16px;'>Understand yearly climate and soil trends</span>", unsafe_allow_html=True)






# Input field for the address

address = st.text_input("Please enter your farm's address")




# Drop-down menu for selecting the data branch

#super basic foolproof

#databranch_options = [38, 39, 40]

#selected_databranch = st.selectbox(

 #  "I want to learn [38] Surface Soil Moisture, [39] Surface Soil Moisture Anomaly, [40] Subsurface Soil Moisture:",

#   options=databranch_options,

#   index=0  # Default selection (40)

#)

#trying to do so viewer only sees string

databranch_options = {

   "Surface Soil Moisture": 38,

   "Soil Moisture Anomaly": 39,

   "Subsurface Soil Moisture": 40

}




#get select box

selected_option = st.selectbox("I want to learn:", list(databranch_options.keys()))




#link user selection to database

selected_databranch = databranch_options[selected_option]




# Create a Folium map centered on a default location

default_location = [20, 0]

zoom_level = 2




if address:

   coordinates = get_coordinates(address)

   if coordinates:

       st.write(f"Coordinates for {address}: {coordinates}")

       # Update the map center and zoom level

       default_location = coordinates

       zoom_level = 14




       # Request ClimateSERV data

       x, y = coordinates[1], coordinates[0]

       outfile = 'out.csv'

       request_climateserv_data(x, y, selected_databranch, outfile)




       # Display the map with a marker

       world_map = folium.Map(location=default_location, zoom_start=zoom_level)

       folium.Marker(coordinates, popup=address).add_to(world_map)

       folium_static(world_map)




       # Display the CSV file content

       if os.path.exists(outfile):

           df = pd.read_csv(outfile)

           st.write("ClimateSERV Data:")

           st.dataframe(df)

       else:

           st.write("No data available for the specified location.")

   else:

       st.write("Address not found. Showing default location.")

else:

   # Display the default map

   world_map = folium.Map(location=default_location, zoom_start=zoom_level)

   folium_static(world_map)