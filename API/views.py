from django.shortcuts import render
from classes.models import Classroom
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .serializers import ClassroomSerializer, ClassroomDetailsSerializer, CreateSerializer, UpdateSerializer
# from rest_framework_jwt.settings import api_settings

class ClassroomList(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomSerializer

class ClassroomDetails(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomDetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class ClassroomCreateView(CreateAPIView):
	serializer_class = CreateSerializer

	def perform_create(self, serializer):
		serializer.save(teacher=self.request.user)

class UpdateClassroom(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = UpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class DeleteClassroom(DestroyAPIView):
	queryset = Classroom.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

