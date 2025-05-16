# Web.py
import streamlit as st
import sys
import os
import wikipediaapi

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from stats import correlation
from stats import dispersion
from stats import central_tendency
from stats import visualization

# Function to display the homepage content
def show_homepage():
    st.title('Homepage')
    
    st.write("Made by: Ferdinand, Frederik, Jonas and Daniel")

def show_wine_quality():
    st.header("Wine Quality Information")

    # Set up Wikipedia API with proper user agent
    wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        user_agent='WineQualityApp/1.0 (ferdinand.a.vestergaard@gmail.com)'  
    )

    # Get the Wikipedia page for Wine
    wine_page = wiki_wiki.page("Wine")

    # Check if the page exists and display content
    if wine_page.exists():
        st.subheader("Summary from Wikipedia")
        st.write(wine_page.summary)

        st.subheader("Watch a related video on Wine Quality")
        st.video("https://www.youtube.com/watch?v=ZSZt4QD3eXk")  
    else:
        st.error("Could not fetch information from Wikipedia.")

# Main function that runs the app
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Choose a page", ["Homepage", "Visualization", "Wine Quality"])

    if page == "Homepage":
        show_homepage()
    elif page == "Visualization":
        visualization.show_graphs()
    elif page == "Wine Quality":
        show_wine_quality()

if __name__ == "__main__":
    main()
