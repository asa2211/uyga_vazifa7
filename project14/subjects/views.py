from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from .models import SubjectModel
from .serializer import SubjectSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


class SubjectAllView(APIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'email', 'subject_name']

    def get(self, *args, **kwargs):
        all = SubjectModel.objects.all()
        serializer = SubjectSerializers(all, many=True)
        return Response(serializer.data)


class DetailSubjectView(APIView):
    def get(self, *args, **kwargs):
        sub_id = kwargs['sub_id']
        subject = get_object_or_404(SubjectModel, id=sub_id)
        serializer = SubjectSerializers(subject)
        return Response(serializer.data)


class EmailSubjectView(APIView):
    def get(self, *args, **kwargs):
        sub_email = kwargs['sub_email']
        subject = get_object_or_404(SubjectModel, email=sub_email)
        serializer = SubjectSerializers(subject)
        return Response(serializer.data)


class SearchView(generics.ListAPIView):
    queryset = SubjectModel.objects.all()
    serializer_class = SubjectSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'email', 'subject_name']
