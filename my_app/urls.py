from django.urls import path

from .views import SampleDetailAPIView, SampleListCreateAPIView

urlpatterns = [
    path("samples", SampleListCreateAPIView.as_view(), name="sample-list-create"),
    path(
        "samples/<uuid:sample_uuid>",
        SampleDetailAPIView.as_view(),
        name="sample-detail",
    ),
]
