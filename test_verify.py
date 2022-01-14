import pytest
import verify


@pytest.mark.parametrize("password", ("Gaash1gh", "ga7shdgG"))
def test_good_passwords(password):
  verify.verify(password)


@pytest.mark.parametrize("password", ("1234567", "1", ""))
def test_verify_length_too_short(password):
  with pytest.raises(verify.PasswordTooShort):
    verify.verify(password)


def test_input_should_not_be_null():
  with pytest.raises(verify.NoneInput):
    verify.verify(None)


def test_uppercase_letter():
  with pytest.raises(verify.UppercaseError):
    verify.verify("1234u5678")


def test_lowercase_letter():
  with pytest.raises(verify.LowercaseError):
    verify.verify("1234U5678")

