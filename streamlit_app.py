import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favourites')

streamlit.text(' 🥣 Omega3 & blueberry Oatmeal')
streamlit.text('🥗 Kale')
streamlit.text(' 🐔 Chicken')
streamlit.text(' 🥑🍞 Avacado')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
