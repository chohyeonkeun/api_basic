"""
관례적으로 serialize.py라고 명명 (rest에서는 form이 아닌 serializer 사용)
"""
from rest_framework import serializers

from .models import User

# 유저 목록에 출력될 형식
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'message', 'profile']

# 회원 가입할 때 필요한 필드들에 관한 시리얼라이저
class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'message', 'profile']
    # 비밀번호 암호화하여 설정할 수 있도록 해주는 함수
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        # create view 는 항상 방금 만든 객체 반환
        return user

class UserModifySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password', 'first_name', 'last_name', 'email', 'message', 'profile']

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if value:
                setattr(instance, key, value)
            if key == 'password' and value:
                instance.set_password(value)
            elif value:
                setattr(instance, key, value)
        instance.save()

        return instance

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'message', 'profile', 'is_superuser']
