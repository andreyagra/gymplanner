from django.core.exceptions import ValidationError


class UserValidator:

    def validate_password_strength(value):
        if len(value) < 6:
            raise ValidationError("Password must be at least 6 characters long.")
        if not any(char.isdigit() for char in value):
            raise ValidationError("Password must contain at least 1 number.")
        if not any(char.isalpha() for char in value):
            raise ValidationError("Password must contain at least 1 letter.")
        if not any(char in "!@#$%^&*()_+=-{}[]|\\:;\"'<>,.?/~`" for char in value):
            raise ValidationError(
                "Password must contain at least 1 special character (!@#$%^&*()_+=-{}[]|\\:;\"'<>,.?/~`).")
