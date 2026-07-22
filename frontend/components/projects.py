"""
Projects Component
"""

import streamlit as st


class ProjectsComponent:

    @staticmethod
    def render(projects: list):

        st.subheader("🚀 Projects")

        if not projects:
            st.info("No projects found.")
            return

        for project in projects:

            with st.container(border=True):

                st.markdown(
                    f"### {project.get('title', 'Untitled Project')}"
                )

                technologies = project.get("technologies", [])

                if technologies:

                    st.markdown("**🛠 Technologies Used**")

                    cols = st.columns(4)

                    for index, tech in enumerate(technologies):
                        cols[index % 4].success(tech)

                description = project.get("description", [])

                if description:

                    st.markdown("**📝 Description**")

                    for point in description:
                        st.markdown(f"- {point}")

                github = project.get("github", "").strip()

                if github:
                    st.markdown(f"**🔗 GitHub:** {github}")

                st.write("")