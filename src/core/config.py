from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Config(BaseSettings):
    """全局配置
    """

    TIME_ZONE: str = Field(default="Asia/Shanghai", description="时区")
    SWAGGER_OPENAPI_URL: str = Field(default="", title="Swagger API文档地址", description="线上环境建议隐藏该文档，即设置为空字符串")
    SWAGGER_DOCS_URL: str = Field(default="", title="Swagger UI地址", description="线上环境建议隐藏该文档，即设置为空字符串")
    SWAGGER_REDOC_URL: str = Field(default="", title="Redoc UI地址", description="线上环境建议隐藏该文档，即设置为空字符串")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        env_ignore_empty=True,
    )


@lru_cache
def get_config() -> Config:
    """获取全局配置

    Returns:
        Config: 全局配置
    """
    return Config()
