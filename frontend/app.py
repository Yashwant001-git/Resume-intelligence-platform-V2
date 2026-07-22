"""
Resume Intelligence Platform
"""

import streamlit as st

from components.upload import UploadComponent
from components.personal_info import PersonalInfoComponent
from components.skills import SkillsComponent
from components.education import EducationComponent
from components.experience import ExperienceComponent
from components.projects import ProjectsComponent
from components.certifications import CertificationsComponent

from services.api import APIService

from utils.constants import (
    APP_TITLE,
    APP_DESCRIPTION,
)


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title=APP_TITLE,
    page_icon="📄",
    layout="wide",
)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.title("Resume Intelligence")

    st.write(APP_DESCRIPTION)

    st.divider()

    st.success("🟢 Backend Connected")

    st.divider()

    st.caption("Version 1.0.0")

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title(APP_TITLE)

st.write(
    "Upload a resume to extract structured candidate information."
)

st.divider()

# --------------------------------------------------
# Upload Resume
# --------------------------------------------------

candidate = UploadComponent.render()

# --------------------------------------------------
# Display Candidate Information
# --------------------------------------------------

if candidate:

    # ---------------- Profile ----------------

    PersonalInfoComponent.render(
        candidate.get("personal_info", {})
    )

    # ---------------- Summary ----------------

    summary = candidate.get("summary", "")

    if summary:

        st.divider()

        st.subheader("📝 Professional Summary")

        st.write(summary)

    # ---------------- Skills ----------------

    st.divider()

    SkillsComponent.render(
        candidate.get("skills", {})
    )

    # ---------------- Education ----------------

    st.divider()

    EducationComponent.render(
        candidate.get("education", [])
    )

    # ---------------- Experience ----------------

    st.divider()

    ExperienceComponent.render(
        candidate.get("experience", [])
    )

    # ---------------- Projects ----------------

    st.divider()

    ProjectsComponent.render(
        candidate.get("projects", [])
    )

    # ---------------- Certifications ----------------

    st.divider()

    CertificationsComponent.render(
        candidate.get("certifications", [])
    )

    # ---------------- Achievements ----------------

    achievements = candidate.get("achievements", [])

    if achievements:

        st.divider()

        st.subheader("🏆 Achievements")

        for achievement in achievements:
            st.markdown(f"- {achievement}")

    # ---------------- Languages ----------------

    languages = candidate.get("languages", [])

    if languages:

        st.divider()

        st.subheader("🌐 Languages")

        cols = st.columns(4)

        for index, language in enumerate(languages):
            cols[index % 4].info(language)

    # ---------------- Interests ----------------

    interests = candidate.get("interests", [])

    if interests:

        st.divider()

        st.subheader("🎯 Interests")

        cols = st.columns(4)

        for index, interest in enumerate(interests):
            cols[index % 4].success(interest)

    # ---------------- Footer ----------------

    st.divider()

    st.success("✅ Resume processed successfully.")

    # ---------------- Download Excel ----------------

    try:

        excel_data = APIService.download_excel()

        st.download_button(
            label="📥 Download Excel",
            data=excel_data,
            file_name="resumes.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True,
        )

    except Exception:

        st.warning("Excel file is not available.")