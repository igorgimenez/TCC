from .models import Forum
import django_filters

class ForumFilter(django_filters.FilterSet):

    class Meta:
        model = Forum
        fields = {
            'titulo': ['icontains'],
            
        }