from app.models.candidate import Candidate
from app.models.document import Document

# LLM
from app.pipeline.extraction.extractors.llm_extractor.llm_extractor import (
    LLMExtractor,
)
from app.pipeline.extraction.extractors.llm_extractor.personal_info_extractor import (
    PersonalInfoExtractor,
)
from app.pipeline.extraction.extractors.llm_extractor.education_extractor import (
    EducationExtractor,
)
from app.pipeline.extraction.extractors.llm_extractor.certification_extractor import (
    CertificationExtractor,
)

# Rule Based
from app.pipeline.extraction.extractors.skills_extractor import SkillsExtractor
from app.pipeline.extraction.extractors.experience_extractor import (
    ExperienceExtractor,
)
from app.pipeline.extraction.extractors.project_extractor import ProjectExtractor

from app.utils.logger import logger


class ExtractionManager:

    def __init__(self):

        # LLM
        self.llm_extractor = LLMExtractor()
        self.personal_info_extractor = PersonalInfoExtractor()
        self.education_extractor = EducationExtractor()
        self.certification_extractor = CertificationExtractor()

        # Rule Based
        self.skills_extractor = SkillsExtractor()
        self.experience_extractor = ExperienceExtractor()
        self.project_extractor = ProjectExtractor()

    def extract(self, document: Document) -> Candidate:

        logger.info("Starting extraction pipeline...")

        candidate = Candidate()

        # ======================================================
        # ONE LLM CALL
        # ======================================================

        llm_response = self.llm_extractor.extract(document)

        # ======================================================
        # LLM Extractors
        # ======================================================

        candidate.personal_info = (
            self.personal_info_extractor.extract(llm_response)
        )

        candidate.education = (
            self.education_extractor.extract(llm_response)
        )

        candidate.certifications = (
            self.certification_extractor.extract(llm_response)
        )

        # ======================================================
        # Rule-Based Extractors
        # ======================================================

        # candidate.skills = self.skills_extractor.extract(document)
        candidate.skills = self.skills_extractor.extract(
            document.sections.skills
        )

        # candidate.experience = self.experience_extractor.extract(document)
        candidate.experience = self.experience_extractor.extract(
            document.sections.experience
        )

        # candidate.projects = self.project_extractor.extract(document)
        candidate.projects = self.project_extractor.extract(
            document.sections.projects
        )

        logger.info("Extraction pipeline completed.")

        return candidate