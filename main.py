# Libs
import streamlit as st


# Set page title and favicon
st.set_page_config(page_title = 'INF-0047 Cloud Based AI', page_icon = "", layout="wide", initial_sidebar_state="expanded")

PAGES = [
    "About the Project",
    "About me"
    ]

def main():
    
    # Dashboard
    abstract_text = st.markdown(get_file_content_as_string("markdowns/abstract_p0.md"))

    # Add an app mode in the sidebar.
    st.sidebar.title("Explore Around")

    app_mode = st.sidebar.radio('Navigation', PAGES)
    
    
    if app_mode == 'About the Project':
        abstract_text.empty()
        st.markdown(get_file_content_as_string("markdowns/About the Project.md"))

    elif app_mode == 'About me':
        abstract_text.empty()
        st.markdown(get_file_content_as_string("markdowns/About me.md"))


def get_file_content_as_string(path):
    with open(path, "r", encoding="utf-8") as input_file:
        text = input_file.read()
    return text


if __name__ == '__main__':
    main()