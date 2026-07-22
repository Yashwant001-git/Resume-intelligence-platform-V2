"""
Skills Component
"""

import streamlit as st


class SkillsComponent:

    @staticmethod
    def render(skills: dict):

        st.subheader("🛠 Skills")

        if not skills:
            st.info("No skills found.")
            return

        categories = {
            "Programming Languages": "programming_languages",
            "Frameworks": "frameworks",
            "Libraries": "libraries",
            "Databases": "databases",
            "Cloud": "cloud",
            "Tools": "tools",
            "AI / ML": "ai_ml_domains",
            "Soft Skills": "soft_skills",
            "Others": "others",
        }

        for title, key in categories.items():

            values = skills.get(key, [])

            if not values:
                continue

            st.markdown(f"**{title}**")

            cols = st.columns(4)

            for i, value in enumerate(values):
                cols[i % 4].success(value)

            st.write("")