from app.pipeline.loader.loader_factory import LoaderFactory
from app.pipeline.parser.docling_parser import DoclingParser
# from app.pipeline.extraction.personal_info.context_builder import ContextBuilder
from pathlib import Path
from app.pipeline.section.section_detector import SectionDetector

# pdf_path = "sample_resume.pdf"
pdf_path = Path("data/input/sample_resume.pdf")

loader = LoaderFactory.get_loader(pdf_path)
document = loader.load(pdf_path)

parser = DoclingParser()
document = parser.parse(document)

print("=" * 80)
print("RAW DOCUMENT ITEMS")
print("=" * 80)

for i, item in enumerate(document.raw_document.texts):
    print(f"\nIndex : {i}")
    print(f"Type  : {type(item).__name__}")
    print(f"Text  : {repr(item.text)}")

print("\n" + "=" * 80)
print("DOCLING DOCUMENT ATTRIBUTES")
print("=" * 80)

print(dir(document.raw_document))