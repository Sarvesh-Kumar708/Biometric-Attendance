import streamlit as st


def footer_home():
    st.markdown(
        """
        <style>
            .footer-contact-button {
                transition: transform 180ms ease, box-shadow 180ms ease, background 180ms ease;
            }
            .footer-contact-button:hover {
                transform: translateY(-2px);
                background: linear-gradient(180deg, #f472b6 0%, #db2777 100%) !important;
                box-shadow: 0 6px 14px rgba(219, 39, 119, 0.32), inset 0 0 0 1px rgba(255,255,255,0.12) !important;
            }
            .footer-contact-button:active {
                transform: translateY(0) scale(0.98);
            }
            .footer-contact-button:focus-visible {
                outline: 2px solid #f9a8d4;
                outline-offset: 3px;
            }
        </style>
        <div style="margin-top:2rem; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:12px; text-align:center;">
            <p style="font-weight:bold; color:white; margin:0;">Created with ❤️ by SARVESH</p>
            <div style="display:flex; flex-wrap:wrap; justify-content:center; gap:10px;">
                <a href="https://www.linkedin.com/in/sarveshsingh007" target="_blank" rel="noopener noreferrer"
                   role="button"
                   kind="primary"
                   data-testid="stBaseButton-primary"
                   class="footer-contact-button"
                   style="display:inline-flex; align-items:center; justify-content:center; gap:8px; min-height:42px; padding:0.7rem 1.1rem; border:1px solid rgba(255,255,255,0.18); border-radius:0.75rem; color:#fff; text-decoration:none; font-size:0.8rem; font-weight:600; background:linear-gradient(180deg, #ec4899 0%, #be185d 100%); box-shadow:0 1px 2px rgba(0,0,0,0.18), inset 0 0 0 1px rgba(255,255,255,0.12); cursor:pointer;">
                    <b>LinkedIn : sarveshsingh007</b>
                </a>
                <a href="mailto:janukumarg708@gmail.com" rel="noopener noreferrer"
                   role="button"
                   kind="primary"
                   data-testid="stBaseButton-primary"
                   class="footer-contact-button"
                   style="display:inline-flex; align-items:center; justify-content:center; gap:8px; min-height:42px; padding:0.7rem 1.1rem; border:1px solid rgba(255,255,255,0.18); border-radius:0.75rem; color:#fff; text-decoration:none; font-size:0.8rem; font-weight:600; background:linear-gradient(180deg, #ec4899 0%, #be185d 100%); box-shadow:0 1px 2px rgba(0,0,0,0.18), inset 0 0 0 1px rgba(255,255,255,0.12); cursor:pointer;">
                    <b>Email : janukumarg708@gmail.com</b>
                </a>
                <a href="tel:+916202834373" rel="noopener noreferrer"
                   role="button"
                   kind="primary"
                   data-testid="stBaseButton-primary"
                   class="footer-contact-button"
                   style="display:inline-flex; align-items:center; justify-content:center; gap:8px; min-height:42px; padding:0.7rem 1.1rem; border:1px solid rgba(255,255,255,0.18); border-radius:0.75rem; color:#fff; text-decoration:none; font-size:0.8rem; font-weight:600; background:linear-gradient(180deg, #ec4899 0%, #be185d 100%); box-shadow:0 1px 2px rgba(0,0,0,0.18), inset 0 0 0 1px rgba(255,255,255,0.12); cursor:pointer;">
                    <b>Mobile : +91 62028 34373</b>
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def footer_dashboard():
    st.markdown(
        """
        <style>
            .footer-contact-button {
                transition: transform 180ms ease, box-shadow 180ms ease, background 180ms ease;
            }
            .footer-contact-button:hover {
                transform: translateY(-2px);
                background: linear-gradient(180deg, #f472b6 0%, #db2777 100%) !important;
                box-shadow: 0 6px 14px rgba(219, 39, 119, 0.32), inset 0 0 0 1px rgba(255,255,255,0.12) !important;
            }
            .footer-contact-button:active {
                transform: translateY(0) scale(0.98);
            }
            .footer-contact-button:focus-visible {
                outline: 2px solid #f9a8d4;
                outline-offset: 3px;
            }
        </style>
        <div style="margin-top:2rem; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:12px; text-align:center;">
            <p style="font-weight:bold; color:black; margin:0;">Created with ❤️ by SARVESH</p>
            <div style="display:flex; flex-wrap:wrap; justify-content:center; gap:10px;">
                <a href="https://www.linkedin.com/in/sarveshsingh007" target="_blank" rel="noopener noreferrer"
                   role="button"
                   kind="primary"
                   data-testid="stBaseButton-primary"
                   class="footer-contact-button"
                   style="display:inline-flex; align-items:center; justify-content:center; gap:8px; min-height:42px; padding:0.7rem 1.1rem; border:1px solid rgba(0,0,0,0.15); border-radius:0.75rem; color:#fff; text-decoration:none; font-size:0.8rem; font-weight:600; background:linear-gradient(180deg, #ec4899 0%, #be185d 100%); box-shadow:0 1px 2px rgba(0,0,0,0.18), inset 0 0 0 1px rgba(255,255,255,0.12); cursor:pointer;">
                    <b>LinkedIn : sarveshsingh007</b>
                </a>
                <a href="mailto:janukumarg708@gmail.com" rel="noopener noreferrer"
                   role="button"
                   kind="primary"
                   data-testid="stBaseButton-primary"
                   class="footer-contact-button"
                   style="display:inline-flex; align-items:center; justify-content:center; gap:8px; min-height:42px; padding:0.7rem 1.1rem; border:1px solid rgba(0,0,0,0.15); border-radius:0.75rem; color:#fff; text-decoration:none; font-size:0.8rem; font-weight:600; background:linear-gradient(180deg, #ec4899 0%, #be185d 100%); box-shadow:0 1px 2px rgba(0,0,0,0.18), inset 0 0 0 1px rgba(255,255,255,0.12); cursor:pointer;">
                    <b>Email : janukumarg708@gmail.com</b>
                </a>
                <a href="tel:+916202834373" rel="noopener noreferrer"
                   role="button"
                   kind="primary"
                   data-testid="stBaseButton-primary"
                   class="footer-contact-button"
                   style="display:inline-flex; align-items:center; justify-content:center; gap:8px; min-height:42px; padding:0.7rem 1.1rem; border:1px solid rgba(0,0,0,0.15); border-radius:0.75rem; color:#fff; text-decoration:none; font-size:0.8rem; font-weight:600; background:linear-gradient(180deg, #ec4899 0%, #be185d 100%); box-shadow:0 1px 2px rgba(0,0,0,0.18), inset 0 0 0 1px rgba(255,255,255,0.12); cursor:pointer;">
                    <b>Mobile : +91 62028 34373</b>
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
