"""
Experience Component
"""

import streamlit as st


class ExperienceComponent:

    @staticmethod
    def render(experiences: list):

        st.subheader("💼 Experience")

        if not experiences:
            st.info("No experience found.")
            return

        for exp in experiences:

            title = exp.get("job_title", "N/A")
            company = exp.get("company", "N/A")

            with st.expander(f"{title} • {company}", expanded=False):

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown(
                        f"**🏢 Company:** {company}"
                    )

                    st.markdown(
                        f"**📍 Location:** {exp.get('location', 'N/A')}"
                    )

                with col2:

                    start = exp.get("start_date", "")
                    end = exp.get("end_date", "")

                    duration = f"{start} - {end}".strip(" -")

                    st.markdown(
                        f"**📅 Duration:** {duration if duration else 'N/A'}"
                    )

                description = exp.get("description", [])

                if description:

                    st.markdown("### Responsibilities")

                    for item in description:
                        st.markdown(f"- {item}")