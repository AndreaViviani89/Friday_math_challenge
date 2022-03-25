import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

###

# full csv
df = pd.read_csv("https://raw.githubusercontent.com/chriswmann/datasets/master/500_Person_Gender_Height_Weight_Index.csv")
st.title("Body Mass Index of different individuals")
st.write(df)


# 1 graph

df.groupby('Gender')['Index'].value_counts().plot(kind='bar')
st.pyplot()

# 2 graph
plt.scatter(df['Weight'], df['Height'], c=df.Index )
st.pyplot()


# 3 graph
plt.figure(figsize=(15,8))
sns.scatterplot(x='Weight', y='Height', hue='Index', data=df ,palette="deep")
plt.scatter(df.Weight.mean(),df.Height.mean(),color='r', marker='o')
plt.show()
st.pyplot()


# 4 graph
male_height = df[df.Gender == 'Male'].Height
male_weight = df[df.Gender == 'Male'].Weight

plt.scatter(male_weight, male_height, c=male_weight.index)
plt.scatter(df.Weight.mean(),df.Height.mean(),color='r', marker='o')
st.pyplot()

# 5 graph

female_height = df[df.Gender == 'Female'].Height
female_weight = df[df.Gender == 'Female'].Weight

plt.scatter(female_weight, female_height, c=female_weight.index)
plt.scatter(df.Weight.mean(),df.Height.mean(),color='r', marker='o')
st.pyplot()


#6 graph

plt.hist(male_height)
plt.grid(True, linestyle='--', linewidth = 1)
plt.title('Males height', color='White')
st.pyplot()

plt.hist(male_weight)
plt.grid(True, linestyle='--', linewidth = 1)
plt.title('Males weight', color='White')
st.pyplot()

# 7 graph



# st.bar_chart(df['Gender'].groupby('Index').value_counts())



# Actor csv
# df_actor = pd.read_csv("C:/Users/andre/Documents/Strive_repository/IMDB_challenge/data_imdb_actors_name.csv")
# st.title("Best Actors")
# st.write(df_actor)

# df_min_max_scaled = df.copy()

# column = 'Rating'
# column1 = 'Duration'

# df_min_max_scaled[column, column1] = (df_min_max_scaled[column] - df_min_max_scaled[column].min()) / (df_min_max_scaled[column].max() - df_min_max_scaled[column].min()) / (df_min_max_scaled[column1] - df_min_max_scaled[column1].min()) / (df_min_max_scaled[column1].max() - df_min_max_scaled[column1].min())

# st.header("Ratings of movies by year")
# st.bar_chart(df[['Release', 'Rating']].groupby('Release').mean())

# st.header("Best directors in Action Movies")
# st.bar_chart(df['Director'].value_counts().nlargest(5))

# st.header("Best Actor in Action Movies")
# st.bar_chart(df["Stars"].value_counts().nlargest(10))



# st.write("line chart")
# st.line_chart(df[["Title"]])

# st.write("area chart")
# st.area_chart(df["Rating"])




# fig, ax = plt.subplots()
# df.hist(
#     bins=8,
#     column="Rating",
#     grid=False,
#     figsize=(8, 8),
#     color="#86bf91",
#     zorder=2,
#     rwidth=0.9,
#     ax=ax,
#   )
# st.write(fig)