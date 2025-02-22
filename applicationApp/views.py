from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Applicant
from .serializers import ApplicantSerializer

class ApplicantListView(ListCreateAPIView):
    serializer_class = ApplicantSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Admins can see all applications, regular users see only their own"""
        user = self.request.user
        if user.is_staff:  # Check if the user is an admin
            return Applicant.objects.all()
        return Applicant.objects.filter(created_by=user)

    def perform_create(self, serializer):
        """Set the created_by field to the authenticated user"""
        serializer.save(created_by=self.request.user)


class ApplicantDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ApplicantSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Admins can access all applications, users can access only their own"""
        user = self.request.user
        if user.is_staff:
            return Applicant.objects.all()
        return Applicant.objects.filter(created_by=user)

    def patch(self, request, *args, **kwargs):
        """Update the status of an applicant"""
        applicant = self.get_object()
        new_status = request.data.get("status")

        if new_status in dict(Applicant.STATUS_CHOICES):
            applicant.status = new_status
            applicant.save()
            return Response(
                {"message": f"Application status updated to {new_status}"},
                status=status.HTTP_200_OK
            )

        return Response(
            {"error": "Invalid status. Choose from 'pending', 'approved', or 'denied'."},
            status=status.HTTP_400_BAD_REQUEST
        )

