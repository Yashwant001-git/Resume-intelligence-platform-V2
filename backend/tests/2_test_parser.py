from pathlib import Path

from app.pipeline.loader.loader_factory import LoaderFactory
from app.pipeline.parser.parser_manager import ParserManager


def test_docling_parser():

    file_path = Path("data/input/sample_resume.pdf")

    loader = LoaderFactory.get_loader(file_path)

    document = loader.load(file_path)

    parser = ParserManager()

    document = parser.parse(document)

    assert document.parsed_document is not None

    print(type(document.parsed_document.raw_document))