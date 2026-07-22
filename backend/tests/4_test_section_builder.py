from pathlib import Path

from app.pipeline.loader.loader_factory import LoaderFactory
from app.pipeline.parser.docling_parser import DoclingParser
from app.pipeline.section.section_detector import SectionDetector
from app.pipeline.section.section_builder import SectionBuilder


def main():

    resume_path = Path("data/input/sample_resume.pdf")

    # Load
    loader = LoaderFactory.get_loader(resume_path)
    document = loader.load(resume_path)

    # Parse
    parser = DoclingParser()
    document = parser.parse(document)

    # Detect Sections
    detector = SectionDetector()
    matches = detector.detect(document)

    # Build Sections
    builder = SectionBuilder()
    document = builder.build(document, matches)

    print("\n")
    print("=" * 70)
    print("RESUME SECTIONS")
    print("=" * 70)

    for section_name, items in vars(document.sections).items():

        if not items:
            continue

        print(f"\n[{section_name.upper()}]")
        print("-" * 50)

        for item in items:

            if hasattr(item, "text"):
                print(item.text)
            else:
                print(item)


if __name__ == "__main__":
    main()