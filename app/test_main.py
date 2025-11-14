from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password, exception",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False)
    ]
)
def test_check_password(password: str, exception: bool) -> None:
    assert check_password(password) == exception
