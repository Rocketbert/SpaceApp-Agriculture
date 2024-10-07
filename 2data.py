
import streamlit as st

import folium

from streamlit_folium import folium_static

from geopy.geocoders import Nominatim

from geopy.exc import GeocoderServiceError

from geopy.exc import GeocoderTimedOut

import pandas as pd

import climateserv

import os

import plotly.express as px

import plotly.graph_objects as go

import math

def create_report(climate_data, option):

       """Generate a text report based on climate data."""

       report_lines = []




       report_lines.append(f"# Climate Data Report for {option}\n")

       report_lines.append(f"Based on your farm's location, the precipitation data shows how to water your crops more efficiently.\n")

       report_lines.append(f"Contact an expert for more information!\n")

       watering_data=climate_data

       watering_data['avg']=wtarget- climate_data['avg']

       watering_data['avg']=[0 if x < 0 else x for x in climate_data['avg']]




       report_lines.append(f" \n")

       separate_fig= go.Figure()




       separate_fig.add_scatter(

       x=watering_data['date'],

       y=watering_data[climate_data.columns[1]],  # Data to plot

       mode='lines+markers',

       name=option

   )




   # Update layout for the separate graph

       separate_fig.update_layout(

       title='This is the watering plan asscribed based on your farm requirements:',

       xaxis_title='Date',

       yaxis_title='Values',

       xaxis=dict(tickformat='%b %d', tickangle=45),

       template='plotly'

   )

   

       st.plotly_chart(separate_fig, key="a")  # Embed the Plotly chart into the webpage

       report_lines.append(f"\n## Observations\n")

       

       savep=math.floor((1-watering_data['avg'].sum()/(wtarget*len(watering_data)))*100)

       report_lines.append(f"Analysis of trends for {option} over the given period show you can save around ***{savep}%***")






       return "\n".join(report_lines)  # Join the report lines into a single string

# Function to request climate data

def request_climate_data(lat, lon, option):

   GeometryCoords = [[lon-.01, lat+.01], [lon+.01, lat+.01],

                     [lon+.01, lat-.01], [lon-.01, lat-.01], [lon-.01, lat+.01]]

   if option == "Soil Moisture":

       DatasetType = 38

   elif option == "Precipitation":

       DatasetType = 90

   elif option == "Drought Risk":

       DatasetType = 41

   OperationType = 'Average'

   EarliestDate = '01/01/2016'

   LatestDate = '12/31/2016'

   SeasonalEnsemble = ''

   SeasonalVariable = ''

   Outfile = 'out.csv'




   # Reset CSV file

   if os.path.exists(Outfile):

       os.remove(Outfile)




   climateserv.api.request_data(DatasetType, OperationType,

                                EarliestDate, LatestDate, GeometryCoords,

                                SeasonalEnsemble, SeasonalVariable, Outfile)




   data = pd.read_csv(Outfile, skiprows=1)

   return data




# Streamlit app

st.title('Interactive Map with Climate Data')




# Add a dropdown menu

option = st.selectbox(

   'Select an option',

   ('Soil Moisture', 'Precipitation', 'Drought Risk')

)

wtarget=st.number_input('Average water used in a day (mm)')

st.markdown(

   """

   <style>

   .wrapped-text-box {

       border: 1px solid #ccc;

       padding: 10px;

       border-radius: 4px;

       background-color: #f9f9f9;

       white-space: pre-wrap;

       word-wrap: break-word;

       overflow-wrap: break-word;

   }

   </style>

   """,

   unsafe_allow_html=True,

)






# Address input

address = st.text_input('Enter an address:')

if address:

   geolocator = Nominatim(user_agent="abcd")

   try:

       location = geolocator.geocode(address, timeout=10)

       if location:

           lat = location.latitude

           lon = location.longitude

           st.write(f"Latitude: {lat}, Longitude: {lon}")




           # Display Folium map

           m = folium.Map(location=[lat, lon], zoom_start=10)

           folium.Marker([lat, lon], tooltip=address).add_to(m)

           folium_static(m)




           # Request climate data

           climate_data = request_climate_data(lat, lon, option)

           st.write('Climate Data:')

           st.dataframe(climate_data)




   

           if 'date' in climate_data.columns:

               # Rename the 'Date' column to 'date'

               climate_data.rename(columns={'Date': 'date'}, inplace=True)

               climate_data['date'] = pd.to_datetime(climate_data['date'])

               sem=0

               fig=go.Figure()

               for year in climate_data['date'].dt.year.unique():

                   year_data = climate_data[climate_data['date'].dt.year == year]

                   fig.add_scatter(x=year_data['date'].dt.date, y=year_data[year_data.columns[1]], mode='lines+markers', name=str(year))






               # Update layout

               fig.update_layout(

                   title=f'{option} Timeseries by Year:',

                   xaxis_title='date',

                   yaxis_title=option,

                   xaxis=dict(tickformat='%b %d', tickangle=45),  # Format and angle for better visibility

                   legend_title='Year',

                   template='plotly',

               )




               st.plotly_chart(fig, key="unique_key_1")  # Embed the Plotly chart into the webpage

               if(option == 'Soil Moisture'):

                   report = create_report(climate_data, option)

                   st.subheader('Generated Report')

                   st.markdown(report)  # Display the report as markdown

               elif(option=='Drought Risk'):

                    st.text(f"Drought Risk is given by the surface soil moisture anomaly of a given year.\n")

                    st.text(f"This means that the higher the number, the more likely it is for your\n")

                    st.text(f"farm to experience drought conditions.\n")




                    

               elif(option=="Precipitation"):

                    st.text(f"Precipitation data shows amount of water fall in a given area.\n")




       else:

           st.error('Address not found.')




   




   except GeocoderTimedOut:

       st.error("Geocoding service timed out. Please try again.")

   except GeocoderServiceError as e:

       st.error(f"Geocoding service error: {e}")

