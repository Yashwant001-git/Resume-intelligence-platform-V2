from pathlib import Path

from app.pipeline.loader.pdf_loader import PDFLoader


class LoaderFactory:

    @staticmethod
    def get_loader(file_path: Path):

        extension = file_path.suffix.lower()

        if extension == ".pdf":
            return PDFLoader()

        raise ValueError(f"Unsupported file format: {extension}")