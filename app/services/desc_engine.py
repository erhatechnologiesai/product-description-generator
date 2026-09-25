def transform_features_to_benefits(name: str, features: list, category: str):
    short = f"The {name} delivers unprecedented performance in the {category} space with turnkey efficiency."
    long_d = (
        f"Designed specifically for modern operators, the {name} bridges the gap between raw capability and effortless usability. "
        f"By incorporating {', '.join(features[:3])}, it transforms daily workflows into streamlined automated pipelines."
    )
    benefits = [f"Gain competitive edge with {f}." for f in features]
    keywords = [name.lower(), category.lower(), "enterprise automation", "productivity"]
    return short, long_d, benefits, keywords
