from app.models.document import Document
from app.models.resume_sections import ResumeSections
from app.models.section_match import SectionMatch
from app.utils.logger import logger
import re
from docling_core.types.doc.document import SectionHeaderItem



class SectionBuilder:
    """
    Build ResumeSections from detected section headers.

    This class groups the Docling items belonging to each section.
    It does not perform any information extraction.
    """

    def build(
        self,
        document: Document,
        matches: list[SectionMatch],
    ) -> Document:

        logger.info("=" * 60)
        logger.info("Section Builder Started")
        logger.info("=" * 60)

        if document.raw_document is None:
            logger.warning("Document has no DoclingDocument.")
            return document

        if not matches:
            logger.warning("No sections detected.")
            return document

        logger.info("Building resume sections...")

        texts = document.raw_document.texts

        # Ensure matches are ordered from top to bottom
        matches = sorted(matches, key=lambda match: match.start_index)

        sections = ResumeSections()

        for index, match in enumerate(matches):

            start = match.start_index + 1

            if index < len(matches) - 1:
                end = matches[index + 1].start_index
            else:
                end = len(texts)

            # items = texts[start:end]
            items = [
                item.text.strip()
                for item in texts[start:end]
                if item.text.strip()
            ]

            #add new thing-----------------------------------------------
            if match.section == "education":

                has_date = any(
                    re.search(r"\d{4}\s*[-–]\s*(\d{4}|Present)", line)
                    for line in items
                )

                if not has_date:

                    for item in texts[end:]:

                        text = item.text.strip()

                        # Stop searching if another major section starts
                        if hasattr(item, "label"):
                            break

                        if re.search(r"\d{4}\s*[-–]\s*(\d{4}|Present)", text):

                            items.append(text)
                            logger.info(
                                f"Appended education date line: {text}"
                            )
                            break
            # -----------------------------------------------------------

            setattr(sections, match.section, items)

            logger.info(
                f"[{match.section.upper()}] -> {len(items)} items"
            )

        document.sections = sections

        logger.info("Section building completed.")

        return document