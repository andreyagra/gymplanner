from rest_framework import serializers
from planner_app.models.user import User
from planner_app.validators.user_validator import UserValidator


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        validator = UserValidator
        fields = ['email', 'password', 'profile']
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 6, 'validators': [validator.validate_password_strength]}
        }

    def create(self, validated_data):
        # Ensure the password is saved using `set_password`
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
