from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@1Aa8", True),
        ("Short1@", False),
        ("NoDigit@Aa", False),
        ("Has Space1@", False),
        ("VeryLongPassword1@A", False)
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
