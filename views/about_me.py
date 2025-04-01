import streamlit as st

col1 = st.columns(1)[0]  # Unpack the single column
with col1:
    st.title("Charyyeva Maya", anchor=False)  # 'anchor' is not a valid parameter for st.title()
    st.write("A bored IT student that is trying to find her passion for coding again.")
