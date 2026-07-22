"""
Personal Information Component
"""

import streamlit as st


class PersonalInfoComponent:

    @staticmethod
    def render(personal_info):

        st.subheader("👤 Personal Information")

        col1, col2 = st.columns(2)

        with col1:
            st.text_input(
                "Full Name",
                value=personal_info.get("full_name", ""),
                disabled=True,
            )

            st.text_input(
                "Email",
                value=personal_info.get("email", ""),
                disabled=True,
            )

            st.text_input(
                "Phone",
                value=personal_info.get("phone", ""),
                disabled=True,
            )

            st.text_input(
                "Location",
                value=personal_info.get("location", ""),
                disabled=True,
            )

        with col2:
            st.text_input(
                "Job Title",
                value=personal_info.get("job_title", ""),
                disabled=True,
            )

            st.text_input(
                "LinkedIn",
                value=personal_info.get("linkedin", ""),
                disabled=True,
            )

            st.text_input(
                "GitHub",
                value=personal_info.get("github", ""),
                disabled=True,
            )

            st.text_input(
                "Portfolio",
                value=personal_info.get("portfolio", ""),
                disabled=True,
            )