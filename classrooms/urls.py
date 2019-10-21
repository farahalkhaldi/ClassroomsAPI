
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views
from API import views as viewsb
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),


    path('API/classrooms/', viewsb.ClassroomList.as_view(), name='classroomapi-list'),
    path('API/classrooms/<int:classroom_id>/', viewsb.ClassroomDetail.as_view(), name='classroomapi-detail'),

    path('API/classrooms/create', viewsb.ClassroomCreate.as_view(), name='classroomapi-create'),
    path('API/classrooms/<int:classroom_id>/update/', viewsb.ClassroomUpdate.as_view(), name='classroomapi-update'),
    path('API/classrooms/<int:classroom_id>/delete/', viewsb.ClassroomDelete.as_view(), name='classroomapi-delete'),

	path('login/', TokenObtainPairView.as_view(), name='login'),
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

