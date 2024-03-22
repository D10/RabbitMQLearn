

def number_validator(value: str) -> str | None:
    return value if value.replace('.', '').isdigit() else None
