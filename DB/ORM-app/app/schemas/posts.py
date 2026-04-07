from pydantic import BaseModel

class PostCreate(BaseModel):
    author: str
    content: str


class PostUpdate(BaseModel):
    author: str
    content: str