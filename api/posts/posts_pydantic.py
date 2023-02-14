from pydantic import BaseModel, Field
from typing import Optional


class Post(BaseModel):
    id: int
    header: str
    main_text: str
    publish_date: str
