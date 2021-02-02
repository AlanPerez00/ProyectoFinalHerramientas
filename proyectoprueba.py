import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
#from plotly.subplots import make subplots
import plotly.graph_objects as go
from PIL import Image


#Título
st.title("Proyecto Final Airbnb")

#header
st.header("Semestre Sep-Enero 2021")

#Texto
st.text("Herramientas para el análisis de datos")

@st.cache  # Para que los datos solo se descarguen una vez
def get_data():
    url = "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-09-12/visualisations/listings.csv"
    return pd.read_csv(url)

st.markdown("Datos del dataframe")

dfDatos = get_data()

dfDatos = st.dataframe(dfDatos.drop(columns=['id', 'host_id', 'host_name', 'latitude', 'longitude', 'minimum_nights', 
                                'last_review', 'reviews_per_month']))

st.markdown("1. ¿Que tipo de alojamiento es el que mas hay (un cuarto, dept. completo, etc)?")
st.code("dfDatos.room_type.value_counts(normalize=True).plot.pie()", language="python")

st.dataframe(dfDatos["room_type"].value_counts())

st.text("2.¿Cuales son los neighbourhoods con mas alojamientos?")
st.code("sns.countplot(x=neighbourhood_group,data=dfDatos)plt.tight_layout()", language="python")

st.text("3.Mostrar los top 5 alojamientos, mas ocupados (tip la columna availability_365 muestra cuantos dias esta disponible)")
st.code("sns.countplot(x=name,data=dfDatos, order = dfDatos['name'].value_counts().iloc[:5].index)plt.tight_layout()", language="python")

st.text("4.Mostrar el mismo dato del punto 3 pero filtrado por neighbourhood")
st.code("sns.countplot(x=neighbourhood,data=dfDatos, order = dfDatos['neighbourhood'].value_counts().iloc[:5].index)plt.tight_layout()",language="python")

st.text("5.Mostrar la distribución de los precios de los alojamientos.")
st.code("sns.barplot(x='room_type',y='price',data=dfDatos)", language="python")


st.text("6.¿Donde se encuentran los alojamientos mas caros / baratos?")
st.code("sns.barplot(x='neighbourhood_group',y='price',data=dfDatos)", language="python")

st.text("7.Mostrar los alojamientos en un mapa, filtrados por neighbourhood y por precio ( usar un slider )")


st.text("8.¿El precio de renta afecta cuantas veces se renta un lugar?")
st.code("sns.jointplot(x=price,y='calculated_host_listings_count',data=dfDatos)", language="python")

st.text("9.¿El número de reviews afecta cuantas veces se renta un lugar?")
st.code("sns.jointplot(x=price,y='calculated_host_listings_count',data=dfDatos)", language="python")
        
st.code("st.code(sns.jointplot(x=price,y='calculated_host_listings_count',data=dfDatos)",language="python")

st.text("10.¿El neighbourhood influye en cuantas veces se renta un lugar?")
st.code("sns.barplot(x='neighbourhood_group',y='calculated_host_listings_count',data=dfDatos)", language="python")