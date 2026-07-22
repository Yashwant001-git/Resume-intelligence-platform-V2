from app.models.llm_response import LLMResponse
from app.models.personal_info import PersonalInfo

from app.utils.logger import logger


class PersonalInfoExtractor:

    def extract(self, llm_response: LLMResponse) -> PersonalInfo:

        logger.info("Extracting personal information...")

        data = llm_response.personal_info

        return PersonalInfo(
            full_name=data.get("name", ""),
            job_title=data.get("Job title", ""),
            email=data.get("email", ""),
            phone=data.get("phone", ""),
            location=data.get("location", ""),
            linkedin=data.get("linkedin", ""),
            github=data.get("github", ""),
        )