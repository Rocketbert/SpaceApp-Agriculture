
import folium

from streamlit_folium import folium_static

import streamlit as st

from geopy.geocoders import Nominatim

from geopy.exc import GeocoderTimedOut

import climateserv

import pandas as pd

import os




#GOVERNMENT/NASA RESOURCES

st.markdown("<div style='text-align: center;'><span style='font-size: 38px;'><em><strong>MyFarm<strong><em>: <em>Resources Page<em></span>", unsafe_allow_html=True)

st.markdown("<div style='text-align: center;'><span style='font-size: 38px;'>🌾</span></div>", unsafe_allow_html=True)

st.markdown("***NASA and Government Resources***")

st.markdown("- [U.S. Drought Monitor:](https://droughtmonitor.unl.edu) Powered by NASA satellite data, this resource is updated every Tuesday at 8:30am EST")

st.markdown("- [Your Local Farmers' Dashboard (USDA):](https://www.farmers.gov/dashboard) View crop prices, current weather, and other agricultural news in your county.")

st.markdown("- [Soil Moisture Data Map:](https://nassgeo.csiss.gmu.edu/CropCASMA/) View a map of soil moisture across the entire US, powered by NASA’s Soil Moisture Active Passive (SMAP) mission and the Moderate Resolution Imaging Spectroradiometer (MODIS).")




#POLICY INFO

#st.markdown("***Relevant Policy Information***")

#st.markdown("- The Farm Bill")

#educate on policy. insurance. are there specific policies that they qualify for??




#farmer suicide hotline

st.markdown("***Hotlines***")

st.markdown("*If you or someone you know may be contemplating suicide, call the National Suicide Prevention Lifeline at 1-800-273-8255 or text HOME to 741741 to reach the Crisis Text Line.*")

