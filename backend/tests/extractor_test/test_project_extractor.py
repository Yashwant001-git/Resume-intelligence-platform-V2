from pathlib import Path

from app.pipeline.parser.parser_manager import ParserManager
from app.pipeline.section.section_detector import SectionDetector
from app.pipeline.section.section_builder import SectionBuilder
from app.pipeline.extraction.extractors.project_extractor import ProjectExtractor
from app.pipeline.loader.pdf_loader import PDFLoader


def main():

    # -------------------------------------------------------------
    # Resume Path
    # -------------------------------------------------------------

    resume_path = Path("data/input/sample_resume.pdf")

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
    # Project Extraction
    # -------------------------------------------------------------

    extractor = ProjectExtractor()

    projects = extractor.extract(document.sections.projects)

    for i, project in enumerate(projects, start=1):

        print("=" * 60)
        print(f"Project {i}")
        print("=" * 60)

        print("Title:")
        print(project.title)

        print("\nTechnologies:")
        print(project.technologies)

        print("\nGitHub:")
        print(project.github)

        print("\nDescription:")
        for desc in project.description:
            print("-", desc)

        print()


if __name__ == "__main__":
    main()