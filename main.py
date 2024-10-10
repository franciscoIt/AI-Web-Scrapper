import streamlit as st
from scrape import (
    scrape_website,
    split_dom,
    clean_body,
    extract_body
)
from parse import parse_with_ollama
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Title of the app
st.title("AI Web Scraper")

# Input field for the URL
url = st.text_input("Enter the Website URL:", placeholder="https://www.linkedin.com/in/yo-enlared")

# Scraping the website when button is clicked
if st.button("Scrape Site"):
    if url:
        st.write("Scraping the website...")

        # Display loading spinner while scraping
        with st.spinner("Scraping in progress..."):
            try:
                result = scrape_website(url)
                body_content = extract_body(result)
                cleaned_content = clean_body(body_content)

                # Store cleaned content in session state
                st.session_state.dom_content = cleaned_content

                st.success("Website scraped successfully!")

                # Display the DOM content in an expander
                with st.expander("View DOM Content"):
                    st.text_area("DOM Content", cleaned_content, height=300)

            except Exception as e:
                st.error(f"Error scraping the website: ¿Website exists?")
                logger.error(e)
    else:
        st.error("Please enter a valid URL.")

# If DOM content is available in session state, allow parsing
if "dom_content" in st.session_state:
    # Input field for the parsing description
    parse_description = st.text_area(
        "Describe what you want to parse:", 
        placeholder="Enter the specific data you want to extract"
    )

    # Parse the content when button is clicked
    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")

            # Display loading spinner while parsing
            with st.spinner("Parsing in progress..."):
                try:
                    dom_chunks = split_dom(st.session_state.dom_content)
                    result = parse_with_ollama(dom_chunks, parse_description)

                    # Display the parsed result
                    with st.expander("Parsed Content"):
                        st.text_area("Parsed Result", result, height=300)

                except Exception as e:
                    st.error(f"Error parsing content: ")
                    logger.error(e)
        else:
            st.error("Please enter a description for parsing.")
