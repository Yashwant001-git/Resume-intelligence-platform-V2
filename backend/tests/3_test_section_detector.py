from pathlib import Path

from app.pipeline.loader.loader_factory import LoaderFactory
from app.pipeline.parser.docling_parser import DoclingParser
from app.pipeline.section.section_detector import SectionDetector

def main():
    # Resume path
    resume_path = Path("data/input/ShreyaSinhaResume.pdf")

    # Load document
    loader = LoaderFactory.get_loader(resume_path)
    document = loader.load(resume_path)

    # Parse using Docling
    parser = DoclingParser()
    document = parser.parse(document)

    # Detect sections
    detector = SectionDetector()
    matches = detector.detect(document)

    print("\nDetected Sections")
    print("=" * 60)

    for match in matches:
        print(match)


if __name__ == "__main__":
    main()