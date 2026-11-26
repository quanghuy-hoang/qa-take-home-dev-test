import pytest

from signup import validate


def test_happy_path_has_no_problems():
    assert validate("An Nguyen", "an@example.com", "s3cret-pass") == []


@pytest.mark.parametrize(
    ("name", "email", "password", "problem"),
    [
        ("", "an@example.com", "s3cret-pass", "name_required"),
        ("An", "not-an-email", "s3cret-pass", "email_invalid"),
        ("An", "an@example.com", "short1", "password_too_short"),
        ("An", "an@example.com", "onlyletters", "password_too_simple"),
    ],
)
def test_each_field_is_validated(name, email, password, problem):
    assert problem in validate(name, email, password)


def test_whitespace_only_name_is_rejected():
    assert "name_required" in validate("   ", "an@example.com", "s3cret-pass")


def test_email_with_surrounding_spaces_is_accepted():
    assert validate("An", "  an@example.com  ", "s3cret-pass") == []
