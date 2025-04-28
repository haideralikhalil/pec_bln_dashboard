import streamlit as st
import streamlit.components.v1 as components


def call_phone(phone_number):
    # Method 1: Using markdown with HTML
    st.markdown(f"""
    <a href="tel:{phone_number}">
        <button style="padding: 5px 5px; border: none; border-radius: 5px; font-size: 16px;">
        :iphone: {phone_number}
        </button>
    </a>
    """, unsafe_allow_html=True)

def call_phone01(phone_number):
    # Method 1: Using markdown with HTML
    st.markdown(f"""
    <a href="tel:{phone_number}">
        <button style="background-color: #25D366; color: white; padding: 10px 20px; border: none; border-radius: 5px; font-size: 16px;">
            Call: {phone_number}
        </button>
    </a>
    """, unsafe_allow_html=True)
