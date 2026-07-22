from app.models.document import Document

from app.pipeline.section.section_detector import SectionDetector
from app.pipeline.section.section_builder import SectionBuilder


class SectionManager:

    def __init__(self):

        self.detector = SectionDetector()
        self.builder = SectionBuilder()

    def build(self, document: Document) -> Document:

        matches = self.detector.detect(document)

        document = self.builder.build(
            document=document,
            matches=matches,
        )

        return document