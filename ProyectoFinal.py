import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
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

st.map(dfDatos)

st.markdown("1. ¿Que tipo de alojamiento es el que mas hay (un cuarto, dept. completo, etc)?")
st.code("dfDatos.room_type.value_counts(normalize=True).plot.pie()", language="python")

image = Image.open('Pregunta1.jpg')
st.image(image, caption='Alojamientos',
         use_column_width=True)

st.text("2.¿Cuales son los neighbourhoods con mas alojamientos?")
st.code("sns.countplot(x=neighbourhood_group,data=dfDatos)plt.tight_layout()", language="python")

image = Image.open('Pregunta2.jpg')
st.image(image, caption='Neighbourhoods con mas alojamientos',
         use_column_width=True)

st.text("3.Mostrar los top 5 alojamientos, mas ocupados (tip la columna availability_365 muestra cuantos dias esta disponible)")
st.code("sns.countplot(x=name,data=dfDatos, order = dfDatos['name'].value_counts().iloc[:5].index)plt.tight_layout()", language="python")

image = Image.open('Pregunta3.jpg')
st.image(image, caption='Top 5 Alojamientos',
         use_column_width=True)

st.text("4.Mostrar el mismo dato del punto 3 pero filtrado por neighbourhood")
st.code("sns.countplot(x=neighbourhood,data=dfDatos, order = dfDatos['neighbourhood'].value_counts().iloc[:5].index)plt.tight_layout()",language="python")

image = Image.open('Pregunta4.jpg')
st.image(image, caption='Top 5 neighbourhood ',
         use_column_width=True)

st.text("5.Mostrar la distribución de los precios de los alojamientos.")
st.code("sns.barplot(x='room_type',y='price',data=dfDatos)", language="python")

image = Image.open('Pregunta5.jpg')
st.image(image, caption='Precios alojamientos',
         use_column_width=True)


st.text("6.¿Donde se encuentran los alojamientos mas caros / baratos?")
st.code("sns.barplot(x='neighbourhood_group',y='price',data=dfDatos)", language="python")

image = Image.open('Pregunta6.jpg')
st.image(image, caption='Alojamientos más',
         use_column_width=True)

st.text("7.Mostrar los alojamientos en un mapa, filtrados por neighbourhood y por precio ( usar un slider )")


st.text("8.¿El precio de renta afecta cuantas veces se renta un lugar?")
st.code("sns.jointplot(x=price,y='calculated_host_listings_count',data=dfDatos)", language="python")

image = Image.open('Pregunta8.jpg')
st.image(image, caption='Renta vs precio',
         use_column_width=True)

st.text("9.¿El número de reviews afecta cuantas veces se renta un lugar?")
st.code("sns.jointplot(x=price,y='calculated_host_listings_count',data=dfDatos)", language="python")

image = Image.open('Pregunta9.jpg')
st.image(image, caption='Review vs renta',
         use_column_width=True)
        
st.code("st.code(sns.jointplot(x=price,y='calculated_host_listings_count',data=dfDatos)",language="python")

image = Image.open('Pregunta89.jpg')
st.image(image, caption='Comparación general',
         use_column_width=True)

st.text("10.¿El neighbourhood influye en cuantas veces se renta un lugar?")
st.code("sns.barplot(x='neighbourhood_group',y='calculated_host_listings_count',data=dfDatos)", language="python")

image = Image.open('Pregunta10.jpg')
st.image(image, caption='Neighbourhood vs renta',
         use_column_width=True)

