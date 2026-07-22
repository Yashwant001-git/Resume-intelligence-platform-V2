# app/llm/ollama_client.py

from ollama import Client

from app.config.settings import settings
from app.utils.logger import logger
from pprint import pprint


class OllamaClient:
    """
    Simple wrapper around the Ollama client.
    """

    def __init__(self):
        self.client = Client(host=settings.OLLAMA_BASE_URL)
        self.model = settings.OLLAMA_MODEL

    def generate(self, prompt: str) -> str:
        """
        Send a prompt to the configured Ollama model.

        Args:
            prompt: Prompt to send to the model.

        Returns:
            Model response as a string.
        """

        logger.info("Sending request to Ollama...")

        response = self.client.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )



        # return response["message"]["content"].strip()

        logger.info("=" * 60)
        logger.info("OLLAMA REQUEST METRICS")
        logger.info("=" * 60)
        logger.info(f"Model            : {response.model}")
        logger.info(f"Prompt Tokens    : {response.prompt_eval_count}")
        logger.info(f"Output Tokens    : {response.eval_count}")
        logger.info(f"Total Tokens     : {response.prompt_eval_count + response.eval_count}")
        logger.info(f"Load Time        : {response.load_duration / 1e9:.2f} sec")
        logger.info(f"Prompt Eval Time : {response.prompt_eval_duration / 1e9:.2f} sec")
        logger.info(f"Generation Time  : {response.eval_duration / 1e9:.2f} sec")
        logger.info(f"Total Time       : {response.total_duration / 1e9:.2f} sec")
        logger.info("=" * 60)

        return response.message.content.strip()