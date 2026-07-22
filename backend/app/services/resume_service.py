from pathlib import Path
from tempfile import NamedTemporaryFile

from fastapi import UploadFile

from app.pipeline.pipeline_manager import PipelineManager
from app.utils.logger import logger


class ResumeService:

    ALLOWED_EXTENSIONS = {".pdf"}

    def __init__(self):

        self.pipeline = PipelineManager()

    async def process_resume(
        self,
        file: UploadFile,
    ):

        if file.filename is None:
            raise ValueError("No file uploaded.")

        extension = Path(file.filename).suffix.lower()

        if extension not in self.ALLOWED_EXTENSIONS:
            raise ValueError(
                f"Unsupported file type: {extension}"
            )

        logger.info(f"Uploading resume: {file.filename}")

        with NamedTemporaryFile(
            suffix=extension,
            delete=False,
        ) as temp_file:

            temp_file.write(await file.read())

            temp_path = Path(temp_file.name)

        try:

            candidate = self.pipeline.process(temp_path)

            return candidate

        finally:

            if temp_path.exists():
                temp_path.unlink()

                logger.info("Temporary file deleted.")