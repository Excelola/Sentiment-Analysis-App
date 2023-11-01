import streamlit as st

def renderPage():
    st.title("Empowering User Experience with Integrated Sentiment Visualization 😊😐😔😡")

    # Introduction section
    st.header("About")
    st.markdown("A sentiment analysis application built using Streamlit (An open-source framework to build web applications in Python).")
    st.markdown("Sentiment Analysis is one of the most famous applications of Natural Language Processing. It applies to all types of data, from text to audio to video to image. Data in any form can be processed to get sentiments out of it. The objective of the project is to create a web application that will harbor all sorts of applications in the field of sentiment analysis from applying it on text to analyzing images.")

    # Author's name and project purpose
    st.header("Author")
    st.markdown("This project was created by **Olaoluwa Folorunso**.")
    st.markdown("The purpose of this project is to demonstrate the capabilities of sentiment analysis using various natural language processing libraries and APIs.")

    # Project Specifications
    st.header("Project Specifications")
    st.markdown("Below are the libraries and frameworks used to create the project:")
    st.markdown("- **Web Framework** :- Streamlit")
    st.markdown("- **Graphs and Images** :- PIL, plotly, cv2")
    st.markdown("- **Libraries for sentiment analysis** :- textblob, nltk(vader), flair, text2emotion, fer")
    st.markdown("- **Libraries for API requests** :- requests, json")

    # Project Components
    st.header("Project Components")
    st.markdown("The project currently contains 2 applications:")
    st.markdown("1. **Text** - Applying sentiment analysis on text given by the user.")
    st.markdown("2. **Image** - Here we analyze sentiments out of an image uploaded by the user. We detect faces and then analyze sentiments for each. We also calculate the sentiment of the image as a whole.")

    # Models used
    st.header("Models used")
    st.markdown("There are multiple libraries available in Python for sentiment analysis. Let's see them below:")
    st.markdown("- **TextBlob** - TextBlob is a Python library for processing textual data. It provides a simple API for diving into common (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.")
    st.markdown("- **Flair** - A very simple framework for state-of-the-art NLP. It is a powerful NLP library that allows you to apply state-of-the-art natural language processing (NLP) models to your text, such as named entity recognition (NER), part-of-speech tagging (PoS), etc.")
    st.markdown("- **Vader** - VADER (Valence Aware Dictionary and Sentiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media.")
    st.markdown("- **text2emotion** - text2emotion is the python package that will help you to extract the emotions from the content. It processes any textual message and recognizes the emotions embedded in it. It is compatible with 5 different emotion categories as Happy, Angry, Sad, Surprise, and Fear.")
    st.markdown("**Note :-**")
    st.markdown("1. textblob, flair, and vader provide polarity score where text is declared in either of 3 states (POSITIVE🙂, NEGATIVE☹️, NEUTRAL😐)")
    st.markdown("2. text2emotion is the only library among the others mentioned above which can classify text in 5 emotion categories (HAPPY😊, ANGRY😡, SAD😔, SURPRISE😲, FEAR😨)")

    # Future Development
    st.header("Project development ideas")
    st.markdown("Below mentioned applications can be implemented as a future scope -")
    st.markdown("- Tweets analysis using Twitter API")
    st.markdown("- Sentiment analysis on Live video streaming")
    st.markdown("- Sentiment analysis of Audio data")
    st.markdown("- Sentiment analysis of data received from the site given by the user using web scraping in Python.")

    # Thank You!
    st.header("Thank You!")
    st.markdown("Thank you. **I hope you liked the project**.")

# Run the application
if __name__ == "__main__":
    renderPage()
