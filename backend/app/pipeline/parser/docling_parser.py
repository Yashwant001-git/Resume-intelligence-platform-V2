from docling.document_converter import DocumentConverter

from app.models.document import Document
from app.models.parsed_document import ParsedDocument
from app.pipeline.parser.base_parser import BaseParser
from app.utils.logger import logger


class DoclingParser(BaseParser):
    """
    Parse PDF documents using Docling.
    """

    def __init__(self):
        self.converter = DocumentConverter()

    def parse(self, document: Document) -> Document:

        logger.info("=" * 60)
        logger.info("Docling Parser Started")
        logger.info("=" * 60)

        logger.info(f"Parsing: {document.file_name}")

        try:

            result = self.converter.convert(document.file_path)

            document.markdown = result.document.export_to_markdown()
            document.text = result.document.export_to_text()
            document.raw_document = result.document

            logger.info("Document parsed successfully.")

            return document

        except Exception as e:

            logger.exception(f"Failed to parse {document.file_name}: {e}")
            raise