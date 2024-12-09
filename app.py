import streamlit as st
from streamlit_extras.row import row
import os

st.set_page_config(
    page_title='ROI GKE Demo App',
    page_icon='./static/logo-64.png',
)

pod_name = os.getenv('POD_NAME', 'unknown')
node_name = os.getenv('NODE_NAME', 'unknown')
pod_ip = os.getenv('POD_IP', 'unknown')

content = """
<style>
    .centered-container {
        text-align: center;
        margin: 0 auto;
    }
    .centered-image {
        max-width: 100%;
        height: auto;
    }
    .centered-text {
        font-size: 40px;
        font-weight: bold;
    }
</style>

<div class="centered-container">
    <img src="app/static/art.png" class="centered-image" width="400px">
    <div class="centered-text">
        We love GKE!
    <div>
    <div class="centered-text small">
</div>
"""

with st.sidebar:
    st.subheader('App Info')
    r1 = row([0.4, 0.6], vertical_align='top')
    r1.write('Pod Name:')
    r1.write(pod_name)

    r2 = row([0.4, 0.6], vertical_align='top')
    r2.write('Pod IP:')
    r2.write(pod_ip)

    r3 = row([0.4, 0.6], vertical_align='top')
    r3.write('Node Name:')
    r3.write(node_name)

st.html(content)
