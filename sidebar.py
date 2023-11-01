from pickle import FALSE
import streamlit as st
from streamlit_option_menu import option_menu

def show():
    with st.sidebar:
        st.markdown("""
                    # Applications
                    """, unsafe_allow_html = False)
        selected = option_menu(
            menu_title = None, #required
            # options = ["Text", "IMDb movie reviews", "Image", "Audio", "Video", "Twitter Data", "Web Scraping"], #required
            # icons = ["card-text", "film", "image", "mic", "camera-video", "twitter", "globe"], #optional
            
            options = ["Home", "Text",  "Image"], #,"IMDb movie reviews",], #required "IMDb movie reviews"
            icons = ["globe", "card-text", "image"], #"film"#optional
            
            # menu_icon="cast", #optional
            default_index = 0, #optional
        )
        return selected