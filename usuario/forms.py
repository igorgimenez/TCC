from usuario.models import Usuario  
from django import forms  

class UsuarioForm(forms.ModelForm):  
    class Meta:  
        model = Usuario  
        fields = "__all__"  