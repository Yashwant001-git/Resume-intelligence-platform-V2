from pathlib import Path
from pprint import pprint

from app.pipeline.loader.pdf_loader import PDFLoader
from app.pipeline.parser.parser_manager import ParserManager
from app.pipeline.section.section_manager import SectionManager
from app.pipeline.extraction.extraction_manager import ExtractionManager


def main():

    # -------------------------------------------------------------
    # Resume Path
    # -------------------------------------------------------------

    resume_path = Path("data/input/ShreyaSinhaResume.pdf")
    # resume_path = Path("data/input/sample_resume.pdf")

    # -------------------------------------------------------------
    # Load Resume
    # -------------------------------------------------------------

    print("\nLoading Resume...")

    loader = PDFLoader()
    document = loader.load(resume_path)

    # -------------------------------------------------------------
    # Parse Resume
    # -------------------------------------------------------------

    print("Parsing Resume...")

    parser = ParserManager()
    document = parser.parse(document)

    # -------------------------------------------------------------
    # Build Resume Sections
    # -------------------------------------------------------------

    print("Building Resume Sections...")

    section_manager = SectionManager()
    document = section_manager.build(document)

    # -------------------------------------------------------------
    # Extraction Pipeline
    # -------------------------------------------------------------

    print("\n")
    print("=" * 80)
    print("RUNNING EXTRACTION PIPELINE")
    print("=" * 80)

    extraction_manager = ExtractionManager()
    candidate = extraction_manager.extract(document)

    # -------------------------------------------------------------
    # Results
    # -------------------------------------------------------------

    # print("\n")
    # print("=" * 80)
    # print("PERSONAL INFO")
    # print("=" * 80)

    # pprint(candidate.personal_info)

    # print("\n")
    # print("=" * 80)
    # print("EDUCATION")
    # print("=" * 80)

    # for index, education in enumerate(candidate.education, start=1):
    #     print(f"\nEducation {index}")
    #     pprint(education)

    # print("\n")
    # print("=" * 80)
    # print("CERTIFICATIONS")
    # print("=" * 80)

    # for index, certification in enumerate(candidate.certifications, start=1):
    #     print(f"\nCertification {index}")
    #     pprint(certification)

    # print("\n")
    # print("=" * 80)
    # print("SKILLS")
    # print("=" * 80)

    # pprint(candidate.skills)

    # print("\n")
    # print("=" * 80)
    # print("EXPERIENCE")
    # print("=" * 80)

    # for index, experience in enumerate(candidate.experience, start=1):
    #     print(f"\nExperience {index}")
    #     pprint(experience)

    # print("\n")
    # print("=" * 80)
    # print("PROJECTS")
    # print("=" * 80)

    # for index, project in enumerate(candidate.projects, start=1):
    #     print(f"\nProject {index}")
    #     pprint(project)

    # print("\n")
    # print("=" * 80)
    # print("FINAL CANDIDATE OBJECT")
    # print("=" * 80)

    pprint(candidate)


if __name__ == "__main__":
    main()