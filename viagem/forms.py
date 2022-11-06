from django import forms  
from viagem.models import Viagem  
class ViagemForm(forms.ModelForm):  
    class Meta:  
        model = Viagem  
        fields = "__all__"  