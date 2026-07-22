# from pathlib import Path

# from app.pipeline.loader.loader_factory import LoaderFactory
# from app.pipeline.parser.docling_parser import DoclingParser
# from app.pipeline.section.section_detector import SectionDetector
# from app.pipeline.section.section_builder import SectionBuilder
# from app.pipeline.extraction.extractors.personal_info_extractor import PersonalInfoExtractor

# from app.models.candidate import Candidate


# def main():

#     resume_path = Path("data/input/ShreyaSinhaResume.pdf")

#     # Load
#     loader = LoaderFactory.get_loader(resume_path)
#     document = loader.load(resume_path)

#     # Parse
#     parser = DoclingParser()
#     document = parser.parse(document)

#     # Detect Sections
#     detector = SectionDetector()
#     matches = detector.detect(document)

#     # Build Sections
#     builder = SectionBuilder()
#     document = builder.build(document, matches)

#     # Initialize Candidate
#     document.candidate = Candidate()

#     # Extract Personal Info
#     extractor = PersonalInfoExtractor()
#     document = extractor.extract(document)

#     # Print Results
#     info = document.candidate.personal_info

#     print("\n")
#     print("=" * 60)
#     print("PERSONAL INFORMATION")
#     print("=" * 60)

#     print(f"Name      : {info.full_name}")
#     print(f"Email     : {info.email}")
#     print(f"Phone     : {info.phone}")
#     print(f"LinkedIn  : {info.linkedin}")
#     print(f"GitHub    : {info.github}")


# if __name__ == "__main__":
#     main()