from pydantic import BaseModel

from private_gpt.settings.settings_loader import load_active_profiles


class ServerSettings(BaseModel):
    env_name: str
    port: int


class LLMSettings(BaseModel):
    mode: str


class LocalSettings(BaseModel):
    llm_hf_repo_id: str
    llm_hf_model_file: str
    embedding_hf_model_name: str


class SagemakerSettings(BaseModel):
    endpoint_name: str


class OpenAISettings(BaseModel):
    api_key: str


class UISettings(BaseModel):
    enabled: bool
    path: str


class Settings(BaseModel):
    server: ServerSettings
    ui: UISettings
    llm: LLMSettings
    local: LocalSettings
    sagemaker: SagemakerSettings
    openai: OpenAISettings


settings = Settings(**load_active_profiles())
