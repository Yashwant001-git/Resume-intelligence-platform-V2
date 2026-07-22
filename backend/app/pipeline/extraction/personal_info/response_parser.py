import json

from app.models.personal_info import PersonalInfo


class ResponseParser:
    """
    Parse the JSON response returned by the LLM into a PersonalInfo object.
    """

    @staticmethod
    def parse(response: str) -> PersonalInfo:
        """
        Parse the raw LLM response.

        Args:
            response: Raw JSON string returned by Ollama.

        Returns:
            PersonalInfo object.
        """

        try:
            data = json.loads(response)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON returned by Ollama.\n{response}") from e

        return PersonalInfo(
            full_name=data.get("full_name", "").strip(),
            job_title=data.get("job_title", "").strip(),
            email=data.get("email", "").strip(),
            phone=data.get("phone", "").strip(),
            location=data.get("location", "").strip(),
            linkedin=data.get("linkedin", "").strip(),
            github=data.get("github", "").strip(),
            portfolio=data.get("portfolio", "").strip(),
        )