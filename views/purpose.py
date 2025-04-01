import streamlit as st

col1 = st.columns(1)[0]  # Unpack the single column
with col1:
    st.title("Purpose of this website:", anchor=False)  # 'anchor' is not a valid parameter for st.title()
    st.write("I though it would be cool to have a website where we all upload our memories together.")
