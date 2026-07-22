import re

from app.models.experience import Experience


class ExperienceExtractor:

    def extract(self, section: list[str]) -> list[Experience]:

        if not section:
            return []

        blocks = self._build_blocks(section)

        experiences = []

        for block in blocks:

            experience = Experience()

            (
                experience.job_title,
                experience.company,
            ) = self._extract_job_and_company(block)

            (
                experience.start_date,
                experience.end_date,
            ) = self._extract_dates(block)

            experience.description = self._extract_description(block)

            experiences.append(experience)

        return experiences

    # ---------------------------------------------------------
    # Build Experience Blocks
    # ---------------------------------------------------------

    def _build_blocks(self, lines: list[str]) -> list[list[str]]:

        blocks = []
        current = []

        i = 0

        while i < len(lines):

            line = lines[i].strip()

            if not line:
                i += 1
                continue

            is_new_block = (
                self._is_job_heading(line)
                and i + 1 < len(lines)
                and self._is_date(lines[i + 1])
            )

            if is_new_block:

                if current:
                    blocks.append(current)

                current = [line]

            else:
                current.append(line)

            i += 1

        if current:
            blocks.append(current)

        return blocks

    # ---------------------------------------------------------
    # Job Heading
    # ---------------------------------------------------------

    def _is_job_heading(self, line: str) -> bool:

        separators = (
            " - ",
            " – ",
            " — ",
            " | ",
            " @ ",
        )

        return any(separator in line for separator in separators)

    # ---------------------------------------------------------
    # Date Detection
    # ---------------------------------------------------------

    def _is_date(self, line: str) -> bool:

        line = line.strip()

        patterns = [

            # June 2024
            r"^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4}$",

            # Jan 2022 - Present
            r"^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4}\s*[-–—]\s*(Present|(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4})$",

            # 2022 - 2024
            r"^\d{4}\s*[-–—]\s*(Present|\d{4})$",
        ]

        return any(
            re.match(pattern, line, re.IGNORECASE)
            for pattern in patterns
        )

    # ---------------------------------------------------------
    # Job Title & Company
    # ---------------------------------------------------------

    def _extract_job_and_company(
        self,
        block: list[str],
    ) -> tuple[str, str]:

        heading = block[0]

        for separator in (" - ", " – ", " — ", " | ", " @ "):

            if separator in heading:

                job, company = heading.split(separator, 1)

                return (
                    job.strip(),
                    company.strip(),
                )

        return heading.strip(), ""

    # ---------------------------------------------------------
    # Dates
    # ---------------------------------------------------------

    def _extract_dates(
        self,
        block: list[str],
    ) -> tuple[str, str]:

        if len(block) < 2:
            return "", ""

        line = block[1].strip()

        # June 2024
        if re.match(
            r"^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4}$",
            line,
            re.IGNORECASE,
        ):
            return line, ""

        # Jan 2022 - Present
        match = re.match(
            r"^(.+?)\s*[-–—]\s*(Present|.+)$",
            line,
            re.IGNORECASE,
        )

        if match:
            return (
                match.group(1).strip(),
                match.group(2).strip(),
            )

        return "", ""

    # ---------------------------------------------------------
    # Description
    # ---------------------------------------------------------

    def _extract_description(
        self,
        block: list[str],
    ) -> list[str]:

        if len(block) <= 2:
            return []

        return [
            line.strip()
            for line in block[2:]
            if line.strip()
        ]