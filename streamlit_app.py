import streamlit as st

#page setup
initial_pg = st.Page(
    page = "views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
) 
pg1 = st.Page(
    page = "views/purpose.py",
    title="Purpose",
    icon=":material/photo:",
) 

pg2 = st.Page(
    page = "views/memories.py",
    title="Memories",
    icon=":material/lightbulb:",
) 

#navigation setup
pg = st.navigation(pages=[initial_pg, pg1, pg2])

pg.run()