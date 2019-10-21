from rest_framework import serializers
from API.models import Classroom

class ClassroomListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ["id", "subject", "year", "teacher"]


class ClassroomDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ["id", "name", "subject", "year", "teacher"]


class ClassroomUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ["name", "subject", "year"]


class ClassroomreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ["name", "subject", "year"]