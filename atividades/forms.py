from django import forms  
from atividades.models import Atividade  
class AtividadesForm(forms.ModelForm): 
    

    v_id = forms.CharField(required=False)
    
    class Meta:  
        model = Atividade  
        fields = "__all__"  