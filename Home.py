import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/lol.jpg")

    with col2:
        st.title("Joshua Van Diepen")
        content = """Hi im Joshua van diepen! I am learning to use python and make website`s and programs.
                   im also learning to make websites with visual code.
                   and to be honest its a lot to learn but its fun.
                   at the time of writing this i am 19 years old
                   i was born on 22-09-2005.
                   that's about all there is to know about me."""

        st.info(content)

content2 = """
Below you can find some of the apps i have build
"""

st.write(content2)

col3, empty_col,  col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
