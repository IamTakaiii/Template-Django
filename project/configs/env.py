from os import getenv

from pydantic import BaseModel

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file if it exists

class EnvModel(BaseModel):
    SECRET_KEY: str
    DEBUG: bool
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    CORS_ALLOW_ALL_ORIGINS: bool
    CORS_ALLOWED_ORIGINS: list[str] = []
    AWS_S3_ACCESS_KEY_ID: str
    AWS_S3_SECRET_ACCESS_KEY: str
    AWS_STORAGE_BUCKET_NAME: str
    AWS_S3_REGION_NAME: str
    AWS_S3_SIGNATURE_VERSION: str = "s3v4"
    AWS_S3_FILE_OVERWRITE: bool = False
    AWS_DEFAULT_ACL: str = "public-read"
    AWS_S3_ENDPOINT_URL: str


ENV = EnvModel(
    SECRET_KEY=getenv("SECRET_KEY"),  # type: ignore
    DEBUG=getenv("DEBUG", "False").lower() == "true",  # type: ignore
    DB_USER=getenv("DB_USER"),  # type: ignore
    DB_PASSWORD=getenv("DB_PASSWORD"),  # type: ignore
    DB_HOST=getenv("DB_HOST"),  # type: ignore
    DB_PORT=getenv("DB_PORT"),  # type: ignore
    DB_NAME=getenv("DB_NAME"),  # type: ignore
    CORS_ALLOW_ALL_ORIGINS=getenv("CORS_ALLOW_ALL_ORIGINS", "False").lower() == "true",  # type: ignore
    CORS_ALLOWED_ORIGINS=getenv("CORS_ALLOWED_ORIGINS", "").split(","),  # type: ignore
    AWS_S3_ACCESS_KEY_ID=getenv("AWS_S3_ACCESS_KEY_ID", ""),  # type: ignore
    AWS_S3_SECRET_ACCESS_KEY=getenv("AWS_S3_SECRET_ACCESS_KEY", ""),  # type: ignore
    AWS_STORAGE_BUCKET_NAME=getenv("AWS_STORAGE_BUCKET_NAME", ""),  # type: ignore
    AWS_S3_REGION_NAME=getenv("AWS_S3_REGION_NAME", ""),  # type: ignore
    AWS_S3_SIGNATURE_VERSION=getenv("AWS_S3_SIGNATURE_VERSION", "s3v4"),  # type: ignore
    AWS_S3_FILE_OVERWRITE=getenv("AWS_S3_FILE_OVERWRITE", "False").lower() == "true",  # type: ignore
    AWS_DEFAULT_ACL=getenv("AWS_DEFAULT_ACL", "public-read"),  # type: ignore
    AWS_S3_ENDPOINT_URL=getenv("AWS_S3_ENDPOINT_URL", ""),  # type: ignore
)
