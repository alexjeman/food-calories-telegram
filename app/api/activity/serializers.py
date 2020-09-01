from datetime import datetime
from pydantic import BaseModel


class ActivityCategoryDetail(BaseModel):
    date_created: datetime
    date_modified: datetime
    title: str
    description: str = None


class ActivityCategoryCreate(BaseModel):
    title: str
    description: str = None


class ActivityDetail(BaseModel):
    date_created: datetime
    date_modified: datetime
    title: str
    description: str = None
    rating: int
    category: ActivityCategoryDetail
    energy: int


class ActivityCreate(BaseModel):
    title: str
    description: str = None
    category: int
    energy: int
