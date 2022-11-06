from .models import Roteiro
import django_filters

class RoteiroFilter(django_filters.FilterSet):

    class Meta:
        model = Roteiro
        fields = {
            'dia': ['icontains'],
            
        }