import streamlit as st

from home import home
from blazepose import blazepose
from PIL import Image

icon = Image.open("images/icon.jpg")
st.set_page_config(
    page_title="REAL TIME HUMAN POSE ESTIMATION:",
    page_icon=icon,
    layout="wide",
    initial_sidebar_state="auto",
)

st.sidebar.markdown(
    "<h1 style='color:Red ;'>Navigation</h1>", unsafe_allow_html=True)
page = st.sidebar.radio(" ", ("Home", "BlazePose"))

if page == "BlazePose":
    blazepose()
else:
    home()
