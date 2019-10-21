from django.shortcuts import render
from API.models import Classroom
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from .serializers import ClassroomListSerializer, ClassroomDetailSerializer, ClassroomUpdateSerializer, ClassroomreateSerializer

class ClassroomList(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomListSerializer

class ClassroomDetail(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomDetailSerializer
	lookup_field = "id"
	lookup_url_kwarg = "classroom_id"

class ClassroomUpdate(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomUpdateSerializer
	lookup_field = "id"
	lookup_url_kwarg = "classroom_id"

class ClassroomDelete(DestroyAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomListSerializer
	lookup_field = "id"
	lookup_url_kwarg = "classroom_id"

class ClassroomCreate(CreateAPIView):
	serializer_class = ClassroomreateSerializer

	def perform_create(self, serializer):
		classroom_id = self.kwargs.get("classroom_id")
		classroom_object = Classroom.objects.get(id=classroom_id)
		serializer.save(teacher=self, =self.request.user)