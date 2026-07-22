from pathlib import Path

from docling.document_converter import DocumentConverter


def main():

    pdf_path = Path("data/input/ShreyaSinhaResume.pdf")

    converter = DocumentConverter()

    result = converter.convert(pdf_path)

    document = result.document

    print("=" * 80)
    print(type(document))
    print("=" * 80)

    print(document)

    # markdown = document.export_to_markdown()

    # output_dir = Path("data/parsed")
    # output_dir.mkdir(parents=True, exist_ok=True)

    # markdown_path = output_dir / "docling_output1.md"
    # markdown_path.write_text(
    #     markdown,
    #     encoding="utf-8"
    # )


if __name__ == "__main__":
    main()