from abc import ABC, abstractmethod

from app.models.document import Document


class BaseParser(ABC):
    """
    Base interface for all document parsers.
    """

    @abstractmethod
    def parse(self, document: Document) -> Document:
        """
        Parse the document and enrich the Document object.
        """
        pass