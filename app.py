import pandas as pd 
import streamlit as st
import plotly.express as px

data=pd.read_csv('vehicles_us.csv')


st.title ('BUY YOUR BEST CAR!')
st.subheader('Use this App to select your best car')




st.caption('blue[choose your parameters here]')
price_range = st.slider(
     'What is your price range?',
     value=(1,375000))

actual_range=list(range(price_range[0],price_range[1]+1))

high_rating = st.checkbox('only high rating')

if high_rating:
    filtered_data=[data.price.isin(actual_range)]
    filtered_data=filtered_data[data.rating>=4.5]
else:
    filtered_data=data[data.price.isin(actual_range)]

st.write('Here are your options with split by type and model')


fig = px.scatter(filtered_data, x="type", y="model")
st.plotly_chart(fig)

st.write('Determine the condition of filtered vehicles')

fig2 = px.histogram(filtered_data, x='condition', y='price')
st.plotly_chart(fig2)

