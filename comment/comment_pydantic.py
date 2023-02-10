from pydantic import BaseModel


class Comment(BaseModel):
    id: int
    text: str
    likes: int
    date: str
