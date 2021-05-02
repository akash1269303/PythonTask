from rest_framework.serializers import ModelSerializer
from .models import Link


class Linkserializers(ModelSerializer):
    class Meta:
        model=Link
        fields='__all__'
