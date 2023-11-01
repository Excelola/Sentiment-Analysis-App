#from emoji.unicode_codes import UNICODE_EMOJI
import streamlit as st
import streamlit.components.v1 as components
from textblob import TextBlob
from PIL import Image
import text2emotion as te
import plotly.graph_objects as go
import os
import mimetypes

# Function to check if a file has a valid text format
def is_valid_text_file(file):
    valid_extensions = {'.doc', '.docx', '.pdf', '.txt'}
    file_extension = os.path.splitext(file.name)[1]
    return file_extension.lower() in valid_extensions

# Function to process uploaded file content
def process_uploaded_file(file):
    file_content = file.read()
    user_text = file_content.decode("utf-8")
    return user_text

def plotPie(labels, values):
    fig = go.Figure(
        go.Pie(
        labels = labels,
        values = values,
        hoverinfo = "label+percent",
        textinfo = "value"
    ))
    st.plotly_chart(fig)

    
def getPolarity(userText):
    tb = TextBlob(userText)
    polarity = round(tb.polarity, 2)
    subjectivity = round(tb.subjectivity, 2)
    if polarity>0:
        return polarity, subjectivity, "Positive"
    elif polarity==0:
        return polarity, subjectivity, "Neutral"
    else:
        return polarity, subjectivity, "Negative"

def getSentiments(userText, type):
    if(type == 'Positive/Negative/Neutral - TextBlob'):
        polarity, subjectivity, status = getPolarity(userText)
        if(status=="Positive"):
            image = Image.open('./images/positive.PNG')
        elif(status == "Negative"):
            image = Image.open('./images/negative.PNG')
        else:
            image = Image.open('./images/neutral.PNG')
        col1, col2, col3 = st.columns(3)
        col1.metric("Polarity", polarity, None)
        col2.metric("Subjectivity", subjectivity, None)
        col3.metric("Result", status, None)
        st.image(image, caption=status)
    elif(type == 'Happy/Sad/Angry/Fear/Surprise - text2emotion'):
        emotion = dict(te.get_emotion(userText))
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("Happy 😊", emotion['Happy'], None)
        col2.metric("Sad 😔", emotion['Sad'], None)
        col3.metric("Angry 😠", emotion['Angry'], None)
        col4.metric("Fear 😨", emotion['Fear'], None)
        col5.metric("Surprise 😲", emotion['Surprise'], None)
        plotPie(list(emotion.keys()), list(emotion.values()))
        
def renderPage():
    st.title("Sentiment Analysis 😊😐😕😡")
    components.html("""<hr style="height:3px;border:none;color:#333;background-color:#333; margin-bottom: 10px" /> """)
    
    st.subheader("User Input Text Analysis")
    st.text("Analyzing text data given by the user and find sentiments within it.")
    st.text("")
    
    # Add a radio button to choose input method
    input_method = st.radio("Choose input method:", ("Upload a text-based file", "Enter text manually"))
    
    if input_method == "Upload a text-based file":
        uploaded_file = st.file_uploader("Upload a text-based file (doc, docx, pdf, txt)", type=["doc", "docx", "pdf", "txt"])
        
        if uploaded_file is not None:
            userText = process_uploaded_file(uploaded_file)
    else:
        userText = st.text_area("Enter text here:")
    
    st.text("")
    type = st.selectbox(
        'Type of analysis',
        ('Positive/Negative/Neutral - TextBlob', 'Happy/Sad/Angry/Fear/Surprise - text2emotion'))
    st.text("")
    if st.button('Predict'):
        if userText:
            st.text("")
            st.components.v1.html("""
                                <h3 style="color: #0284c7; font-family: Source Sans Pro, sans-serif; font-size: 28px; margin-bottom: 10px; margin-top: 50px;">Result</h3>
                                """, height=100)
            getSentiments(userText, type)

# Call the renderPage function to render the Streamlit page
if __name__ == '__main__':
    renderPage()