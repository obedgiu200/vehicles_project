import pandas as pd 
import streamlit as st
import plotly.express as px

data=pd.read_csv('vehicles_us.csv')


st.title ('BUY YOUR BEST CAR!')
st.subheader('Use this App to select your best car')




st.caption('red[choose your parameters here]')
price = st.slider(
     'What is your price?',
     value=(1,375000))

actual_range=list(range(price[0],price[1]+1))
high_pricing = st.checkbox('high pricing')

if high_pricing:
    filtered_data=[data.price.isin(actual_range)]
    filtered_data=filtered_data[data.price>=250000]
else:
    filtered_data=[data.price.isin(actual_range)]


st.write('Here are your options with split by type')

fig = px.scatter(filtered_data, x='type',y='price')
st.plotly_chart(fig)

st.write('Determine the condition of filtered vehicles')

fig2 = px.histogram(filtered_data, x='condition', y='price')
st.plotly_chart(fig2)

