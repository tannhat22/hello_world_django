from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from . import views
# from .admin import admin_site

router = DefaultRouter()
router.register('courses', views.CourseViewSet)
router.register('lessons', views.LessonViewSet)
router.register('users', views.UserViewSet)


urlpatterns = [
    # path('', views.index, name="index"),
    # path('welcome/<int:year>/', views.welcome, name="welcome"),
    # path('test/', views.TestView.as_view()),
    # re_path(r'welcome2/(?P<year>[0-9]{4})/$', views.welcome2, name="welcome2"),
    # path('admin/', admin_site.urls),
    path('',include(router.urls)),
]