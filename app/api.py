from fastapi import FastAPI
from app.config import settings
from app.models import ProductInput, DescriptionOutput
from app.services.desc_engine import transform_features_to_benefits

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.post("/generate-description", response_model=DescriptionOutput)
def generate_description(prod: ProductInput):
    s, l, b, k = transform_features_to_benefits(prod.product_name, prod.raw_features, prod.category)
    return DescriptionOutput(
        product_name=prod.product_name,
        short_pitch=s,
        long_description=l,
        bullet_benefits=b,
        seo_keywords=k
    )
