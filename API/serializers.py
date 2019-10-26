from rest_framework import serializers
from classes.models import Classroom


class ClassroomSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['subject', 'year', 'teacher', 'id']

class ClassroomDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['name', 'subject', 'year', 'teacher', 'id']

class CreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = [ 'name', 'subject', 'year', 'teacher' ]

class UpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = [ 'name', 'subject', 'year']