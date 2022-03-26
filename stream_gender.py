from cProfile import label
from turtle import width
import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px
from difflib import get_close_matches
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt
df =pd.read_csv('https://raw.githubusercontent.com/chriswmann/datasets/master/500_Person_Gender_Height_Weight_Index.csv')

df1 = df[df["Gender"] == 'Male']
df2 = df[df["Gender"] == 'Female']

if 'Height' == 'Height':
    print(df1['Height'].head())

st.title('Comparison male and female body sizes')
st.header('Compare your weight and height with others')
st.subheader('Good Luck!')
st.write('Have a fun!')
img = Image.open("weakness.png")
st.image(img, width = 700, caption="Action Image")
status = st.sidebar.radio('What is your Gender?',('Male','Female'))
select_classifier = st.sidebar.selectbox('Select your body type!',('Extremely Weak', 'Weak', 'Normal', 'Overweight', 'Obesity', 'Extremely Obesity'))
plt.pie(df)


if status == 'Male':
    if select_classifier == 'Weak':







    st.success('You are male')
else:
    st.warning('You are female')    

    
st.write(select_classifier)
# data_set=st.sidebar.selectbox('select your height',('James Cameron', 'David Fincher', 'George Miller','Pierre Morel'))
# st.write(data_set)
level = st.sidebar.slider('Choose your height', 140,199)



# vid_file = open("file.mp4","rb").read()
# st.video(vid_file)