from pathlib import Path

from app.models.document import Document
from app.pipeline.loader.pdf_loader import PDFLoader
from app.pipeline.parser.parser_manager import ParserManager
from app.pipeline.section.section_detector import SectionDetector
from app.pipeline.section.section_builder import SectionBuilder
from app.pipeline.extraction.extractors.skills_extractor import SkillsExtractor


def main():

    resume_path = Path("data/input/sample_resume.pdf")

    # ----------------------------
    # Load Resume
    # ----------------------------

    loader = PDFLoader()

    document = loader.load(resume_path)

    # ----------------------------
    # Parse Resume
    # ----------------------------

    parser = ParserManager()

    document = parser.parse(document)

    # ----------------------------
    # Detect Sections
    # ----------------------------

    detector = SectionDetector()

    matches = detector.detect(document)

    # ----------------------------
    # Build Sections
    # ----------------------------

    builder = SectionBuilder()

    document = builder.build(document, matches)

    # ----------------------------
    # Extract Skills
    # ----------------------------

    extractor = SkillsExtractor()

    skills = extractor.extract(document.sections.skills)
    # print(type(document.sections.skills))

    # for item in document.sections.skills:
    #     print(type(item))
    #     print(item)
    #     print("-" * 80)

    # ----------------------------
    # Print Result
    # ----------------------------

    print("\n" + "=" * 70)
    print("SKILLS")
    print("=" * 70)

    print(f"Programming Languages : {skills.programming_languages}")
    print(f"Frameworks            : {skills.frameworks}")
    print(f"Libraries             : {skills.libraries}")
    print(f"Databases             : {skills.databases}")
    print(f"Cloud                 : {skills.cloud}")
    print(f"Tools                 : {skills.tools}")
    print(f'AI/ML                 : {skills.ai_ml_domains}')
    print(f"Soft Skills           : {skills.soft_skills}")
    print(f"Others                : {skills.others}")

    print("=" * 70)


if __name__ == "__main__":
    main()