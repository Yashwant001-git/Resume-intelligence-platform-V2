import json
import re
from pathlib import Path

from docling_core.types.doc.document import SectionHeaderItem

from app.models.document import Document
from app.models.section_match import SectionMatch
from app.utils.logger import logger


class SectionDetector:
    """
    Detects resume sections from a DoclingDocument.

    Input:
        Document.raw_document (DoclingDocument)

    Output:
        List[SectionMatch]
    """

    def __init__(self) -> None:
        self.lookup = self._load_headers()

    def detect(self, document: Document) -> list[SectionMatch]:
        """
        Detect all section headers in the resume.
        """

        logger.info("Starting section detection...")

        if document.raw_document is None:
            logger.warning("Document has no DoclingDocument.")
            return []

        matches = []

        for index, item in enumerate(document.raw_document.texts):

            # Ignore everything except section headers
            if not isinstance(item, SectionHeaderItem):
                continue

            normalized = self._normalize_header(item.text)

            section = self.lookup.get(normalized)

            if section:
                logger.info(
                    f"Detected section: '{section}' "
                    f"(Header='{item.text}', Index={index})"
                )

                matches.append(
                    SectionMatch(
                        section=section,
                        header=item.text,
                        start_index=index
                    )
                )

        logger.info(f"Detected {len(matches)} sections.")

        return matches

    def _load_headers(self) -> dict[str, str]:
        """
        Loads section_headers.json and converts it into
        a lookup dictionary.

        Example:

        {
            "skills": [
                "skills",
                "technical skills"
            ]
        }

        becomes

        {
            "skills": "skills",
            "technical skills": "skills"
        }
        """

        config_path = (
            Path(__file__)
            .resolve()
            .parents[2]
            / "config"
            / "section_headers.json"
        )

        with open(config_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        lookup = {}

        for section, headers in data.items():
            for header in headers:
                normalized = self._normalize_header(header)
                lookup[normalized] = section

        logger.info(
            f"Loaded {len(lookup)} section header aliases."
        )

        return lookup

    def _normalize_header(self, header: str) -> str:
        """
        Normalize a section header.

        Examples

        " EDUCATION "
            -> education

        "PROJECTS:"
            -> projects

        "S K I L L S"
            -> skills

        "Technical Skills"
            -> technical skills
        """

        header = header.lower()

        header = header.strip()

        header = header.replace(":", "")

        header = re.sub(r"\s+", " ", header)

        words = header.split()

        # Detect headers like:
        # S K I L L S
        # P R O J E C T S
        if words and all(len(word) == 1 for word in words):
            header = "".join(words)

        return header