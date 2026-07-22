# app/pipeline/extraction/extractors/llm/llm_extractor.py

from app.models.document import Document
from app.models.llm_response import LLMResponse


from app.pipeline.extraction.llm.ollama_client import OllamaClient
from app.pipeline.extraction.llm.prompts import RESUME_EXTRACTION_PROMPT
from app.pipeline.extraction.llm.response_parser import ResponseParser

from app.utils.logger import logger


class LLMExtractor:
    """
    Sends the complete resume to Ollama and returns the extracted JSON.
    """

    def __init__(self):
        self.client = OllamaClient()

    def extract(self, document: Document) -> LLMResponse:

        logger.info("Starting LLM extraction...")

        # prompt = RESUME_EXTRACTION_PROMPT.format(
        #     resume=document.markdown
        # )
        prompt = RESUME_EXTRACTION_PROMPT.replace(
            "<<RESUME>>",
            document.markdown
        )

        response = self.client.generate(prompt)

        data = ResponseParser.parse(response)

        logger.info("LLM extraction completed.")

        # return data
        return LLMResponse(
            personal_info=data.get("personal_info", {}),
            education=data.get("education", []),
            certifications=data.get("certifications", []),
        )