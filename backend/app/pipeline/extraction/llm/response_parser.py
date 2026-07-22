# app/pipeline/extraction/llm/response_parser.py

import json
import re


class ResponseParser:

    @staticmethod
    def parse(response: str) -> dict:
        """
        Convert the LLM response into a Python dictionary.
        """

        response = re.sub(r"```json", "", response)
        response = re.sub(r"```", "", response)

        response = response.strip()

        return json.loads(response)