from . import serializers
from rest_framework import generics, permissions
from . import serializers
from . import models
class VendorList(generics.ListAPIView):
        queryset = models.Vendor.objects.all()
        serializer_class = serializers.VendorSerializers
        permission_classes = [permissions.IsAuthenticated]


