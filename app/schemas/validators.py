import re
from typing import Annotated

from pydantic import AfterValidator


def validate_password(value: str) -> str:
    if len(value) < 10:
        raise ValueError("Password must be at least 10 characters long")
    if not re.search(r"[A-Z]", value):
        raise ValueError("Password must contain at least one uppercase letter (A–Z)")
    if not re.search(r"[a-z]", value):
        raise ValueError("Password must contain at least one lowercase letter (a–z)")
    if not re.search(r"\d", value):
        raise ValueError("Password must contain at least one digit (0–9)")
    if not re.search(r"[!@#$%^&*()]", value):
        raise ValueError(
            "Password must contain at least one special character: !@#$%^&*()"
        )
    return value


Password = Annotated[str, AfterValidator(validate_password)]
