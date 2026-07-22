"""
Education Component
"""

import streamlit as st


class EducationComponent:

    @staticmethod
    def render(education: list):

        st.subheader("🎓 Education")

        if not education:
            st.info("No education details found.")
            return

        for edu in education:

            with st.container(border=True):

                st.markdown(f"### {edu.get('degree', 'N/A')}")

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown(
                        f"**🏫 Institution:** {edu.get('institution', 'N/A')}"
                    )

                    st.markdown(
                        f"**📍 Location:** {edu.get('location', 'N/A')}"
                    )

                with col2:
                    start = edu.get("start_date", "")
                    end = edu.get("end_date", "")

                    duration = f"{start} - {end}".strip(" -")

                    st.markdown(
                        f"**📅 Duration:** {duration if duration else 'N/A'}"
                    )

                    st.markdown(
                        f"**⭐ Grade:** {edu.get('grade', 'N/A')}"
                    )

                st.write("")