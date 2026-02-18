from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sample
from .serializers import (
    SampleCreateSerializer,
    SampleDetailSerializer,
    SampleListSerializer,
)


class SampleListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        samples = Sample.objects.all()
        return Response(
            SampleListSerializer(samples, many=True).data, status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = SampleCreateSerializer(
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        sample = serializer.save()

        return Response(
            SampleDetailSerializer(sample).data, status=status.HTTP_201_CREATED
        )


class SampleDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, sample_uuid):
        sample = get_object_or_404(
            Sample,
            uuid=sample_uuid,
        )

        return Response(SampleDetailSerializer(sample).data, status=status.HTTP_200_OK)
