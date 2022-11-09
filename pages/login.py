from sqlalchemy import null
import streamlit as st

import json
import requests

# Create an empty container
placeholder = st.empty()

def switch_page(page_name):
    from streamlit import _RerunData, _RerunException
    from streamlit.source_util import get_pages

    def standardize_name(name: str) -> str:
        return name.lower().replace("_", " ")
    
    page_name = standardize_name(page_name)

    pages = get_pages("streamlit_app.py")

    for page_hash, config in pages.items():
        if standardize_name(config["page_name"]) == page_name:
            raise _RerunException(
                _RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
                )
            )

    page_names = [standardize_name(config["page_name"]) for config in pages.values()]

    raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")

# Insert a form in the container
with placeholder.form("login"):
    st.markdown("#### Enter your credentials")
    email = st.text_input("Id")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")

if submit :

    url = 'http://localhost:3000/users/login'
    myobj = {'user_id': email, 'password': password}

    x = requests.post(url, json = myobj)

    if x is not null:
        print(x.text)
        resp = json.loads(x.text)

        if resp is not null:
            if resp["message"] == "Authentication success":
                switch_page("sentimenanalisis")
            else:
                email = ""
                password = ""

                st.error("Login failed")