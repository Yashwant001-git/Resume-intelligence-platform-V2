# app/pipeline/extraction/extractors/llm/certification_extractor.py

from app.models.certification import Certification
from app.models.llm_response import LLMResponse

from app.utils.logger import logger


class CertificationExtractor:
    """
    Converts the LLM certification response into a list of Certification objects.
    """

    def extract(self, llm_response: LLMResponse) -> list[Certification]:

        logger.info("Extracting certifications...")

        certification_list = []

        for item in llm_response.certifications:

            certification = Certification(
                name=item.get("name", "")
            )

            certification_list.append(certification)

        logger.info(
            f"Extracted {len(certification_list)} certifications."
        )

        return certification_list