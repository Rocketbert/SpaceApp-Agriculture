
import folium

from streamlit_folium import folium_static

import streamlit as st

from geopy.geocoders import Nominatim

from geopy.exc import GeocoderTimedOut

import climateserv

import pandas as pd

import os




#title part

st.markdown("<div style='text-align: center;'><span style='font-size: 38px;'><em><strong>MyFarm<strong><em>: <em>empowering the everyday<em></span>", unsafe_allow_html=True)

st.markdown("<div style='text-align: center;'><span style='font-size: 38px;'>🚜</span></div>", unsafe_allow_html=True)




##little writeup

st.write("""American farming is a majority family-run industry. In 2021, the USDA found that 98% of farms were family-run,

        with 89% of farms also being small-scale operations (referring to farms with a gross profit under $250,000/year).

       The farm industry does not offer much financial stability, with 73.2% of all farms considered high risk, with less

       than 10% of their income considered profit (known as the “red zone”). Over the past decade, the percentage of small

       farms operating in the red zone has been steadily rising.""")

st.markdown(

   "<div style='text-align: center;'><span style='font-size: 24px;'><em>With production costs ever rising, farmers are occasionally selling their crops for less than it cost to produce them.</em></span></div>",

   unsafe_allow_html=True)

st.write("")

st.write("""With production costs ever rising (especially fertilizer, seed prices, labor costs), farmers are occasionally selling

        their crops for less than it cost to produce them. Severe weather events, increasingly unpredictable with climate change,

        exacerbate this issue. Thousands of farms have ceased operations, with the US Department of Agriculture estimating that the

       farm sector’s debt is set to rise to a whopping $540.8 billion in 2024. Farmer deaths by suicide and other mental health

        struggles have been a large issue since the 1980s, with the CDC reporting the Agricultural industry to have the fourth highest

        rates of suicide among all occupations.""") 

st.markdown(

   "<div style='text-align: center;'><span style='font-size: 24px;'><em>A one-stop resource hub for farmers: How to use.</em></span></div>",

   unsafe_allow_html=True)

st.write("")

st.write("""This is an incredibly nuanced issue with no quick solution. We hope to provide a one-stop hub to connect farmers to relevant data and other resources.

        Navigate to the "Data" tab to view personalized statistics for your farm including soil moisture, precipitation, and drought risk.

        Navigate to the "Resources" tab to be connected with government assistance, understand NASA data, and view useful hotlines.""")




#add a little banner pic

image_path = '/Users/ashleyashiku/Desktop/SPACE APPS/green.webp' 

#image size

image_width = 350

col1, col2, col3 = st.columns([1, 3, 1])  # Adjust the numbers for column width ratio




with col2:  # This will be the center column

   st.image(image_path, use_column_width=True)
