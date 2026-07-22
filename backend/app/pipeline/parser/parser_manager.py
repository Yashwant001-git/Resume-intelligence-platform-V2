from app.models.document import Document
from app.pipeline.parser.docling_parser import DoclingParser


class ParserManager:

    def __init__(self):
        self.parser = DoclingParser()

    def parse(self, document: Document) -> Document:
        return self.parser.parse(document)