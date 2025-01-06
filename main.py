import streamlit as st
from scrape import (
    scrape_website,
    split_dom_content,
    clean_body_content,
    extract_body_content,
    )

st.title('AI Web Scraper')

url =st.text_input('Enter Website URL')

if st.button('Scrape Site'):

    result =scrape_website(url)

    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander('View Dom Content'):  
        st.text_area("DOM Content",cleaned_content, height=500)

if "dom_content" in st.session_state:
    parse_description= st.text_area("What you want to parse")

    if st.button('Parse Content'):
        if parse_description:
            st.write("Parsing Content...")

            dom_chunks= split_dom_content(st.session_state.dom_content)
