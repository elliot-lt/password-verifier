# Create a Password verifications class or function for the purposes of password verification.  Verification will fail if any one of the rules mentioned does not pass.

#    Implement the following rules:
#
#        - password should be larger than 8 chars
#
#        - password should not be null
#
#        - password should have one uppercase letter at least
#
#        - password should have one lowercase letter at least
#
#        - password should have one number at least
#
#     Each one of these should throw an exception with a different message of your choosing

class VerifyError(Exception):
  pass

class NoneInput(VerifyError):
  pass

class PasswordTooShort(VerifyError):
  pass

class UppercaseError(VerifyError):
  pass

class LowercaseError(VerifyError):
  pass

def verify(password: str):
  if password is None:
    raise NoneInput()
  if len(password) < 8:
    raise PasswordTooShort()
  if not any(i.islower() for i in password):
    raise LowercaseError("Password should contain at least one lowercase character")
  if not any(i.isupper() for i in password):
    raise UppercaseError()


