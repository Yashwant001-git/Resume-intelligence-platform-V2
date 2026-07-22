# import requests

# from config import API_URL


# def upload_resume(file):

#     files = {
#         "file": (
#             file.name,
#             file.getvalue(),
#             "application/pdf",
#         )
#     }

#     response = requests.post(
#         API_URL,
#         files=files,
#     )

#     return response


"""
API Service
"""

import requests

from utils.constants import (
    API_BASE_URL,
    EXTRACT_ENDPOINT,
)


class APIService:

    @staticmethod
    def extract_resume(file):

        files = {
            "file": (
                file.name,
                file.getvalue(),
                "application/pdf",
            )
        }

        response = requests.post(
            f"{API_BASE_URL}{EXTRACT_ENDPOINT}",
            files=files,
        )

        response.raise_for_status()

        return response.json()

    @staticmethod
    def download_excel():

        response = requests.get(
            f"{API_BASE_URL}/api/v1/resume/download"
        )

        response.raise_for_status()

        return response.content