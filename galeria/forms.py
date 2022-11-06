from django import forms  
from galeria.models import FotoGaleria, Galeria  
class GaleriaForm(forms.ModelForm): 

    class Meta:  
        model = Galeria  
        fields = "__all__"  


class FotoGaleriaForm(forms.ModelForm): 

    class Meta:  
        model = FotoGaleria  
        fields = "__all__"