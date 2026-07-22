import re

from app.models.project import Project


class ProjectExtractor:

    def extract(self, section: list[str]) -> list[Project]:

        if not section:
            return []

        blocks = self._build_blocks(section)

        projects = []

        for block in blocks:

            project = Project()

            project.title = self._extract_title(block)

            project.technologies = self._extract_technologies(block)

            project.description = self._extract_description(block)

            project.github = self._extract_github(block)

            projects.append(project)

        return projects

    # ---------------------------------------------------------
    # Build Project Blocks
    # ---------------------------------------------------------

    def _build_blocks(self, lines: list[str]) -> list[list[str]]:

        blocks = []
        current = []

        for line in lines:

            line = line.strip()

            if not line:
                continue

            if self._is_project_heading(line):

                if current:
                    blocks.append(current)

                current = [line]

            else:
                current.append(line)

        if current:
            blocks.append(current)

        return blocks

    # ---------------------------------------------------------
    # Project Heading
    # ---------------------------------------------------------

    def _is_project_heading(self, line: str) -> bool:

        separators = (
            " | ",
            " - ",
            " – ",
            " — ",
        )

        return any(separator in line for separator in separators)

    # ---------------------------------------------------------
    # Project Title
    # ---------------------------------------------------------

    def _extract_title(self, block: list[str]) -> str:

        if not block:
            return ""

        heading = block[0]

        for separator in (" | ", " - ", " – ", " — "):

            if separator in heading:
                return heading.split(separator, 1)[0].strip()

        return heading.strip()

    # ---------------------------------------------------------
    # Technologies
    # ---------------------------------------------------------

    def _extract_technologies(self, block: list[str]) -> list[str]:

        for line in block:

            if line.lower().startswith("technologies"):

                _, techs = line.split(":", 1)

                return [
                    tech.strip()
                    for tech in techs.split(",")
                    if tech.strip()
                ]

        return []

    # ---------------------------------------------------------
    # Description
    # ---------------------------------------------------------

    def _extract_description(self, block: list[str]) -> list[str]:

        description = []

        for line in block[1:]:

            if line.lower().startswith("technologies"):
                continue

            if line.startswith("GitHub"):
                continue

            description.append(line.strip())

        return description

    # ---------------------------------------------------------
    # GitHub
    # ---------------------------------------------------------

    def _extract_github(self, block: list[str]) -> str:

        pattern = r"https?://[^\s]+"

        for line in block:

            match = re.search(pattern, line)

            if match:
                return match.group()

        return ""