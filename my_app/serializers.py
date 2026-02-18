from rest_framework import serializers

from .models import Sample


class SampleCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sample
        fields = ["name", "description"]

    def create(self, validated_data):
        return Sample.objects.create(**validated_data)


class SampleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sample
        fields = [
            "uuid",
            "name",
            "description",
        ]


class SampleDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sample
        fields = [
            "uuid",
            "name",
            "description",
            "created_at",
            "updated_at",
        ]
