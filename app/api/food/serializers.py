from typing import List
from datetime import datetime
from pydantic import BaseModel


class FoodPortionDetail(BaseModel):
    date_created: datetime
    date_modified: datetime
    title: str
    description: str = None
    weight: int


class FoodPortionCreate(BaseModel):
    title: str
    description: str = None
    weight: int


class FoodCategoryDetail(BaseModel):
    date_created: datetime
    date_modified: datetime
    title: str
    description: str = None


class FoodCategoryCreate(BaseModel):
    title: str
    description: str = None


class FoodDetail(BaseModel):
    date_created: datetime
    date_modified: datetime
    rating: int
    title: str
    description: str = None
    category: FoodCategoryDetail
    portions: List[FoodPortionDetail]
    energy: int
    protein: float
    carbohydrate: float
    fat: float
    fiber: float
    sugar: float
    salt: float


class FoodCreate(BaseModel):
    title: str
    description: str = None
    category: int
    portions: List[int]
    energy: int
    protein: float
    carbohydrate: float
    fat: float
    fiber: float
    sugar: float
    salt: float
