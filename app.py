import streamlit as st
import sidebar
import textPage
import homePage
# import audioPage
import imagePage
# import videoPage
# import twitterAnalysisPage

# st.title("Hello")
page = sidebar.show()

if page=="Home":
    homePage.renderPage()
elif page=="Text":
    textPage.renderPage()
# elif page=="Audio":
#     audioPage.renderPage()
#elif page=="IMDb movie reviews":
 #  imdbReviewsPage.renderPage()
elif page=="Image":
    imagePage.renderPage()
# elif page=="Video":
#     videoPage.main()
# elif page=="Twitter Data":
#     twitterAnalysisPage.renderPage()