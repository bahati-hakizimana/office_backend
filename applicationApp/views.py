from django.shortcuts import render

# Create your views here.
# Create your views here.
# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Applicant
from .serializers import ApplicantSerializer

# View to list all applications and create new ones
class ApplicantListView(ListCreateAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

# View to retrieve, update status, and delete a specific application
class ApplicantDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

    def put(self, request, *args, **kwargs):
        applicant = self.get_object()
        new_status = request.data.get("status")  # Renamed variable to avoid conflict
        if new_status and new_status in [choice[0] for choice in Applicant.STATUS_CHOICES]:
            applicant.status = new_status
            applicant.save()
            return Response({"status": f"Application status updated to {new_status}"}, status=new_status.HTTP_200_OK)
        return Response({"error": "Invalid status"}, status=new_status_status.HTTP_400_BAD_REQUEST)