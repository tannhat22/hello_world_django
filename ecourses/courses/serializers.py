from rest_framework.serializers import ModelSerializer

from .models import Course, Lesson, Tag, User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password','avatar']
        extra_kwargs = {
            'password': {'write_only': 'true'}
        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "subject", "image", "created_date", "category"]

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]

class LessonSerializer(ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Lesson
        fields = ["id", "subject", "image", "created_date", "content", "course", "tags"]