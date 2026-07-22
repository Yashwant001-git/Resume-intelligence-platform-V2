import re

from app.models.skills import Skills
from app.utils.logger import logger


class SkillsExtractor:

    CATEGORY_MAPPING = {
        "languages": "programming_languages",
        "programming languages": "programming_languages",

        "frameworks": "frameworks",

        "libraries": "libraries",

        "database": "databases",
        "databases": "databases",

        "cloud": "cloud",
        "cloud platforms": "cloud",

        "tools": "tools",
        "tools & deployment": "tools",
        "deployment": "tools",

        "soft skills": "soft_skills",

        "ai / ml domains": "ai_ml_domains",
        "ai":'ai_ml_domains',
        "ai framework":"ai_ml_domains",
        
        "domains": "others",
        "others": "others",
    }

    def extract(self, section: list[str]) -> Skills:

        logger.info("Extracting skills...")

        skills = Skills()

        current_category = None

        for line in section:

            line = line.strip()

            if not line:
                continue

            # Handle lines containing a category
            if ":" in line:

                header, values = line.split(":", 1)

                current_category = self.CATEGORY_MAPPING.get(
                    header.lower().strip(),
                    "others",
                )

                if values.strip():
                    self._add_skills(
                        skills,
                        current_category,
                        values,
                    )

            else:

                if current_category:
                    self._add_skills(
                        skills,
                        current_category,
                        line,
                    )

        logger.info("Skills extracted successfully.")

        return skills

    def _add_skills(
        self,
        skills: Skills,
        category: str,
        values: str,
    ) -> None:

        values = [
            skill.strip()
            for skill in re.split(r",|;", values)
            if skill.strip()
        ]

        getattr(skills, category).extend(values)