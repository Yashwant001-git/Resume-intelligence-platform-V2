"""
Certifications Component
"""

import streamlit as st


class CertificationsComponent:

    @staticmethod
    def render(certifications: list):

        st.subheader("📜 Certifications")

        if not certifications:
            st.info("No certifications found.")
            return

        for index, certification in enumerate(certifications, start=1):

            with st.container(border=True):

                st.markdown(
                    f"**{index}. {certification.get('name', 'N/A')}**"
                )

                issuer = certification.get("issuer", "")

                if issuer:
                    st.write(f"🏢 **Issuer:** {issuer}")

                issue_date = certification.get("issue_date", "")

                if issue_date:
                    st.write(f"📅 **Issued:** {issue_date}")

                credential_id = certification.get("credential_id", "")

                if credential_id:
                    st.write(
                        f"🆔 **Credential ID:** {credential_id}"
                    )

                credential_url = certification.get(
                    "credential_url", ""
                )

                if credential_url:
                    st.markdown(
                        f"🔗 **Credential:** {credential_url}"
                    )