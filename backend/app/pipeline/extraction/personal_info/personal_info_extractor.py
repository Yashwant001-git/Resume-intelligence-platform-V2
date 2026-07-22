from app.models.document import Document
from app.models.personal_info import PersonalInfo

from .ollama_extractor import OllamaExtractor
from .response_parser import ResponseParser


class PersonalInfoExtractor:
    """
    Extract personal information from a resume using an LLM.
    """

    def __init__(self):
        self.ollama_extractor = OllamaExtractor()

    def extract(self, document: Document) -> PersonalInfo:
        """
        Extract personal information from a resume.

        Args:
            document: Parsed resume document.

        Returns:
            PersonalInfo object.
        """
        

        response = self.ollama_extractor.extract(document)

        personal_info = ResponseParser.parse(response)

        return personal_info