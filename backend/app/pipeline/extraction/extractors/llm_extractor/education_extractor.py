from app.models.education import Education
from app.models.llm_response import LLMResponse

from app.utils.logger import logger


class EducationExtractor:
    """
    Converts the LLM education response into a list of Education objects.
    """

    def extract(self, llm_response: LLMResponse) -> list[Education]:

        logger.info("Extracting education...")

        education_list = []

        for item in llm_response.education:

            education = Education(
                degree=item.get("degree", ""),
                institution=item.get("institution", ""),
                location=item.get("location", ""),
                start_date=item.get("start_date", ""),
                end_date=item.get("end_date", ""),
                grade=item.get("grade", ""),
            )

            education_list.append(education)

        logger.info(f"Extracted {len(education_list)} education entries.")

        return education_list