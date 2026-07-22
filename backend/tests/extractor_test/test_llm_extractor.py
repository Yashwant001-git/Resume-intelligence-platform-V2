from pathlib import Path
from pprint import pprint

from app.pipeline.loader.pdf_loader import PDFLoader
from app.pipeline.parser.parser_manager import ParserManager

from app.pipeline.extraction.extractors.llm_extractor.llm_extractor import (
    LLMExtractor,
)
from app.pipeline.extraction.extractors.llm_extractor.personal_info_extractor import (
    PersonalInfoExtractor,
)
from app.pipeline.extraction.extractors.llm_extractor.education_extractor import (
    EducationExtractor,
)
from app.pipeline.extraction.extractors.llm_extractor.certification_extractor import (
    CertificationExtractor,
)


def main():

    # -------------------------------------------------------------
    # Resume Path
    # -------------------------------------------------------------

    # resume_path = Path("data/input/ShreyaSinhaResume.pdf")
    resume_path = Path("data/input/sample_resume.pdf")

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
    # LLM Extraction
    # -------------------------------------------------------------

    print("\n")
    print("=" * 80)
    print("RUNNING LLM EXTRACTOR")
    print("=" * 80)

    llm_extractor = LLMExtractor()

    llm_response = llm_extractor.extract(document)

    # -------------------------------------------------------------
    # Personal Information
    # -------------------------------------------------------------

    print("\n")
    print("=" * 80)
    print("PERSONAL INFO")
    print("=" * 80)

    personal_info = PersonalInfoExtractor().extract(llm_response)

    pprint(personal_info)

    # -------------------------------------------------------------
    # Education
    # -------------------------------------------------------------

    print("\n")
    print("=" * 80)
    print("EDUCATION")
    print("=" * 80)

    education = EducationExtractor().extract(llm_response)

    for idx, edu in enumerate(education, start=1):
        print(f"\nEducation {idx}")
        pprint(edu)

    # -------------------------------------------------------------
    # Certifications
    # -------------------------------------------------------------

    print("\n")
    print("=" * 80)
    print("CERTIFICATIONS")
    print("=" * 80)

    certifications = CertificationExtractor().extract(llm_response)

    for idx, cert in enumerate(certifications, start=1):
        print(f"\nCertification {idx}")
        pprint(cert)


if __name__ == "__main__":
    main()