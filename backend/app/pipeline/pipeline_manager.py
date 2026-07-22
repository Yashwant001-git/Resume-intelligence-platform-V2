from app.pipeline.loader.pdf_loader import PDFLoader
from app.pipeline.parser.parser_manager import ParserManager
from app.pipeline.section.section_manager import SectionManager
from app.pipeline.extraction.extraction_manager import ExtractionManager
from app.utils.logger import logger

class PipelineManager:

    def __init__(self):

        self.loader = PDFLoader()
        self.parser = ParserManager()
        self.section_manager = SectionManager()
        self.extraction_manager = ExtractionManager()

    def process(self, resume_path):

        logger.info("Starting resume processing pipeline...")

        document = self.loader.load(resume_path)

        document = self.parser.parse(document)

        document = self.section_manager.build(document)

        candidate = self.extraction_manager.extract(document)

        logger.info("Resume processing completed successfully.")

        return candidate