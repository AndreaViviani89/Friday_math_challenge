import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.express as px


header = st.container()
dataset = st.container()


with header:
    st.title('Nutrition Challenge')
    st.markdown('*Member of the team:*')
    st.text('Andrea')
    st.text('Eunice')
    st.text('Islom')

    df = pd.read_csv("https://raw.githubusercontent.com/chriswmann/datasets/master/500_Person_Gender_Height_Weight_Index.csv")
    # st.write(df)

with dataset:
    st.header('About Data')

    # Information about gender
    st.subheader('Gender')
    Gender = pd.DataFrame(df['Gender'].value_counts())
    st.bar_chart(Gender)
    st.text('Our sample consists of 500 subjects, with 255 females and 245 males')

    # Information about height
    st.subheader('Information about Height')
    histo = pd.DataFrame(df['Height'].value_counts())
    st.bar_chart(histo)

    # Information about weight
    st.subheader('Information about Weight')
    histo = pd.DataFrame(df['Weight'].value_counts())
    st.bar_chart(histo)

    st.subheader('Comparison Weight and Height')
    plot = px.scatter(data_frame = df, x =df['Weight'], y=df['Height'], color= "Index")
    st.plotly_chart(plot)


    # BMI
    st.subheader('Body Mass Index')
    st.markdown('* **0 mean** - Extremely Weak')
    st.markdown('* **1 mean** - Weak')
    st.markdown('* **2 mean** - Normal')
    st.markdown('* **3 mean** - Overweight')
    st.markdown('* **4 mean** - Obesity')
    st.markdown('* **5 mean** - Extreme Obesity')

    # Information about BMI sorted by number of people
    st.subheader('BMI - sorted by number of people')
    index = pd.DataFrame(df['Index'].value_counts())
    st.bar_chart(index)

    # Information about BMI sorted by female
    df_female = df[df.Gender == "Female"]
    st.subheader('BMI - sorted by Female')
    go = pd.DataFrame(df_female['Index'].value_counts())
    st.bar_chart(go)

    # Information about BMI sorted by male
    df_male = df[df.Gender == "Male"]
    st.subheader('BMI - sorted by Male')
    index = pd.DataFrame(df_male['Index'].value_counts())
    st.bar_chart(index)

    st.subheader('BMI Comparison')
    fig = px.scatter(df, x = 'Weight', y = 'Height', size='Index',color='Index', hover_name='Index')
    st.write(fig)
    

    st.subheader('Lets do it interactive!')
    weight_option = df['Index'].unique().tolist()
    weight = st.multiselect('Choose a number', weight_option)
    df = df[df['Index'].isin(weight)]
    fig = px.scatter(df, x = 'Weight', y = 'Height', size='Index', hover_name='Index')
    st.write(fig)


