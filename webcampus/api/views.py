from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import authentication, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.db.models import Q, Count, Exists
from rest_framework.viewsets import ModelViewSet
from itertools import chain
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

import operator
from rest_framework.response import Response
from datetime import datetime
from webcampus.models import *
from .serializers import *
from rest_framework.decorators import api_view


class SubjectView(ListAPIView):
	queryset = Subject.objects.all()
	permission_classes = (AllowAny,)
	serializer_class = SubjectSerializer


@api_view(['GET'])
def get_course(request, course_slug):
    try:
        course = Course.objects.get(name_slug=course_slug)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # serializer = SnippetSerializer(snippet, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        pass

    elif request.method == 'DELETE':
        # snippet.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)
        pass

class SyllabusView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, course_slug, format=None):
        try:
            course = Course.objects.get(name_slug=course_slug)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = SyllabusSerializer(course)
            return Response(serializer.data)


class LessonView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, course_slug, chapter_slug, format=None):
        try:
            course = Course.objects.get(name_slug=course_slug)
            chapter = Chapter.objects.get(course=course, name_slug=chapter_slug)
        except Chapter.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = ChapterShortSerializer(chapter, many=False)
            return Response(serializer.data)

class StepView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, course_slug, chapter_slug, step_slug, format=None):
        try:
            step = Step.objects.get(chapter__course__name_slug=course_slug, chapter__name_slug=chapter_slug, title_slug=step_slug)
            texts = step.texts.all()
            videos = step.videos.filter(visible = True)
            htmlblocks = step.htmlblocks.all()
        except Step.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            content = []
            step_serializer = StepFullSerializer(step)
            for i in TextSerializer(texts, many=True).data:
                i.update({ "type": "text" })
                content.append(dict(i))
            for i in VideoSerializer(videos, many=True).data:
                i.update({ "type": "video" })
                content.append(dict(i))
            for i in HTMLBlockSerializer(htmlblocks, many=True).data:
                i.update({ "type": "html" })
                content.append(dict(i))
        
            result = step_serializer.data
            sorted_content = sorted(content, key=lambda k: k['created'])
            result.update({ "content": sorted_content })

            return Response(result)



