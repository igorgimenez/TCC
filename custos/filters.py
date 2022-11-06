from .models import Custo
import django_filters

class CustoFilter(django_filters.FilterSet):

    class Meta:
        model = Custo
        fields = {
            'valor': ['icontains'],
            
        }