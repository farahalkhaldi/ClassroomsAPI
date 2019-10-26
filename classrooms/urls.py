

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views as viewsa
from API import views as viewsb

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('classrooms/', viewsa.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', viewsa.classroom_detail, name='classroom-detail'),
    path('classrooms/create/', viewsa.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', viewsa.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', viewsa.classroom_delete, name='classroom-delete'),
    path('login/', TokenObtainPairView.as_view(), name="login"),

    path('classrooms/api/', viewsb.ClassroomList.as_view(), name='list'),
    path('classrooms/<int:classroom_id>/api/', viewsb.ClassroomDetails.as_view(), name='detail'),
    path('classrooms/create/api/', viewsb.ClassroomCreateView.as_view(), name='create'),
    path('classrooms/<int:classroom_id>/update/api/', viewsb.UpdateClassroom.as_view(), name='update'),
    path('classrooms/<int:classroom_id>/delete/api/', viewsb.DeleteClassroom.as_view(), name='delete'), 

]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)