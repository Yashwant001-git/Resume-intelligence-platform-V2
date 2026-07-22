from pathlib import Path

from app.pipeline.parser.parser_manager import ParserManager
from app.pipeline.section.section_detector import SectionDetector
from app.pipeline.section.section_builder import SectionBuilder
from app.pipeline.extraction.extractors.experience_extractor import ExperienceExtractor 
from app.pipeline.loader.pdf_loader import PDFLoader


def main():

    # -------------------------------------------------------------
    # Resume Path
    # -------------------------------------------------------------

    resume_path = Path("data/input/ShreyaSinhaResume.pdf")

    # -------------------------------------------------------------
    # Parse Resume
    # -------------------------------------------------------------
    loader = PDFLoader()
    document = loader.load(resume_path)
    print("\nParsing Resume...")

    parser = ParserManager()
    document = parser.parse(document)

    # print("=" * 100)
    # print("ALL DOCLING TEXT ITEMS")
    # print("=" * 100)

    # for i, item in enumerate(document.raw_document.texts):
    #     print(f"{i:03} | {type(item).__name__:<20} | {repr(item.text)}")
    
    

    # -------------------------------------------------------------
    # Detect Sections
    # -------------------------------------------------------------

    print("Detecting Sections...")

    detector = SectionDetector()
    matches = detector.detect(document)

    print(f"Detected {len(matches)} sections")

    print("Building Resume Sections...")

    builder = SectionBuilder()
    document = builder.build(document, matches)

    # -------------------------------------------------------------
    # Experiance Extraction
    # -------------------------------------------------------------

    extractor = ExperienceExtractor()

    experiences = extractor.extract(document.sections.experience)

    for i, exp in enumerate(experiences, start=1):

        print("=" * 60)
        print(f"Experience {i}")
        print("=" * 60)

        print("Job Title :", exp.job_title)
        print("Company   :", exp.company)
        print("Location  :", exp.location)
        print("Start Date:", exp.start_date)
        print("End Date  :", exp.end_date)

        print("\nDescription:")
        for point in exp.description:
            print("-", point)


if __name__ == "__main__":
    main()