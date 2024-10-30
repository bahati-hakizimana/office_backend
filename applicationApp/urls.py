from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import ApplicantListView, ApplicantDetailView

urlpatterns = [
    path('api/applicants/', ApplicantListView.as_view(), name='applicant-list'),
    path('api/applicants/<int:pk>/', ApplicantDetailView.as_view(), name='applicant-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
