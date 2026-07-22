from abc import ABC, abstractmethod
from pathlib import Path

from app.models.document import Document


class BaseLoader(ABC):
    """
    Base class for all document loaders.
    """

    @abstractmethod
    def load(self, file_path: Path) -> Document:
        """
        Load a document and return a Document object.
        """
        pass