from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Resume Intelligence Platform"

    DEBUG: bool = False

    # OLLAMA_URL: str
    # OLLAMA_MODEL: str

    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "qwen2.5:3b"

    LOG_LEVEL: str = "INFO"

    UPLOAD_DIR: str = "backend/data/input"
    OUTPUT_DIR: str = "backend/data/output"

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    class Config:
        env_file = ".env"


settings = Settings()