import streamlit as st


def header_home():

    logo_url = "https://www.cusb.ac.in/images/cusb/logo-new3.png"
    
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <img src='{logo_url}' style='height:100px;' />
            <h2 style='text-align:center; color:blue'>BIOMETRIC<br/>ATTENDANCE</h2>
        </div>   
                
                """, unsafe_allow_html=True)


def header_dashboard():

    logo_url = "https://i.postimg.cc/ns0tTVSc/2ef8d8a9ca04ef0bbb423f634b2d88ed.png"
    
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src='{logo_url}' style='height:85px;' />
            <h3 style='text-align:left; color:#5865F2'>BIOMETRIC<br/>ATTENDANCE</h3>
        </div>   
                
                """, unsafe_allow_html=True)
