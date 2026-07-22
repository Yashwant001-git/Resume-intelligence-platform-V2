from pathlib import Path

from app.pipeline.loader.loader_factory import LoaderFactory


def test_pdf_loader():

    file_path = Path("data/input/sample_resume.pdf")

    loader = LoaderFactory.get_loader(file_path)

    document = loader.load(file_path)

    print(document)