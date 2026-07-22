# from pathlib import Path

# from app.pipeline.loader.pdf_loader import PDFLoader
# from app.pipeline.parser.parser_manager import ParserManager
# from app.pipeline.section.section_detector import SectionDetector
# from app.pipeline.section.section_builder import SectionBuilder

# from app.pipeline.extraction.education.education_extractor import (
#     EducationExtractor,
# )


# def main():

#     # -------------------------------------------------------------
#     # Resume Path
#     # -------------------------------------------------------------

#     resume_path = Path("data/input/ShreyaSinhaResume.pdf")

#     # -------------------------------------------------------------
#     # Load Resume
#     # -------------------------------------------------------------

#     print("\nLoading Resume...")

#     loader = PDFLoader()
#     document = loader.load(resume_path)

#     # -------------------------------------------------------------
#     # Parse Resume
#     # -------------------------------------------------------------

#     print("Parsing Resume...")

#     parser = ParserManager()
#     document = parser.parse(document)

#     # -------------------------------------------------------------
#     # Detect Sections
#     # -------------------------------------------------------------

#     print("Detecting Sections...")

#     detector = SectionDetector()
#     matches = detector.detect(document)

#     print(f"Detected {len(matches)} sections")

#     # -------------------------------------------------------------
#     # Build Resume Sections
#     # -------------------------------------------------------------

#     print("Building Resume Sections...")

#     builder = SectionBuilder()
#     document = builder.build(document, matches)

#     # -------------------------------------------------------------
#     # Print Raw Education Section
#     # -------------------------------------------------------------

#     print("\n")
#     print("=" * 80)
#     print("RAW EDUCATION SECTION")
#     print("=" * 80)

#     if not document.sections.education:
#         print("Education section not found.")
#         return

#     for line in document.sections.education:
#         print(line)

#     # -------------------------------------------------------------
#     # Education Extraction
#     # -------------------------------------------------------------

#     print("\n")
#     print("=" * 80)
#     print("RUNNING OLLAMA EDUCATION EXTRACTOR")
#     print("=" * 80)

#     extractor = EducationExtractor()

#     educations = extractor.extract(document.sections.education)

#     # -------------------------------------------------------------
#     # Results
#     # -------------------------------------------------------------

#     print("\n")
#     print("=" * 80)
#     print("EXTRACTED EDUCATION")
#     print("=" * 80)

#     if not educations:
#         print("No education information extracted.")
#         return

#     for index, edu in enumerate(educations, start=1):

#         print(f"\nEducation {index}")
#         print("-" * 40)
#         print(f"Degree      : {edu.degree}")
#         print(f"Institution : {edu.institution}")
#         print(f"Location    : {edu.location}")
#         print(f"Start Date  : {edu.start_date}")
#         print(f"End Date    : {edu.end_date}")
#         print(f"Grade       : {edu.grade}")


# if __name__ == "__main__":
#     main()