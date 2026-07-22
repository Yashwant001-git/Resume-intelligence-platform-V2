"""
Upload Component
"""

import streamlit as st

from services.api import APIService


class UploadComponent:

    @staticmethod
    def render():

        uploaded_file = st.file_uploader(
            "Upload Resume",
            type=["pdf"],
        )

        if uploaded_file is None:
            return None

        st.success(
            f"Selected File: {uploaded_file.name}"
        )

        if st.button(
            "🚀 Extract Resume",
            use_container_width=True,
        ):

            with st.spinner(
                "Extracting Resume..."
            ):

                try:

                    response = (
                        APIService.extract_resume(
                            uploaded_file
                        )
                    )

                    return response["data"]

                except Exception as e:

                    st.error(str(e))

                    return None

        return None