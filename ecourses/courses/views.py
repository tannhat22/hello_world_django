from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse
from django.views import View

from .models import Course, Lesson, Tag
from .serializers import *

# Create your views here.
def index(request):
    return render(request, template_name='index.html', context={'name': 'Tan Nhat'})

def welcome(request, year):
    return HttpResponse("HELLO EVERYONE " + str(year))

def welcome2(request, year):
    return HttpResponse("HELLO EVERYONE " + str(year))


class TestView(View):
    def get(self, request):
        return HttpResponse("Testing")

    def post(self, request):
        pass

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def get_permissions(self):
    #     if self.action == 'list':
    #         return [permissions.AllowAny()]
    #     return [permissions.IsAuthenticated()]
    
class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.filter(active=True)
    serializer_class = LessonSerializer

    # Ẩn lesson (active=False)
    # /lessons/{pk}/hide-lesson
    @action(methods=['post'], detail=True, url_path="hide-lesson", url_name="hide-lesson")
    def hide_lesson(self, request, pk):
        try:
            l = Lesson.objects.get(pk=pk)
            l.active = False
            l.save()
            return Response(data=LessonSerializer(l, context={'request': request}).data, status=status.HTTP_200_OK)
        except Lesson.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)