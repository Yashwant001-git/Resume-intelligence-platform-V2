from pathlib import Path

from app.models.document import Document
from app.pipeline.loader.base_loader import BaseLoader
from app.utils.logger import logger


class PDFLoader(BaseLoader):
    """
    Loads PDF documents.
    """

    def load(self, file_path: Path) -> Document:

        logger.info("=" * 60)
        logger.info("PDF Loader Started")
        logger.info("=" * 60)

        logger.info(f"Loading document: {file_path}")

        if not file_path.exists():
            logger.error(f"File not found: {file_path}")
            raise FileNotFoundError(file_path)

        if file_path.suffix.lower() != ".pdf":
            logger.error("Unsupported file type.")
            raise ValueError("Only PDF files are supported.")

        document = Document(
            file_path=file_path,
            file_name=file_path.name,
            file_extension=file_path.suffix.lower(),
            file_size=file_path.stat().st_size,
        )

        logger.info("Document loaded successfully.")
        logger.info(f"Filename : {document.file_name}")
        logger.info(f"Size     : {document.file_size} bytes")

        return document