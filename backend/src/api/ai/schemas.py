from pydantic import BaseModel, Field
from langchain_ollama import ChatOllama



class EmailMessageSchema(BaseModel):
    subject: str
    contents: str
    invalid_request: bool | None = Field(default=None)
