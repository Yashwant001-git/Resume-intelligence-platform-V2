import re

from app.models.personal_info import PersonalInfo
from app.pipeline.validation.validation_report import ValidationReport


class PersonalInfoValidator:

    EMAIL_PATTERN = re.compile(
        r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    )

    PHONE_PATTERN = re.compile(
        r"^\+?[0-9\s()-]{8,20}$"
    )

    def validate(
        self,
        personal_info: PersonalInfo,
    ) -> ValidationReport:

        report = ValidationReport()

        if not personal_info.name:
            report.add_issue(
                "name",
                "Candidate name is missing.",
                "ERROR",
            )

        if personal_info.email:

            if not self.EMAIL_PATTERN.match(
                personal_info.email
            ):
                report.add_issue(
                    "email",
                    "Invalid email address.",
                )

        else:
            report.add_issue(
                "email",
                "Email not found.",
                "ERROR",
            )

        if personal_info.phone:

            if not self.PHONE_PATTERN.match(
                personal_info.phone
            ):
                report.add_issue(
                    "phone",
                    "Invalid phone number.",
                )

        return report