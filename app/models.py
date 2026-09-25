from pydantic import BaseModel
from typing import List

class ProductInput(BaseModel):
    product_name: str
    raw_features: List[str]
    category: str

class DescriptionOutput(BaseModel):
    product_name: str
    short_pitch: str
    long_description: str
    bullet_benefits: List[str]
    seo_keywords: List[str]
