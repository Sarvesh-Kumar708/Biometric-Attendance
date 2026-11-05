import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home
def home_screen():


    header_home()
    style_background_home()
    style_base_layout()


    col1, col2 = st.columns(2, gap="large")

    with col1:
        # st.header("I'm Student")
        st.image("https://www.cusb.ac.in/images/cusb/icon/student_samarth_login.jpg#joomlaImage://local-images/cusb/icon/student_samarth_login.jpg?width=300&height=300", width=300)
        if st.button('Student Portal', type='primary', icon=':material/arrow_outward:', icon_position='right'):
            st.session_state['login_type']='student'
            st.rerun()

    with col2:
        # st.header("I'm Teacher")
        st.image("https://www.cusb.ac.in/images/cusb/icon/employee_samarth_login.jpg#joomlaImage://local-images/cusb/icon/employee_samarth_login.jpg?width=300&height=300", width=300)
        if st.button('Teacher Portal', type='primary', icon=':material/arrow_outward:', icon_position='right'):
            st.session_state['login_type']='teacher'
            st.rerun()

    footer_home()