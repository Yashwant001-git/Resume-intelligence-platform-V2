from pathlib import Path

from app.pipeline.parser.parser_manager import ParserManager
from app.pipeline.extraction.personal_info.personal_info_extractor import PersonalInfoExtractor
from app.pipeline.loader.loader_factory import LoaderFactory
from app.pipeline.parser.docling_parser import DoclingParser


def main():

    resume_path = Path("data/input/ShreyaSinhaResume.pdf")

    loader = LoaderFactory.get_loader(resume_path)
    document = loader.load(resume_path)

    # Parse Resume
    parser = ParserManager()
    document = parser.parse(document)

    # Extract Personal Information
    extractor = PersonalInfoExtractor()
    personal_info = extractor.extract(document)

    print("\n" + "=" * 60)
    print("PERSONAL INFORMATION")
    print("=" * 60)

    print(f"Name      : {personal_info.full_name}")
    print(f"Job Title : {personal_info.job_title}")
    print(f"Email     : {personal_info.email}")
    print(f"Phone     : {personal_info.phone}")
    print(f"Location  : {personal_info.location}")
    print(f"LinkedIn  : {personal_info.linkedin}")
    print(f"GitHub    : {personal_info.github}")
    print(f"Portfolio : {personal_info.portfolio}")

    print("=" * 60)


if __name__ == "__main__":
    main()