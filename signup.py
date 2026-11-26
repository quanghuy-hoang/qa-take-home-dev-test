"""A tiny sign-up form validator, the system under test."""

import re

EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def validate(name: str, email: str, password: str) -> list[str]:
    """Return the list of problems with a sign-up; empty means valid."""
    problems = []
    if not name.strip():
        problems.append("name_required")
    if not EMAIL.match(email.strip()):
        problems.append("email_invalid")
    if len(password) < 8:
        problems.append("password_too_short")
    elif password.isalpha() or password.isdigit():
        problems.append("password_too_simple")
    return problems
