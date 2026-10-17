from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    whatsapp_verify_token: str = "changeme"
    whatsapp_access_token: str = ""
    whatsapp_phone_number_id: str = ""
    groq_api_key: str = ""
    groq_model: str = "llama-3.3-70b-versatile"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
